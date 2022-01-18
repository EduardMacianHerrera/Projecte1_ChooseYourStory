use project;

alter table `USER` 
	modify ID_USER INT NOT NULL AUTO_INCREMENT,
  modify username VARCHAR(10) NOT NULL,
  modify `password` VARCHAR(12) NOT NULL,
  modify user_creation VARCHAR(45) NOT NULL,
  modify date_creation DATETIME NOT NULL,
  modify date_mod DATETIME NULL,
  modify user_mod VARCHAR(45) NULL,
  add PRIMARY KEY (ID_USER),
  add UNIQUE INDEX username_UNIQUE (username);

alter table `CHARACTER`
	modify ID_CHARACTER INT NOT NULL AUTO_INCREMENT,
  modify character_name VARCHAR(45) NOT NULL,
  modify `description` VARCHAR(250) NOT NULL,
  modify user_creation VARCHAR(45) NOT NULL,
  modify date_creation DATETIME NOT NULL,
  modify date_mod DATETIME NULL,
  modify user_mod VARCHAR(45) NULL,
  add PRIMARY KEY (ID_CHARACTER),
  add UNIQUE INDEX character_name_UNIQUE (character_name);
  
alter table ADVENTURE
	modify ID_ADVENTURE INT NOT NULL AUTO_INCREMENT,
  modify adventure_name VARCHAR(45) NOT NULL,
  modify `description` VARCHAR(250) NOT NULL,
  modify user_creation VARCHAR(45) NOT NULL,
  modify date_creation DATETIME NOT NULL,
  modify date_mod DATETIME NULL,
  modify user_mod VARCHAR(45) NULL,
  add PRIMARY KEY (ID_ADVENTURE);
  
alter table GAME
	modify ID_GAME INT NOT NULL AUTO_INCREMENT,
  modify `date` DATETIME NOT NULL,
  modify user_creation VARCHAR(45) NOT NULL,
  modify date_creation DATETIME NOT NULL,
  modify date_mod DATETIME NULL,
  modify user_mod VARCHAR(45) NULL,
  modify ID_CHARACTER INT NOT NULL,
  modify ID_USER INT NOT NULL,
  modify ID_ADVENTURE INT NOT NULL,
  add PRIMARY KEY (ID_GAME),
  add INDEX fk_character_game_idx (ID_CHARACTER),
  add INDEX fk_user_game_idx (ID_USER),
  add INDEX fk_adventure_game_idx (ID_ADVENTURE),
  add CONSTRAINT fk_character_game FOREIGN KEY (ID_CHARACTER) REFERENCES project.`CHARACTER` (ID_CHARACTER),
  add CONSTRAINT fk_user_game FOREIGN KEY (ID_USER) REFERENCES project.`USER` (ID_USER),
  add CONSTRAINT fk_adventure_game FOREIGN KEY (ID_ADVENTURE) REFERENCES project.ADVENTURE (ID_ADVENTURE);
  
alter table STEP
	modify ID_STEP INT NOT NULL AUTO_INCREMENT,
  modify `description` VARCHAR(500) NOT NULL,
  modify the_end BIT NOT NULL,
  modify `start` BIT NOT NULL,
  modify user_creation VARCHAR(45) NOT NULL,
  modify date_creation DATETIME NOT NULL,
  modify date_mod DATETIME NULL,
  modify user_mod VARCHAR(45) NULL,
  modify ID_ADVENTURE INT NOT NULL,
  add PRIMARY KEY (ID_STEP),
  add INDEX fk_adventure_step_idx (ID_ADVENTURE),
  add CONSTRAINT fk_adventure_step FOREIGN KEY (ID_ADVENTURE) REFERENCES project.ADVENTURE (ID_ADVENTURE);
  
alter table `OPTION`
	modify ID_OPTION INT NOT NULL AUTO_INCREMENT,
  modify `description` VARCHAR(500) NOT NULL,
  modify answer VARCHAR(1000) NOT NULL,
  modify user_creation VARCHAR(45) NOT NULL,
  modify date_creation DATETIME NOT NULL,
  modify date_mod DATETIME NULL,
  modify user_mod VARCHAR(45) NULL,
  modify ID_STEP_FROM INT NOT NULL,
  modify ID_STEP_TO INT NOT NULL,
  add PRIMARY KEY (ID_OPTION),
  add INDEX fk_OPTION_STEP1_idx (ID_STEP_FROM),
  add INDEX fk_OPTION_STEP2_idx (ID_STEP_TO),
  add CONSTRAINT fk_OPTION_STEP1 FOREIGN KEY (ID_STEP_FROM) REFERENCES project.STEP (ID_STEP),
  add CONSTRAINT fk_OPTION_STEP2 FOREIGN KEY (ID_STEP_TO) REFERENCES project.STEP (ID_STEP);
  
alter table RECORD
	modify user_creation VARCHAR(45) NOT NULL,
  modify date_creation DATETIME NOT NULL,
  modify date_mod DATETIME NULL,
  modify user_mod VARCHAR(45) NULL,
  modify ID_GAME INT NOT NULL,
  modify ID_STEP INT NOT NULL,
  modify ID_OPTION INT NOT NULL,
  add PRIMARY KEY (ID_GAME, ID_STEP, ID_OPTION),
  add INDEX fk_RECORD_STEP1_idx (ID_STEP),
  add INDEX fk_RECORD_OPTION1_idx (ID_OPTION),
  add CONSTRAINT fk_RECORD_GAME FOREIGN KEY (ID_GAME) REFERENCES project.GAME (ID_GAME),
  add CONSTRAINT fk_RECORD_STEP FOREIGN KEY (ID_STEP) REFERENCES project.STEP (ID_STEP),
  add CONSTRAINT fk_RECORD_OPTION1 FOREIGN KEY (ID_OPTION) REFERENCES project.`OPTION` (ID_OPTION);
  
alter table STARS
	modify ID_ADVENTURE INT NOT NULL,
  modify ID_CHARACTER INT NOT NULL,
  add PRIMARY KEY (ID_ADVENTURE, ID_CHARACTER),
  add INDEX fk_ADVENTURE_has_CHARACTER_CHARACTER1_idx (ID_CHARACTER),
  add INDEX fk_ADVENTURE_has_CHARACTER_ADVENTURE1_idx (ID_ADVENTURE),
  add CONSTRAINT fk_adventure_stars FOREIGN KEY (ID_ADVENTURE) REFERENCES project.ADVENTURE (ID_ADVENTURE),
  add CONSTRAINT fk_character_stars FOREIGN KEY (ID_CHARACTER) REFERENCES project.`CHARACTER` (ID_CHARACTER);