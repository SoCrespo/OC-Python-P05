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
  `cat_name` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY (`cat_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openfoodfacts`.`store`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfoodfacts`.`store` ;

CREATE TABLE IF NOT EXISTS `openfoodfacts`.`store` (
  `store_id` INT(11) NOT NULL AUTO_INCREMENT,
  `store_name` VARCHAR(30) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY (`store_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `openfoodfacts`.`product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfoodfacts`.`product` ;

CREATE TABLE IF NOT EXISTS `openfoodfacts`.`product` (
  `prod_id` INT(11) NOT NULL AUTO_INCREMENT,
  `prod_name` VARCHAR(50) NOT NULL,
  `prod_full_name` VARCHAR(50) CHARACTER SET 'utf8' NULL,
  `prod_nutriscore_index` CHAR(1) NOT NULL,
  `cat_id` INT(11) NOT NULL,
  `store_id` INT(11) ,
  `prod_url` VARCHAR(2000) NOT NULL,
  `prod_ingredients` TEXT(2000) ,
  PRIMARY KEY (`prod_id`),
  INDEX `fk_shop_id` (`store_id` ASC),
  INDEX `fk_product_category` (`cat_id` ASC),
  INDEX `idx_prod_name` (`prod_name` ASC),
  CONSTRAINT `fk_product_category`
    FOREIGN KEY (`cat_id`)
    REFERENCES `openfoodfacts`.`category` (`cat_id`),
  CONSTRAINT `fk_shop_id`
    FOREIGN KEY (`store_id`)
    REFERENCES `openfoodfacts`.`store` (`store_id`))
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

