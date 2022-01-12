use project;

delete from ADVENTURE;

# Historia 1
insert into ADVENTURE(adventure_name,description,user_creation,date_creation,date_mod,user_mod)
 values ("En busca de la gráfica perdida","Busca el tesoro oculto, disfruta de una aventura a través de las mazmorras Morgul. Encuentra, enfrenta y supera cada desafío que te encuentres por el camino hasta descubrir que final es el que te espera.",user(),now(),now(),user());

# Historia 2
insert into ADVENTURE(adventure_name,description,user_creation,date_creation,date_mod,user_mod)
 values ("Un examen desastroso","Te despiertas un día de examen, no te ha sonado la alarma. Decide que vas a hacer, pero cuidado con las decisiones que tomas, toda acción tiene su consecuencia ya sea para bien o para mal.",user(),now(),now(),user());

#Historia 3
insert into ADVENTURE(adventure_name,description,user_creation,date_creation,date_mod,user_mod)
 values ("Póker interdimensional","Juega una o varias partidas de poker interdimensional. Recuerda que no todo depende de la mano que te toque sino de como juegues tus cartas. A veces retirarse a tiempo es una victoria (o no).",user(),now(),now(),user());

