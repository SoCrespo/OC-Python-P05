-- -----------------------------------------------------
-- Database openfoodfacts
-- -----------------------------------------------------

DROP DATABASE IF EXISTS openfoodfacts;
CREATE DATABASE IF NOT EXISTS openfoodfacts;

-- -----------------------------------------------------
-- Table Category
-- -----------------------------------------------------
DROP TABLE IF EXISTS openfoodfacts.Category ;

CREATE TABLE IF NOT EXISTS openfoodfacts.Category(
  cat_id INT NOT NULL AUTO_INCREMENT,
  cat_name VARCHAR(50) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (cat_id)
  )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Shop
-- -----------------------------------------------------
DROP TABLE IF EXISTS openfoodfacts.Shop ;

CREATE TABLE IF NOT EXISTS openfoodfacts.Shop (
  shop_id INT NOT NULL AUTO_INCREMENT,
  shop_name VARCHAR(30) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (shop_id)
  )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table Product
-- -----------------------------------------------------
DROP TABLE IF EXISTS openfoodfacts.Product ;

CREATE TABLE IF NOT EXISTS openfoodfacts.Product (
  prod_id INT NOT NULL AUTO_INCREMENT,
  prod_name VARCHAR(50) NOT NULL,
  prod_full_name VARCHAR(50) CHARACTER SET utf8 NOT NULL,
  prod_nutriscore_index CHAR(1) NOT NULL,
  cat_id INT NOT NULL,
  shop_id INT,
  PRIMARY KEY (prod_id),
  
  CONSTRAINT fk_shop_id
    FOREIGN KEY (shop_id)
    REFERENCES Shop(shop_id),

  CONSTRAINT fk_product_category
    FOREIGN KEY (cat_id)
    REFERENCES Category(cat_id)
    )
ENGINE = InnoDB;
