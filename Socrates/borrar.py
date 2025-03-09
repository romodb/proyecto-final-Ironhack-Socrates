# Dao Get
def obtener_usuarios():
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)  # Obtener resultados como diccionarios
        query = "SELECT id, nombre, email FROM usuarios"
        cursor.execute(query)
        usuarios = cursor.fetchall()  # Obtener todos los resultados
        return usuarios
    except Error as e:
        print(f"Error al obtener usuarios: {e}")
        return []
    
# Endpoin get:
@app.get("/api/usuarios")
async def obtener_usuarios_endpoint():
    usuarios = obtener_usuarios()  # Llamada a la función DAO
    if usuarios:
        return JSONResponse(content=usuarios, status_code=200)  # Respuesta con lista de usuarios
    else:
        return JSONResponse(content={"mensaje": "No se encontraron usuarios"}, status_code=404)  # Si no hay usuarios
    
# Función para crear un nuevo usuario (post), query:
def crear_usuario(db: Session, nombre: str, email: str):
    db_usuario = Usuario(nombre=nombre, email=email)
    db.add(db_usuario)  # Agregar el usuario a la sesión
    db.commit()  # Guardar los cambios en la base de datos
    db.refresh(db_usuario)  # Obtener los datos actualizados del usuario (incluyendo el ID generado)
    return db_usuario

# Endpoint para crear un nuevo usuario (post):
@app.post("/api/usuarios", response_model=UsuarioCreate)
async def crear_nuevo_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Verificar si el correo electrónico ya existe
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="El correo electrónico ya está en uso")
    # Llamar a la función para crear el usuario
    nuevo_usuario = crear_usuario(db=db, nombre=usuario.nombre, email=usuario.email)
    return nuevo_usuario

# Función para actualizar un usuario en la base de datos (put):
def actualizar_usuario(db: Session, usuario_id: int, nombre: str, email: str):
    # Buscar el usuario por su ID
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    # Si el usuario no existe, devolver None
    if db_usuario is None:
        return None
    # Actualizar los campos
    db_usuario.nombre = nombre
    db_usuario.email = email
    # Guardar los cambios en la base de datos
    db.commit()
    db.refresh(db_usuario)  # Refrescar los datos del usuario
    return db_usuario

# Endpoint para actualizar los datos de un usuario (put):
@app.put("/api/usuarios/{usuario_id}", response_model=UsuarioUpdate)
async def actualizar_usuario_endpoint(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    # Llamar a la función para actualizar el usuario
    usuario_actualizado = actualizar_usuario(db=db, usuario_id=usuario_id, nombre=usuario.nombre, email=usuario.email)
    # Si no se encontró el usuario, lanzar una excepción 404
    if usuario_actualizado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_actualizado

# Función para eliminar un usuario de la base de datos (delete):
def eliminar_usuario(db: Session, usuario_id: int):
    # Buscar al usuario por su ID
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    # Si el usuario no existe, devolver None
    if db_usuario is None:
        return None
    # Eliminar el usuario de la base de datos
    db.delete(db_usuario)
    db.commit()  # Guardar los cambios en la base de datos
    return db_usuario

# Endpoint para eliminar un usuario
@app.delete("/api/usuarios/{usuario_id}", response_model=Usuario)
async def eliminar_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    # Llamar a la función para eliminar el usuario
    usuario_eliminado = eliminar_usuario(db=db, usuario_id=usuario_id)
    # Si no se encuentra el usuario, lanzar una excepción 404
    if usuario_eliminado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_eliminado
