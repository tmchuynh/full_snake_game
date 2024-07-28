-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema snake_game
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema snake_game
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `snake_game` DEFAULT CHARACTER SET utf8 ;
USE `snake_game` ;

-- -----------------------------------------------------
-- Table `snake_game`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `snake_game`.`user` ;

CREATE TABLE IF NOT EXISTS `snake_game`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `date_created` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `snake_game`.`high_score`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `snake_game`.`high_score` ;

CREATE TABLE IF NOT EXISTS `snake_game`.`high_score` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `difficulty` VARCHAR(45) NULL,
  `obstacles` INT NULL,
  `obstaclesMove` VARCHAR(45) BINARY NOT NULL,
  `peacefulMode` VARCHAR(45) BINARY NOT NULL,
  `user_id` INT NOT NULL,
  `date_created` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `date_uipdated` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_high score_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_high score_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `snake_game`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
