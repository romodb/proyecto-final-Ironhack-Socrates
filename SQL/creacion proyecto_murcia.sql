-- MySQL Script generated by MySQL Workbench
-- Thu Feb 27 19:32:12 2025
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuarios_murcia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`usuarios_murcia` ;

CREATE TABLE IF NOT EXISTS `mydb`.`usuarios_murcia` (
  `id_usuario` INT NULL AUTO_INCREMENT,
  `nombre_usuario` VARCHAR(250) NOT NULL,
  `id_inventario` VARCHAR(50) NULL,
  `municipio` VARCHAR(100) NULL,
  `pedania` VARCHAR(100) NULL,
  `dirección` VARCHAR(250) NULL,obras_murcia
  `C.P.` VARCHAR(6) NULL,
  PRIMARY KEY (`id_usuario`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `nombre_usuario_UNIQUE` ON `mydb`.`usuarios_murcia` (`nombre_usuario` ASC) VISIBLE;

CREATE UNIQUE INDEX `id_inventario_UNIQUE` ON `mydb`.`usuarios_murcia` (`id_inventario` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `mydb`.`autores_murcia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`autores_murcia` ;

CREATE TABLE IF NOT EXISTS `mydb`.`autores_murcia` (
  `id_autor` INT NULL AUTO_INCREMENT,
  `nombre_autor` VARCHAR(150) NULL,
  `id_inventario` VARCHAR(250) NULL,
  PRIMARY KEY (`id_autor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`obras_murcia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`obras_murcia` ;

CREATE TABLE IF NOT EXISTS `mydb`.`obras_murcia` (
  `id_inventario` INT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(250) NOT NULL,
  `id_autor` INT NOT NULL,
  `fondo(cm)` INT NULL,
  `ancho(cm)` INT NULL,
  `alto(cm)` INT NULL,
  `tecnica` VARCHAR(45) NOT NULL,
  `material_base` VARCHAR(100) NULL,
  `material_secundario` VARCHAR(100) NULL,
  `tematica` VARCHAR(100) NULL,
  `id_usuario` INT NOT NULL,
  PRIMARY KEY (`id_inventario`),
  CONSTRAINT `id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `mydb`.`usuarios_murcia` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_autor`
    FOREIGN KEY (`id_autor`)
    REFERENCES `mydb`.`autores_murcia` (`id_autor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `id_autor_UNIQUE` ON `mydb`.`obras_murcia` (`id_autor` ASC) VISIBLE;

CREATE INDEX `id_usuario_idx` ON `mydb`.`obras_murcia` (`id_usuario` ASC) VISIBLE;

USE `mydb` ;

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `mydb`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`view1`;
DROP VIEW IF EXISTS `mydb`.`view1` ;
USE `mydb`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
obras_murciaproyecto_murcia