-- MySQL Script generated by Transformo Framework
-- Tuesday, April 26, 2022 14:54:24

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
-- Schema output_database
-- -----------------------------------------------------

DROP SCHEMA IF EXISTS `output_database` ;
CREATE SCHEMA IF NOT EXISTS `output_database` DEFAULT CHARACTER SET UTF8MB4 ;
USE `output_database` ;


-- -----------------------------------------------------
-- Table  `output_database`.`post`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `output_database`.`post` ;
CREATE TABLE IF NOT EXISTS `output_database`.`post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(25)  NOT NULL,
  `body` TEXT  NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = UTF8MB4;

INSERT INTO `output_database`.`post` 
  SELECT * FROM `base1`.`post` ;

-- -----------------------------------------------------
-- Table  `output_database`.`post_meta`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `output_database`.`post_meta` ;
CREATE TABLE IF NOT EXISTS `output_database`.`post_meta` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `author` VARCHAR(25)  NOT NULL,
  post_id INT,
  PRIMARY KEY (id),
  CONSTRAINT FOREIGN KEY (post_id) REFERENCES post (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = UTF8MB4;

INSERT INTO `output_database`.`post_meta` 
  SELECT * FROM `base1`.`post_meta` ;

-- -----------------------------------------------------
-- Table  `output_database`.`vieja`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `output_database`.`vieja` ;
CREATE TABLE IF NOT EXISTS `output_database`.`vieja` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(50)  NOT NULL,
  `oter` NUMBER  NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = UTF8MB4;

INSERT INTO `output_database`.`vieja` 
  SELECT * FROM `base1`.`vieja` ;

-- -----------------------------------------------------
-- Transformation  ChangeAuthorType
-- -----------------------------------------------------

ALTER TABLE `output_database`.`post_meta`
  MODIFY COLUMN `author` VARCHAR(100);

-- -----------------------------------------------------
-- Transformation  RenameAuthorName
-- -----------------------------------------------------

ALTER TABLE `output_database`.`post_meta`
  RENAME COLUMN `author` TO `owner`;

-- -----------------------------------------------------
-- Transformation  DeleteAuthor
-- -----------------------------------------------------

ALTER TABLE `output_database`.`post_meta`
  DROP COLUMN `owner`;

-- -----------------------------------------------------
-- Transformation  CreateSummary
-- -----------------------------------------------------

ALTER TABLE `output_database`.`post_meta`
  ADD COLUMN `summary` TEXT;

-- -----------------------------------------------------
-- Transformation  MoveBody
-- -----------------------------------------------------

ALTER TABLE `output_database`.`post_meta`
  ADD COLUMN `body` TEXT;

INSERT INTO `output_database`.`post_meta` (`body`) 
  SELECT `body` FROM `base1`.`post`;

ALTER TABLE `output_database`.`post`
  DROP COLUMN `body`;

-- -----------------------------------------------------
-- Transformation  CreateComments
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `output_database`.`comment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id))
ENGINE = InnoDB
DEFAULT CHARACTER SET = UTF8MB4;

-- -----------------------------------------------------
-- Transformation  CreateTextInComment
-- -----------------------------------------------------

ALTER TABLE `output_database`.`comment`
  ADD COLUMN `title` VARCHAR(100);

-- -----------------------------------------------------
-- Transformation  CreateRelationBetweenCommentAndPost
-- -----------------------------------------------------

ALTER TABLE `output_database`.`comment`
  ADD COLUMN `post_id` INT NOT NULL;

ALTER TABLE `output_database`.`comment`
    ADD CONSTRAINT `fk_post_id` 
    FOREIGN KEY (`post_id`) 
    REFERENCES `post` (`id`);

-- -----------------------------------------------------
-- Transformation  RenameCommentToReview
-- -----------------------------------------------------

RENAME TABLE `output_database`.`comment` 
  TO  `review`;

-- -----------------------------------------------------
-- Transformation  DeleteReview
-- -----------------------------------------------------

DROP TABLE `output_database`.`review`

