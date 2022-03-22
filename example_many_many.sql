-- MySQL Script generated by MySQL Workbench
-- Tue Mar 22 12:38:47 2022
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
-- Table `mydb`.`post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`post` ;

CREATE TABLE IF NOT EXISTS `mydb`.`post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(20) NOT NULL,
  `body` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`postmeta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`postmeta` ;

CREATE TABLE IF NOT EXISTS `mydb`.`postmeta` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `author` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`post_has_postmeta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`post_has_postmeta` ;

CREATE TABLE IF NOT EXISTS `mydb`.`post_has_postmeta` (
  `post_id` INT NOT NULL,
  `postmeta_id` INT NOT NULL,
  `postmeta_idpostmeta` INT NOT NULL,
  PRIMARY KEY (`post_id`, `postmeta_id`, `postmeta_idpostmeta`),
  INDEX `fk_post_has_postmeta_postmeta1_idx` (`postmeta_id` ASC, `postmeta_idpostmeta` ASC) VISIBLE,
  INDEX `fk_post_has_postmeta_post1_idx` (`post_id` ASC) VISIBLE,
  CONSTRAINT `fk_post_has_postmeta_post1`
    FOREIGN KEY (`post_id`)
    REFERENCES `mydb`.`post` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_post_has_postmeta_postmeta1`
    FOREIGN KEY (`postmeta_id`)
    REFERENCES `mydb`.`postmeta` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
