
CREATE SCHEMA IF NOT EXISTS project;
USE project ;

CREATE TABLE IF NOT EXISTS project.`USER` (
  ID_USER INT,
  username VARCHAR(10),
  `password` VARCHAR(12),
  user_creation VARCHAR(45),
  date_creation DATETIME,
  date_mod DATETIME,
  user_mod VARCHAR(45));
  
CREATE TABLE IF NOT EXISTS project.`CHARACTER` (
  ID_CHARACTER INT,
  character_name VARCHAR(45),
  `description` VARCHAR(250),
  user_creation VARCHAR(45),
  date_creation DATETIME,
  date_mod DATETIME,
  user_mod VARCHAR(45));
  
CREATE TABLE IF NOT EXISTS project.ADVENTURE (
  ID_ADVENTURE INT,
  adventure_name VARCHAR(45),
  `description` VARCHAR(250),
  user_creation VARCHAR(45),
  date_creation DATETIME,
  date_mod DATETIME,
  user_mod VARCHAR(45));
  
CREATE TABLE IF NOT EXISTS project.GAME (
  ID_GAME INT,
  `date` DATETIME,
  user_creation VARCHAR(45),
  date_creation DATETIME,
  date_mod DATETIME,
  user_mod VARCHAR(45),
  ID_CHARACTER INT,
  ID_USER INT,
  ID_ADVENTURE INT);
  
CREATE TABLE IF NOT EXISTS project.STEP (
  ID_STEP INT,
  `description` VARCHAR(500),
  the_end BIT,
  `start` BIT,
  user_creation VARCHAR(45),
  date_creation DATETIME,
  date_mod DATETIME,
  user_mod VARCHAR(45),
  ID_ADVENTURE INT);
  
CREATE TABLE IF NOT EXISTS project.`OPTION` (
  ID_OPTION INT,
  `description` VARCHAR(500),
  answer VARCHAR(1000),
  user_creation VARCHAR(45),
  date_creation DATETIME,
  date_mod DATETIME,
  user_mod VARCHAR(45),
  ID_STEP_FROM INT,
  ID_STEP_TO INT);
  
CREATE TABLE IF NOT EXISTS project.RECORD (
  user_creation VARCHAR(45),
  date_creation DATETIME,
  date_mod DATETIME,
  user_mod VARCHAR(45),
  ID_GAME INT,
  ID_STEP INT,
  ID_OPTION INT);
  
CREATE TABLE IF NOT EXISTS project.STARS (
  ID_ADVENTURE INT,
  ID_CHARACTER INT);
  