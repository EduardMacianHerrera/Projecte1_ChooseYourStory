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
  `date_mod` DATETIME NOT NULL,
  `user_mod` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_USER`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`CHARACTERS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`CHARACTERS` (
  `ID_CHARACTER` INT NOT NULL AUTO_INCREMENT,
  `character_name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(250) NOT NULL,
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NOT NULL,
  `user_mod` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_CHARACTER`),
  UNIQUE INDEX `character_name_UNIQUE` (`character_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`RECORD`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`RECORD` (
  `ID_RECORD` INT NOT NULL AUTO_INCREMENT,
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NOT NULL,
  `user_mod` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_RECORD`))
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
  `date_mod` DATETIME NOT NULL,
  `user_mod` VARCHAR(45) NOT NULL,
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
  `date_mod` DATETIME NOT NULL,
  `user_mod` VARCHAR(45) NOT NULL,
  `FK_ID_CHARACTER` INT NOT NULL,
  `FK_ID_USER` INT NOT NULL,
  `FK_ID_RECORD` INT NOT NULL,
  `FK_ID_ADVENTURE` INT NOT NULL,
  PRIMARY KEY (`ID_GAME`),
  INDEX `fk_character_game_idx` (`FK_ID_CHARACTER` ASC) VISIBLE,
  INDEX `fk_user_game_idx` (`FK_ID_USER` ASC) VISIBLE,
  INDEX `fk_record_game_idx` (`FK_ID_RECORD` ASC) VISIBLE,
  INDEX `fk_adventure_game_idx` (`FK_ID_ADVENTURE` ASC) VISIBLE,
  CONSTRAINT `fk_character_game`
    FOREIGN KEY (`FK_ID_CHARACTER`)
    REFERENCES `project`.`CHARACTERS` (`ID_CHARACTER`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_game`
    FOREIGN KEY (`FK_ID_USER`)
    REFERENCES `project`.`USER` (`ID_USER`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_record_game`
    FOREIGN KEY (`FK_ID_RECORD`)
    REFERENCES `project`.`RECORD` (`ID_RECORD`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_adventure_game`
    FOREIGN KEY (`FK_ID_ADVENTURE`)
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
  `date_mod` DATETIME NOT NULL,
  `user_mod` VARCHAR(45) NOT NULL,
  `FK_ID_ADVENTURE` INT NOT NULL,
  `FK_ID_STEP` INT NOT NULL,
  PRIMARY KEY (`ID_STEP`),
  INDEX `fk_adventure_step_idx` (`FK_ID_ADVENTURE` ASC) VISIBLE,
  INDEX `fk_STEP_STEP1_idx` (`FK_ID_STEP` ASC) VISIBLE,
  CONSTRAINT `fk_adventure_step`
    FOREIGN KEY (`FK_ID_ADVENTURE`)
    REFERENCES `project`.`ADVENTURE` (`ID_ADVENTURE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_step_step`
    FOREIGN KEY (`FK_ID_STEP`)
    REFERENCES `project`.`STEP` (`ID_STEP`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`OPTION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`OPTION` (
  `ID_OPTION` INT NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(500) NOT NULL,
  `user_creation` VARCHAR(45) NOT NULL,
  `date_creation` DATETIME NOT NULL,
  `date_mod` DATETIME NOT NULL,
  `user_mod` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_OPTION`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`RECORD_HAS_OPTION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`RECORD_HAS_OPTION` (
  `FK_ID_OPTION` INT NOT NULL,
  `FK_ID_RECORD` INT NOT NULL,
  PRIMARY KEY (`FK_ID_OPTION`, `FK_ID_RECORD`),
  INDEX `fk_OPTION_has_RECORD_RECORD1_idx` (`FK_ID_RECORD` ASC) VISIBLE,
  INDEX `fk_OPTION_has_RECORD_OPTION1_idx` (`FK_ID_OPTION` ASC) VISIBLE,
  CONSTRAINT `fk_option_has`
    FOREIGN KEY (`FK_ID_OPTION`)
    REFERENCES `project`.`OPTION` (`ID_OPTION`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_record_has`
    FOREIGN KEY (`FK_ID_RECORD`)
    REFERENCES `project`.`RECORD` (`ID_RECORD`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`STARS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`STARS` (
  `FK_ID_ADVENTURE` INT NOT NULL,
  `FK_ID_CHARACTER` INT NOT NULL,
  PRIMARY KEY (`FK_ID_ADVENTURE`, `FK_ID_CHARACTER`),
  INDEX `fk_ADVENTURE_has_CHARACTER_CHARACTER1_idx` (`FK_ID_CHARACTER` ASC) VISIBLE,
  INDEX `fk_ADVENTURE_has_CHARACTER_ADVENTURE1_idx` (`FK_ID_ADVENTURE` ASC) VISIBLE,
  CONSTRAINT `fk_adventure_stars`
    FOREIGN KEY (`FK_ID_ADVENTURE`)
    REFERENCES `project`.`ADVENTURE` (`ID_ADVENTURE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_character_stars`
    FOREIGN KEY (`FK_ID_CHARACTER`)
    REFERENCES `project`.`CHARACTERS` (`ID_CHARACTER`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`RECORD_HAS_STEP`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`RECORD_HAS_STEP` (
  `FK_ID_STEP` INT NOT NULL,
  `FK_ID_RECORD` INT NOT NULL,
  PRIMARY KEY (`FK_ID_STEP`, `FK_ID_RECORD`),
  INDEX `fk_STEP_has_RECORD_RECORD1_idx` (`FK_ID_RECORD` ASC) VISIBLE,
  INDEX `fk_STEP_has_RECORD_STEP1_idx` (`FK_ID_STEP` ASC) VISIBLE,
  CONSTRAINT `fk_step_record_has_step`
    FOREIGN KEY (`FK_ID_STEP`)
    REFERENCES `project`.`STEP` (`ID_STEP`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_record_record_has_step`
    FOREIGN KEY (`FK_ID_RECORD`)
    REFERENCES `project`.`RECORD` (`ID_RECORD`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`GOES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`GOES` (
  `FK_ID_STEP` INT NOT NULL,
  `FK_ID_OPTION` INT NOT NULL,
  PRIMARY KEY (`FK_ID_STEP`, `FK_ID_OPTION`),
  INDEX `fk_STEP_has_OPTION_OPTION1_idx` (`FK_ID_OPTION` ASC) VISIBLE,
  INDEX `fk_STEP_has_OPTION_STEP1_idx` (`FK_ID_STEP` ASC) VISIBLE,
  CONSTRAINT `fk_step_goes`
    FOREIGN KEY (`FK_ID_STEP`)
    REFERENCES `project`.`STEP` (`ID_STEP`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_option_goes`
    FOREIGN KEY (`FK_ID_OPTION`)
    REFERENCES `project`.`OPTION` (`ID_OPTION`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`COMES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`COMES` (
  `FK_ID_STEP` INT NOT NULL,
  `FK_ID_OPTION` INT NOT NULL,
  PRIMARY KEY (`FK_ID_STEP`, `FK_ID_OPTION`),
  INDEX `fk_STEP_has_OPTION_OPTION1_idx` (`FK_ID_OPTION` ASC) VISIBLE,
  INDEX `fk_STEP_has_OPTION_STEP1_idx` (`FK_ID_STEP` ASC) VISIBLE,
  CONSTRAINT `fk_step_comes`
    FOREIGN KEY (`FK_ID_STEP`)
    REFERENCES `project`.`STEP` (`ID_STEP`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_option_comes`
    FOREIGN KEY (`FK_ID_OPTION`)
    REFERENCES `project`.`OPTION` (`ID_OPTION`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`ANSWER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`ANSWER` (
  `ID_ANSWER` INT NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(1000) NOT NULL,
  `FK_ID_OPTION` INT NOT NULL,
  `ANSWER_ID_ANSWER` INT NOT NULL,
  `ANSWER_FK_ID_OPTION` INT NOT NULL,
  PRIMARY KEY (`ID_ANSWER`, `FK_ID_OPTION`),
  INDEX `fk_option_answer_idx` (`FK_ID_OPTION` ASC) VISIBLE,
  INDEX `fk_ANSWER_ANSWER1_idx` (`ANSWER_ID_ANSWER` ASC, `ANSWER_FK_ID_OPTION` ASC) VISIBLE,
  CONSTRAINT `fk_option_answer`
    FOREIGN KEY (`FK_ID_OPTION`)
    REFERENCES `project`.`OPTION` (`ID_OPTION`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ANSWER_ANSWER1`
    FOREIGN KEY (`ANSWER_ID_ANSWER` , `ANSWER_FK_ID_OPTION`)
    REFERENCES `project`.`ANSWER` (`ID_ANSWER` , `FK_ID_OPTION`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
