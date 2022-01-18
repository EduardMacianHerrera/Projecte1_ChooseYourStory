use project;

# Inserts ADVENTURE
delete from ADVENTURE;

insert into ADVENTURE(adventure_name,description,user_creation,date_creation,date_mod,user_mod) values 
# Historia 1
("En busca de la gráfica perdida","Busca el tesoro oculto, disfruta de una aventura a través de las mazmorras Morgul. Encuentra, enfrenta y supera cada desafío que te encuentres por el camino hasta descubrir que final es el que te espera.",user(),now(),now(),user()),
#Historia 2
("Un examen desastroso","Te despiertas un día de examen, no te ha sonado la alarma. Decide que vas a hacer, pero cuidado con las decisiones que tomas, toda acción tiene su consecuencia ya sea para bien o para mal.",user(),now(),now(),user()),
#Historia 3
("Póker interdimensional","Juega una o varias partidas de poker interdimensional. Recuerda que no todo depende de la mano que te toque sino de como juegues tus cartas. A veces retirarse a tiempo es una victoria (o no).",user(),now(),now(),user());

# Inserts STEP
delete from STEP;

insert into STEP(description,the_end,start,user_creation,date_creation,date_mod,user_mod,FK_ID_ADVENTURE) values 
# Historia 1
# Primer Paso
("Estás en una misión dentro de unas mazmorras con el fin de conseguir el gran tesoro; Una RTX3090. Te encuentras un arsenal lleno de armas de todo tipo, que escoges?", 0,1,user(),now(),now(),user(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
 
("Aparece Joseph Joestar, que haces?", 0,0,user(),now(),now(),user(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
#Final 1
("Le caes bien, os haceis amigos y buscais la grafica juntos. Finalmente la acabas vendiendo por esteroides y te vuelves culturista. FIN", 1,0,user(),now(),now(),user(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida"));

