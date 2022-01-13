-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project` DEFAULT CHARACTER SET utf8 ;
USE `project` ;

-- -----------------------------------------------------
-- Table `project`.`USER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`USER` (
  `ID_USER` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(10) NOT NULL,
  `password` VARCHAR(12) NOT NULL,
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NULL,
  `user_mod` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_USER`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`CHARACTER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`CHARACTER` (
  `ID_CHARACTER` INT NOT NULL AUTO_INCREMENT,
  `character_name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(250) NOT NULL,
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NULL,
  `user_mod` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_CHARACTER`),
  UNIQUE INDEX `character_name_UNIQUE` (`character_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`ADVENTURE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`ADVENTURE` (
  `ID_ADVENTURE` INT NOT NULL AUTO_INCREMENT,
  `adventure_name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(250) NOT NULL,
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NULL,
  `user_mod` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_ADVENTURE`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`GAME`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`GAME` (
  `ID_GAME` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NULL,
  `user_mod` VARCHAR(45) NULL,
  `ID_CHARACTER` INT NOT NULL,
  `ID_USER` INT NOT NULL,
  `ID_ADVENTURE` INT NOT NULL,
  PRIMARY KEY (`ID_GAME`),
  INDEX `fk_character_game_idx` (`ID_CHARACTER` ASC) VISIBLE,
  INDEX `fk_user_game_idx` (`ID_USER` ASC) VISIBLE,
  INDEX `fk_adventure_game_idx` (`ID_ADVENTURE` ASC) VISIBLE,
  CONSTRAINT `fk_character_game`
    FOREIGN KEY (`ID_CHARACTER`)
    REFERENCES `project`.`CHARACTER` (`ID_CHARACTER`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_game`
    FOREIGN KEY (`ID_USER`)
    REFERENCES `project`.`USER` (`ID_USER`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_adventure_game`
    FOREIGN KEY (`ID_ADVENTURE`)
    REFERENCES `project`.`ADVENTURE` (`ID_ADVENTURE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`STEP`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`STEP` (
  `ID_STEP` INT NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(500) NOT NULL,
  `the_end` BIT NOT NULL,
  `start` BIT NOT NULL,
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NULL,
  `user_mod` VARCHAR(45) NULL,
  `ID_ADVENTURE` INT NOT NULL,
  PRIMARY KEY (`ID_STEP`),
  INDEX `fk_adventure_step_idx` (`ID_ADVENTURE` ASC) VISIBLE,
  CONSTRAINT `fk_adventure_step`
    FOREIGN KEY (`ID_ADVENTURE`)
    REFERENCES `project`.`ADVENTURE` (`ID_ADVENTURE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`OPTION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`OPTION` (
  `ID_OPTION` INT NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(500) NOT NULL,
  `answer` VARCHAR(1000) NOT NULL,
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NULL,
  `user_mod` VARCHAR(45) NULL,
  `ID_STEP_FROM` INT NOT NULL,
  `ID_STEP_TO` INT NOT NULL,
  PRIMARY KEY (`ID_OPTION`, `ID_STEP_FROM`, `ID_STEP_TO`),
  INDEX `fk_OPTION_STEP1_idx` (`ID_STEP_FROM` ASC) VISIBLE,
  INDEX `fk_OPTION_STEP2_idx` (`ID_STEP_TO` ASC) VISIBLE,
  CONSTRAINT `fk_OPTION_STEP1`
    FOREIGN KEY (`ID_STEP_FROM`)
    REFERENCES `project`.`STEP` (`ID_STEP`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_OPTION_STEP2`
    FOREIGN KEY (`ID_STEP_TO`)
    REFERENCES `project`.`STEP` (`ID_STEP`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`RECORD`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`RECORD` (
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NULL,
  `user_mod` VARCHAR(45) NULL,
  `ID_GAME` INT NOT NULL,
  `ID_OPTION` INT NOT NULL,
  `ID_STEP_FROM` INT NOT NULL,
  `ID_STEP_TO` INT NOT NULL,
  PRIMARY KEY (`ID_GAME`, `ID_OPTION`, `ID_STEP_FROM`, `ID_STEP_TO`),
  INDEX `fk_RECORD_OPTION1_idx` (`ID_OPTION` ASC, `ID_STEP_FROM` ASC, `ID_STEP_TO` ASC) VISIBLE,
  CONSTRAINT `fk_RECORD_GAME1`
    FOREIGN KEY (`ID_GAME`)
    REFERENCES `project`.`GAME` (`ID_GAME`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RECORD_OPTION1`
    FOREIGN KEY (`ID_OPTION` , `ID_STEP_FROM` , `ID_STEP_TO`)
    REFERENCES `project`.`OPTION` (`ID_OPTION` , `ID_STEP_FROM` , `ID_STEP_TO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`STARS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`STARS` (
  `ID_ADVENTURE` INT NOT NULL,
  `ID_CHARACTER` INT NOT NULL,
  PRIMARY KEY (`ID_ADVENTURE`, `ID_CHARACTER`),
  INDEX `fk_ADVENTURE_has_CHARACTER_CHARACTER1_idx` (`ID_CHARACTER` ASC) VISIBLE,
  INDEX `fk_ADVENTURE_has_CHARACTER_ADVENTURE1_idx` (`ID_ADVENTURE` ASC) VISIBLE,
  CONSTRAINT `fk_adventure_stars`
    FOREIGN KEY (`ID_ADVENTURE`)
    REFERENCES `project`.`ADVENTURE` (`ID_ADVENTURE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_character_stars`
    FOREIGN KEY (`ID_CHARACTER`)
    REFERENCES `project`.`CHARACTER` (`ID_CHARACTER`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
