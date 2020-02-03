-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema openfoodfacts
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `openfoodfacts` ;

-- -----------------------------------------------------
-- Schema openfoodfacts
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `openfoodfacts` DEFAULT CHARACTER SET latin1 ;
USE `openfoodfacts` ;

-- -----------------------------------------------------
-- Table `openfoodfacts`.`category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfoodfacts`.`category` ;

CREATE TABLE IF NOT EXISTS `openfoodfacts`.`category` (
  `cat_id` INT(11) NOT NULL AUTO_INCREMENT,
  `cat_name` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT 'corresponds to categories field in OFF answer',
  PRIMARY KEY (`cat_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openfoodfacts`.`product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfoodfacts`.`product` ;

CREATE TABLE IF NOT EXISTS `openfoodfacts`.`product` (
  `prod_id` INT(11) NOT NULL AUTO_INCREMENT,
  `prod_brand` VARCHAR(50) NOT NULL COMMENT 'Corresponds to brands_tags',
  `prod_name` VARCHAR(50) NOT NULL COMMENT 'Corresponds to product_name_fr',
  `prod_full_name` VARCHAR(50) CHARACTER SET 'utf8' NULL COMMENT 'Corresponds to generic_name_fr',
  `prod_nutriscore_index` CHAR(1) NOT NULL COMMENT 'corresponds to nutriscore_grades',
  `cat_id` INT(11) NOT NULL,
  `prod_url` VARCHAR(2000) NOT NULL COMMENT 'corresponds to url',
  `prod_ingredients` TEXT(2000) NULL COMMENT 'corresponds to ingredients_text',
  `prod_stores` VARCHAR(200) NULL COMMENT 'Corresponds to stores',
  PRIMARY KEY (`prod_id`),
  INDEX `fk_product_category` (`cat_id` ASC),
  INDEX `idx_prod_name` (`prod_name` ASC),
  CONSTRAINT `fk_product_category`
    FOREIGN KEY (`cat_id`)
    REFERENCES `openfoodfacts`.`category` (`cat_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openfoodfacts`.`substition`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfoodfacts`.`substition` ;

CREATE TABLE IF NOT EXISTS `openfoodfacts`.`substition` (
  `sub_id` INT NOT NULL AUTO_INCREMENT,
  `sub_origin_id` INT NOT NULL,
  `sub_substitute_id` INT NOT NULL,
  `sub_create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`sub_id`),
  INDEX `fk_origin_product_idx` (`sub_origin_id` ASC),
  INDEX `fk_substitute_product_idx` (`sub_substitute_id` ASC),
  CONSTRAINT `fk_origin_product`
    FOREIGN KEY (`sub_origin_id`)
    REFERENCES `openfoodfacts`.`product` (`prod_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_substitute_product`
    FOREIGN KEY (`sub_substitute_id`)
    REFERENCES `openfoodfacts`.`product` (`prod_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;