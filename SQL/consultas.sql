-- Consultas del pruecto murcia: 
USE proyecto_murcia_definitivo;
-- Autor más prolífico: 
-- En solitario:

SELECT nombre_autor
FROM autores_murcia
WHERE nombre_autor IN (
    SELECT nombre_autor
    FROM obras_murcia
    GROUP BY nombre_autor
    ORDER BY COUNT(titulo) DESC
);

SELECT * FROM autores_murcia; 
SELECT * FROM obras_murcia COUNT(tematica) AS temas FROM obras_murcia;

-- En estas categorías: pintura, escultura y fotografía:




-- ¿Categoría más frecuente?


-- ¿Autor más frecuente en la categoría más frecuente?


-- ¿Autor más frecuente en la temática más frecuente?


-- Algún usuario que destaque en cuanto a obras en su poder? 

