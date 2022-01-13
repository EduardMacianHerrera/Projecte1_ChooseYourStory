use project;

delete from `OPTION`;
delete from STEP;
delete from ADVENTURE;
delete from `CHARACTER`;
delete from STARS;


# Inserts CHARACTERS

INSERT INTO `CHARACTER`(character_name, description, user_creation, date_creation) VALUES 
('Vegeta','Príncipe de una raza guerrera extraterrestre conocida como los Saiyajin.', user(), now()),
('Itachi','Ninja renegado considerado un prodigio y portador de numerosas cualidades sobresalientes', user(), now()),
('Zoro','Espadachín experto en el Santōryū (estilo de tres espadas) Valiente, fuerte y bastante temperamental', user(), now()),
('Jack Sparrow','Legendario pirata de Todos los Mares y un irreverente embaucador del Caribe.', user(), now());

# Inserts ADVENTURE

insert into ADVENTURE(adventure_name,description,user_creation,date_creation) values 
# Historia 1
("En busca de la gráfica perdida","Busca el tesoro oculto, disfruta de una aventura a través de las mazmorras Morgul. Encuentra, enfrenta y supera cada desafío que te encuentres por el camino hasta descubrir que final es el que te espera.",user(),now()),
#Historia 2
("Un examen desastroso","Te despiertas un día de examen, no te ha sonado la alarma. Decide que vas a hacer, pero cuidado con las decisiones que tomas, toda acción tiene su consecuencia ya sea para bien o para mal.",user(),now()),
#Historia 3
("Póker interdimensional","Juega una o varias partidas de poker interdimensional. Recuerda que no todo depende de la mano que te toque sino de como juegues tus cartas. A veces retirarse a tiempo es una victoria (o no).",user(),now());

# Inserts STEP
insert into STARS(ID_ADVENTURE,ID_CHARACTER) values 
((select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida"),(select ID_CHARACTER from `CHARACTER` where character_name = "Jack Sparrow")),
((select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso"),(select ID_CHARACTER from `CHARACTER` where character_name = "Zoro")),
((select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso"),(select ID_CHARACTER from `CHARACTER` where character_name = "Itachi")),
((select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso"),(select ID_CHARACTER from `CHARACTER` where character_name = "Jack Sparrow")),
((select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional"),(select ID_CHARACTER from `CHARACTER` where character_name = "Vegeta")),
((select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional"),(select ID_CHARACTER from `CHARACTER` where character_name = "Zoro")),
((select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional"),(select ID_CHARACTER from `CHARACTER` where character_name = "Itachi")),
((select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional"),(select ID_CHARACTER from `CHARACTER` where character_name = "Jack Sparrow"))
;

# Inserts STEP

insert into STEP(description,the_end,start,user_creation,date_creation,ID_ADVENTURE) values 
# Historia 1
# Primer Paso
("Estás en una misión dentro de unas mazmorras con el fin de conseguir el gran tesoro; Una RTX3090 Ti. Te encuentras un arsenal lleno de armas de todo tipo, que escoges?", 0,1,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
# Pasos intermedios
("Que haces?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
#Final 1
("Le caes bien, os haceis amigos y buscais la grafica juntos. Finalmente la acabas vendiendo por esteroides y te vuelves culturista. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida"));

# Insert OPTION

insert into `OPTION`(description,answer,user_creation,date_creation,ID_STEP_FROM,ID_STEP_TO) values
("Armas de fuego","Aparece Joseph Joestar",user(),now(),(
	select ID_STEP from STEP where description = 
    "Estás en una misión dentro de unas mazmorras con el fin de conseguir el gran tesoro; Una RTX3090 Ti. Te encuentras un arsenal lleno de armas de todo tipo, que escoges?"),(
    select ID_STEP from STEP where description = 
    "Que haces?")),
("Te pones a hacer Jojo poses con él.","",user(),now(),(
	select ID_STEP from STEP where description = 
    "Que haces?"),(
    select ID_STEP from STEP where description = 
    "Le caes bien, os haceis amigos y buscais la grafica juntos. Finalmente la acabas vendiendo por esteroides y te vuelves culturista. FIN"));
 