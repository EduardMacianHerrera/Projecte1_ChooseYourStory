use project;

delete from `OPTION`;
delete from STEP;
delete from STARS;
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

# Inserts STARS
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
("Que quieres hacer?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
("Lo ayudas?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
("Cual escoges?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
("Piensa rápido, que haces?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
("Vuelves a estar como al principio.Que haces?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),

#Final 1
("Le caes bien, os haceis amigos y buscais la grafica juntos. Finalmente la acabas vendiendo por esteroides y te vuelves culturista. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
#Final 2
("Consigues salir de las mazmorras, llegas a casa y te poner a llorar por no haber podido encontrar la gráfica. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
#Final 3
("Goku para agradecerte tu ayuda te teletransporta a lo más profundo de las mazmorras donde se haya el tesoro. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
#Final 4
("Te encuentras a Gohan y te pega una paliza por no haber ayudado a su padre. Te tomas la judia y huyes. Finalmente encuentras el tesoro y vuelves a casa. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
#Final 5
("Te encuentras a Chi-Chi que te da una charla sobre lo que está bien y lo que está mal y te pone a estudiar. Gracias a ella apruebas M02 y M03, consigues trabajo y te la acabas comprando tu. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),
#Final 6
("Sukuna vence a Akaza, consigue la grafica, pero antes de acabar los 2 minutos la vende por ebay y se transfiere el dinero a su monedero de bitcoins. Te has quedado sin la grafica y sin saber como salir de las mazmorras. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida"));

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
    "Le caes bien, os haceis amigos y buscais la grafica juntos. Finalmente la acabas vendiendo por esteroides y te vuelves culturista. FIN")),
 ("Le apuntas con el bazoka","Utiliza su tecnica más legendaria y sale corriendo. Tu disparas de todos motos y destruyes la estancia en la que estás. Logras salir por los pelos.",user(),now(),(
	select ID_STEP from STEP where description = 
    "Que haces?"),(
    select ID_STEP from STEP where description = 
    "Que quieres hacer?")),
 ("Intentas salir de las mazmorras y volver a casa","",user(),now(),(
	select ID_STEP from STEP where description = 
	"Que quieres hacer?"),(
	select ID_STEP from STEP where description = 
	"Consigues salir de las mazmorras, llegas a casa y te poner a llorar por no haber podido encontrar la gráfica. FIN")),
 ("Continuas tu busqueda","Te encuentras a Goku maleherido por una pelea reciente",user(),now(),(
	select ID_STEP from STEP where description = 
	"Que quieres hacer?"),(
	select ID_STEP from STEP where description = 
	"Lo ayudas?")),
("Paso de armas, ha puños, soy invencible.","Te encuentras a Goku maleherido por una pelea reciente",user(),now(),(
	select ID_STEP from STEP where description = 
    "Estás en una misión dentro de unas mazmorras con el fin de conseguir el gran tesoro; Una RTX3090 Ti. Te encuentras un arsenal lleno de armas de todo tipo, que escoges?"),(
    select ID_STEP from STEP where description = 
    "Lo ayudas?")),
 ("Le ayudas","",user(),now(),(
	select ID_STEP from STEP where description = 
	"Lo ayudas?"),(
	select ID_STEP from STEP where description = 
	"Goku para agradecerte tu ayuda te teletransporta a lo más profundo de las mazmorras donde se haya el tesoro. FIN")),
("Aprovechas y le robas su ultima judia magica (puede venirte bien en combate)","Te encuentras dos puertas",user(),now(),(
	select ID_STEP from STEP where description = 
	"Lo ayudas?"),(
	select ID_STEP from STEP where description = 
	"Cual escoges?")),
("A","",user(),now(),(
	select ID_STEP from STEP where description = 
	"Cual escoges?"),(
	select ID_STEP from STEP where description = 
	"Te encuentras a Gohan y te pega una paliza por no haber ayudado a su padre. Te tomas la judia y huyes. Finalmente encuentras el tesoro y vuelves a casa. FIN")),
("B","",user(),now(),(
	select ID_STEP from STEP where description = 
	"Cual escoges?"),(
	select ID_STEP from STEP where description = 
	"Te encuentras a Chi-Chi que te da una charla sobre lo que está bien y lo que está mal y te pone a estudiar. Gracias a ella apruebas M02 y M03, consigues trabajo y te la acabas comprando tu. FIN")),
("3 Katanas","Aparece Akaza, un demonio deborador de hombres que lucha con sus puños. Te acuerdas de como mató a tu amigo Rengoku y cargas contra él con toda tu rabia. Te esquiva y va a por ti.",user(),now(),(
	select ID_STEP from STEP where description = 
    "Estás en una misión dentro de unas mazmorras con el fin de conseguir el gran tesoro; Una RTX3090 Ti. Te encuentras un arsenal lleno de armas de todo tipo, que escoges?"),(
    select ID_STEP from STEP where description = 
    "Piensa rápido, que haces?")),
("Te centras en intentar cortarle los brazos, así no podrá golpearte.","Lo consigues. Le cortas los brazos pero este al ser un demonio se regenera practicamente al instante.",user(),now(),(
	select ID_STEP from STEP where description = 
    "Piensa rápido, que haces?"),(
    select ID_STEP from STEP where description = 
    "Vuelves a estar como al principio.Que haces?")),
("Intentas matarlo directamente cortandole la cabeza.","Se rompe la katana, (solo te quedan 2). Te desmayas y Sukuna tu demonio interior te lleva a su templo del mal, te ofrece cambiaros durante 2 minutos.",user(),now(),(
	select ID_STEP from STEP where description = 
    "Piensa rápido, que haces?"),(
    select ID_STEP from STEP where description = 
    "Sukuna vence a Akaza, consigue la grafica, pero antes de acabar los 2 minutos la vende por ebay y se transfiere el dinero a su monedero de bitcoins. Te has quedado sin la grafica y sin saber como salir de las mazmorras. FIN")),
("Lo vuelves a intentar.","Se rompe la katana, (solo te quedan 2). Te desmayas y Sukuna tu demonio interior te lleva a su templo del mal, te ofrece cambiaros durante 2 minutos.",user(),now(),(
	select ID_STEP from STEP where description = 
    "Vuelves a estar como al principio.Que haces?"),(
    select ID_STEP from STEP where description = 
    "Sukuna vence a Akaza, consigue la grafica, pero antes de acabar los 2 minutos la vende por ebay y se transfiere el dinero a su monedero de bitcoins. Te has quedado sin la grafica y sin saber como salir de las mazmorras. FIN")),
("Huyes","Aparece Joseph Joestar",user(),now(),(
	select ID_STEP from STEP where description = 
    "Vuelves a estar como al principio.Que haces?"),(
    select ID_STEP from STEP where description = 
    "Que haces?"));
    