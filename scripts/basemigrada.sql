-- MySQL Script generated by Transformo Framework
-- Monday, May 16, 2022 09:55:49

--      David Romero Organvidez
--      Technical Researcher
--      drorganvidez@us.es
--      University of Seville

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Schema basemigrada
-- -----------------------------------------------------

DROP SCHEMA IF EXISTS `basemigrada` ;
CREATE SCHEMA IF NOT EXISTS `basemigrada` DEFAULT CHARACTER SET UTF8MB4 ;
USE `basemigrada` ;


-- -----------------------------------------------------
-- Table  `basemigrada`.`post`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `basemigrada`.`post` ;
CREATE TABLE IF NOT EXISTS `basemigrada`.`post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(25)  NOT NULL,
  `body` TEXT  NOT NULL,
  `attribute_move` TEXT  NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = UTF8MB4;

INSERT INTO `basemigrada`.`post` 
  SELECT * FROM `base1`.`post` ;

-- -----------------------------------------------------
-- Table  `basemigrada`.`post_meta`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `basemigrada`.`post_meta` ;
CREATE TABLE IF NOT EXISTS `basemigrada`.`post_meta` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `author` VARCHAR(25)  NOT NULL,
  post_id INT,
  PRIMARY KEY (id),
  CONSTRAINT FOREIGN KEY (post_id) REFERENCES post (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = UTF8MB4;

INSERT INTO `basemigrada`.`post_meta` 
  SELECT * FROM `base1`.`post_meta` ;

-- -----------------------------------------------------
-- Transformation  RetypeAttributeAction
-- -----------------------------------------------------

ALTER TABLE `basemigrada`.`post`
  MODIFY COLUMN `body` varchar(100);

-- -----------------------------------------------------
-- Transformation  MoveAttributeAction
-- -----------------------------------------------------

ALTER TABLE `basemigrada`.`post`
  ADD COLUMN `author` VARCHAR(25);

INSERT INTO `basemigrada`.`post` (`author`) 
  SELECT `author` FROM `base1`.`post_meta`;

ALTER TABLE `basemigrada`.`post_meta`
  DROP COLUMN `author`;

-- -----------------------------------------------------
-- Transformation  DeleteEntityAction
-- -----------------------------------------------------

DROP TABLE `basemigrada`.`post_meta`

