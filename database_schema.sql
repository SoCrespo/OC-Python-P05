-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema offdb2020p5
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `offdb2020p5` DEFAULT CHARACTER SET latin1 ;
USE `offdb2020p5` ;

-- -----------------------------------------------------
-- Table `category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `category` ;

CREATE TABLE IF NOT EXISTS `category` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT 'corresponds to categories field in OFF answer',
  `full_name` VARCHAR(70) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `product` ;

CREATE TABLE IF NOT EXISTS `product` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `brand` VARCHAR(200) NOT NULL COMMENT 'Corresponds to brands_tags',
  `name` VARCHAR(200) NOT NULL COMMENT 'Corresponds to product_name_fr',
  `full_name` VARCHAR(200) CHARACTER SET 'utf8' NULL DEFAULT NULL COMMENT 'Corresponds to generic_name_fr',
  `nutriscore` CHAR(1) NOT NULL COMMENT 'corresponds to nutriscore_grades',
  `cat_id` INT(11) NOT NULL,
  `url` VARCHAR(2000) NOT NULL COMMENT 'corresponds to url',
  `ingredients` VARCHAR(2000) NULL DEFAULT NULL COMMENT 'corresponds to ingredients_text',
  `stores` VARCHAR(200) NULL DEFAULT NULL COMMENT 'Corresponds to stores',
  `quantity` VARCHAR(8) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_product_category` (`cat_id` ASC),
  INDEX `idx_prod_name` (`name` ASC),
  CONSTRAINT `fk_product_category`
    FOREIGN KEY (`cat_id`)
    REFERENCES `category` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `substitution`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `substitution` ;

CREATE TABLE IF NOT EXISTS `substitution` (
  `origin_id` INT(11) NOT NULL,
  `substitute_id` INT(11) NOT NULL,
  PRIMARY KEY (`origin_id`, `substitute_id`),
  INDEX `fk_origin_product_idx` (`origin_id` ASC),
  INDEX `fk_substitute_product_idx` (`substitute_id` ASC),
  CONSTRAINT `fk_origin_product`
    FOREIGN KEY (`origin_id`)
    REFERENCES `product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_substitute_product`
    FOREIGN KEY (`substitute_id`)
    REFERENCES `product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
