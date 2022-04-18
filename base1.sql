
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


DROP SCHEMA IF EXISTS `base1` ;

CREATE SCHEMA IF NOT EXISTS `base1` DEFAULT CHARACTER SET utf8 ;
USE `base1` ;

-- TABLES

DROP TABLE IF EXISTS `post` ;

CREATE TABLE IF NOT EXISTS post (
  id int(4) NOT NULL AUTO_INCREMENT,
  title varchar(20) NOT NULL,
  body varchar(20) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1;

DROP TABLE IF EXISTS `postmeta` ;
CREATE TABLE IF NOT EXISTS postmeta (
  id int(4) NOT NULL AUTO_INCREMENT,
  author varchar(20) NOT NULL,
  idpostmeta int(4) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT FOREIGN KEY (idpostmeta) REFERENCES post (id)
) ENGINE=InnoDB AUTO_INCREMENT=1;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
