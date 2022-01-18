use project;


delete from RECORD;
delete from `OPTION`;
delete from STEP;
delete from STARS;
delete from GAME;
delete from ADVENTURE;
delete from `CHARACTER`;



# Inserts CHARACTERS

INSERT INTO `CHARACTER`(character_name, description, user_creation, date_creation) VALUES 
('Vegeta','Príncipe de una raza guerrera extraterrestre conocida como los Saiyajin.', user(), now()),
('Itachi','Ninja renegado considerado un prodigio y portador de numerosas cualidades sobresalientes', user(), now()),
('Zoro','Espadachín experto en el Santōryū (estilo de tres espadas) Valiente, fuerte y bastante temperamental', user(), now()),
('Jack Sparrow','Legendario pirata de Todos los Mares y un irreverente embaucador del Caribe.', user(), now());

# Inserts ADVENTURE

insert into ADVENTURE(adventure_name,description,user_creation,date_creation) values 
# En busca de la gráfica perdida
("En busca de la gráfica perdida","Busca el tesoro oculto, disfruta de una aventura a través de las mazmorras Morgul. Encuentra, enfrenta y supera cada desafío que te encuentres por el camino hasta descubrir que final es el que te espera.",user(),now()),
# Un examen desastroso
("Un examen desastroso","Te despiertas un día de examen, no te ha sonado la alarma. Decide que vas a hacer, pero cuidado con las decisiones que tomas, toda acción tiene su consecuencia ya sea para bien o para mal.",user(),now()),
# Póker interdimensional
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
# Irene 
# En busca de la gráfica perdida
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
("Sukuna vence a Akaza, consigue la grafica, pero antes de acabar los 2 minutos la vende por ebay y se transfiere el dinero a su monedero de bitcoins. Te has quedado sin la grafica y sin saber como salir de las mazmorras. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida")),

# Albert
# Póker interdimensional
("Necesitas dinero para comprar  RAM, ya que actualmente tu ordenador no puede correr dos maquinas virtuales simulataneamente y lo necesitas para un trabajo. Decides ir a jugar a Poker a la cantina interdimensional para conseguir dinero rapido. Llegas a la cantina y la unica mesa a la que te puedes unir es una que van a empezar Shrek, Tobey Maguire, mister Bean, Hermione Granger y un Loro Pirata entrenado. Decides unirte. Hay dos sillas libres, ¿Donde te sientas?", 
0,1,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")), 

("¿Quieres jugar?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Tu siguiente movimiento?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Doblas?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Igualas?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Continuas?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Que harás?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Que haces?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Quieres volver a jugar?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Te unes a el?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Otra partida?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("¿Te apuntas?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("Se hace la apuesta inicial, cada uno apuesta una ficha. Se reparten las dos cartas por jugador, te tocan el 3 de picas y la J de diamante ¿Quieres volver a jugar?", 0,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),



#FINAL
("Sales de la cantina tras decir que necesitas ir a descansar a casa. Antes pasas por el cajero automatico para entrar los billetes en tu cuenta y hacer la compra online. El cajero no los lee porque estan mojados, al final no podras usar ese dinero para comprar la RAM. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("Vuelves a perder, esta vez gana Hermione, que no se ha vuelto a dejar engañar por un pajarraco charlatán. Te retiras, no has logrado ganar dinero y ya buscaras otra forma. Abandonas la cantina. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),

("Abandonas la cantina. FIN", 1,0,user(),now(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "Póker interdimensional")),


# Sergio
# Un examen desastroso
#Primer paso
("Te despiertas un día cualquiera para ir al colegio, miras la hora y ves que no te ha sonado el despertador. Sabes que llegas tarde y tienes un examen de programación. Está lloviendo. ¿Que haces?", 0, 1, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
#Pasos intermedios
("Tu cuerpo rebosa adrenalina, ¿que haces?", 0, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
("¿Que le dices?",0,0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
("Estás triste por haber suspendido. ¿Que haces?", 0,0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
("Hay mucho dinero. ¿Que haces?", 0, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
("Es hora de volver a casa, que haces?", 0, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
("Piensa bien. ¿Que haces?", 0, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
("Tienes que llamar a alguien para que te venga a buscar, a quien?", 0, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
#Final 1
("Al llegar a clase, haces el examen, lo apruebas pero te empiezas a encontrar mal. Los profesores llaman a una ambulancia, te llevan al hospital y te dicen que si hubieras ido en el momento del accidente estarías mejor. Te habías fisurado la clavícula pero al levantar la moto se ha hecho más grande la fisura y ahora te tienen que operar. Por lo que vas a faltar un mínimo de 2 meses al colegio, los cuales no podrás hacer exámenes.", 1, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
#Final 2
("El propietario es un multimillonario que para agradecerte el buen gesto te ingresa 11 millones de euros en tu cuenta bancaria. Tu vives feliz por no tener que volver a trabajar y te olvidas del suspenso.", 1, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
#Final 3
("Un vecino al que no le caes bien pasaba por allí, te vió guardartela y se lo dijo a la policía. Te detienen y te toca ir a juicio, pierdes el caso y acabas teniendo una deuda que no te va a permitir seguir estudiando.", 1, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
#Final 4
("Al día siguiente te espiertas y llegas a tiempo al siguiente examen, los apruebas y al menos estás felix, aunque hueles mal y te duele la espalda.", 1, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso")),
#Final 5
("Te lleva a casa pero te cobra 70 euros. Tu te das cuenta del horrible día que has tenido y que hubiera salido más a cuenta quedarte en casa.", 1, 0, user(), now(), (select ID_ADVENTURE from ADVENTURE where adventure_name = "Un examen desastroso"));

# Insert OPTION

insert into `OPTION`(description,answer,user_creation,date_creation,ID_STEP_FROM,ID_STEP_TO) values
# Irene
# En busca de la gráfica perdida
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
    "Que haces?")),
    
# Albert
# Póker interdimensional
(
"Al lado de Tobey Maguire, el Spiderman de tu infancia",
"Se hace la apuesta incial, cada uno apuesta una ficha. Se reparten las dos cartas por jugador, te tocan el 2 de corazones y el 5 de picas.",
user(),
now(),
(select ID_STEP from STEP where description = 
"Necesitas dinero para comprar  RAM, ya que actualmente tu ordenador no puede correr dos maquinas virtuales simulataneamente y lo necesitas para un trabajo. Decides ir a jugar a Poker a la cantina interdimensional para conseguir dinero rapido. Llegas a la cantina y la unica mesa a la que te puedes unir es una que van a empezar Shrek, Tobey Maguire, mister Bean, Hermione Granger y un Loro Pirata entrenado. Decides unirte. Hay dos sillas libres, ¿Donde te sientas?"), #ok
(select ID_STEP from STEP where description = 
	"¿Quieres jugar?")
),

(
"Si",
"Tobey Maguire se retira. Se colocan las 3 cartas visibles sobre la mesa. Son el 4 de diamante, el 5 de corazones y la k de diamante.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Quieres jugar?"),
(select ID_STEP from STEP where description = 
    "¿Tu siguiente movimiento?"))
,

(
"Continuas y duplicas la apuesta",
"Hermione se retira. El resto igualan tu apuesta y continua el juego. Se revela otra carta, el as de diamante",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Tu siguiente movimiento?"),
(select ID_STEP from STEP where description = 
    "¿Doblas?"))
,

(
"¡Si!",
"Ultima carta! Es el 2 de diamante. Mr Bean sube mucho la apuesta. Shrek se retira. El loro iguala la apuesta dispuesto a todo.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Doblas?"),
(select ID_STEP from STEP where description = 
    "¿Igualas?"))
,

(
"Si",
"",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Igualas?"),
(select ID_STEP from STEP where description = 
    "Abandonas la cantina. FIN")
)
,

(
"No",
"Te retiras y esperas a la siguiente partida. Mr Bean gana la partida con doble pareja de 4 y de 2.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Quieres jugar?"),
(select ID_STEP from STEP where description = 
    "Se hace la apuesta inicial, cada uno apuesta una ficha. Se reparten las dos cartas por jugador, te tocan el 3 de picas y la J de diamante ¿Quieres volver a jugar?")
)
,

(
"Continuas e igualas la apuesta",
"Hermione se retira. Se revela otra carta, el as de diamante",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Tu siguiente movimiento?"),
(select ID_STEP from STEP where description = 
    "¿Doblas?")
)
,

(
"No, solo igualas la apuesta",
"Ultima carta! Es el 2 de diamante. Nadie sube la apuesta",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Doblas?"),
(select ID_STEP from STEP where description = 
    "¿Continuas?")
)
,

(
"Si",
"Mr Bean revela sus cartas, el 2 de diamantes y el 4 de treboles, tiene doble pareja, al igual que tu. El loro revela sus cartas, pareja de K. Has ganado, pero aun no tienes suficiente dinero.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Continuas?"),
(select ID_STEP from STEP where description = 
    "¿Que harás?")
)
,

(
"Dejar de jugar, ya buscarás alguna forma de hacer la práctica de las MVs",
"resultado",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Que harás?"),
(select ID_STEP from STEP where description = 
    "Abandonas la cantina. FIN")
)
,

(
"Te retiras",
"Te retiras y esperas a la siguiente partida. Mr Bean gana la partida con doble pareja de 4 y de 2.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Tu siguiente movimiento?"),
(select ID_STEP from STEP where description = 
    "Se hace la apuesta inicial, cada uno apuesta una ficha. Se reparten las dos cartas por jugador, te tocan el 3 de picas y la J de diamante ¿Quieres volver a jugar?")
)
,

(
"No, te retiras",
"Te retiras y esperas a la siguiente partida. Mr Bean gana la partida con doble pareja de 4 y de 2.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Igualas?"),
(select ID_STEP from STEP where description = 
    "Se hace la apuesta inicial, cada uno apuesta una ficha. Se reparten las dos cartas por jugador, te tocan el 3 de picas y la J de diamante ¿Quieres volver a jugar?")
)
,

(
"No",
"Te retiras y esperas a la siguiente partida. Mr Bean gana la partida con doble pareja de 4 y de 2.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Continuas?"),
(select ID_STEP from STEP where description = 
    "Se hace la apuesta inicial, cada uno apuesta una ficha. Se reparten las dos cartas por jugador, te tocan el 3 de picas y la J de diamante ¿Quieres volver a jugar?")
)
,

(
"Apuntarte a un concurso que consiste en ver quien aguanta mas bebiendo cerveza con premio en dinero",
"El concurso trata de beber Cruzcampo. Terminas bastante afectado y te duermes sentado en la taza del vater (Has tenido que ir varias veces y es obvio no ganarás). Te despiertas  con una fuerte voz que resuena por toda la cantina y tu craneo. Es Shrek, quien ha ganado el concurso y, ligeramente ebrio, lo celebra cantando All Star (Somebody once told me...) Te levantas algo aturdido, te apoyas un momento en la pared de la izquierda y ves en el suelo una cartera que alguien se ha dejado, esta sucia y mojada, pero ves que dentro hay un par de billetes.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Que harás?"),
(select ID_STEP from STEP where description = 
    "¿Que haces?")
)
,

(
"Coger el dinero",
"",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Que haces?"),
(select ID_STEP from STEP where description = 
    "Sales de la cantina tras decir que necesitas ir a descansar a casa. Antes pasas por el cajero automatico para entrar los billetes en tu cuenta y hacer la compra online. El cajero no los lee porque estan mojados, al final no podras usar ese dinero para comprar la RAM. FIN")
)
,

(
"Decides no coger nada, y entregar la cartera al dueño de la cantina",
"resultado",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Que haces?"),
(select ID_STEP from STEP where description = 
    "Abandonas la cantina. FIN")
)
,

(
"No",
"Te retiras y ves el resto de la partida. Tobey Maguire gana la partida con una pareja de Q. Lo celebra con sus bailes caracteristicos, que nos traen gratos recuerdos de Spiderman III",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Quieres volver a jugar?"),
(select ID_STEP from STEP where description = 
    "¿Te unes a el?")
)
,

(
"No, has venido aqui a por dinero, asi que te apuntas al concurso de beber cerveza para aspirar el premio",
"El concurso trata de beber Cruzcampo. Terminas bastante afectado y te duermes sentado en la taza del vater (Has tenido que ir varias veces y es obvio no ganarás). Te despiertas  con una fuerte voz que resuena por toda la cantina y tu craneo. Es Shrek, quien ha ganado el concurso y, ligeramente ebrio, lo celebra cantando All Star (Somebody once told me...) Te levantas algo aturdido, te apoyas un momento en la pared de la izquierda y ves en el suelo una cartera que alguien se ha dejado, esta sucia y mojada, pero ves que dentro hay un par de billetes.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Te unes a el?"),
(select ID_STEP from STEP where description = 
    "¿Que haces?")
)
,

(
"Si, pasas el resto de la noche bailando con Tobey y renunciando a la poca dignidad que te queda. Tampoco consigues ligarte a nadie.",
"",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Te unes a el?"),
(select ID_STEP from STEP where description = 
    "Abandonas la cantina. FIN")
)
,

(
"Si",
"Pierdes la partida, el Loro gana con una pareja de 10, gracias a su tactica de ir subiendo la apuesta y ahuyentar a los otros jugadores.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Quieres volver a jugar?"),
(select ID_STEP from STEP where description = 
    "¿Otra partida?")
)
,

(
"No",
"Ves que hay un concurso de beber cerveza con un premio en dinero interesante.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Otra partida?"),
(select ID_STEP from STEP where description = 
    "¿Te apuntas?")
)
,

(
"Si",
"El concurso trata de beber Cruzcampo. Terminas bastante afectado y te duermes sentado en la taza del vater (Has tenido que ir varias veces y es obvio no ganarás). Te despiertas  con una fuerte voz que resuena por toda la cantina y tu craneo. Es Shrek, quien ha ganado el concurso y, ligeramente ebrio, lo celebra cantando All Star (Somebody once told me...) Te levantas algo aturdido, te apoyas un momento en la pared de la izquierda y ves en el suelo una cartera que alguien se ha dejado, esta sucia y mojada, pero ves que dentro hay un par de billetes.",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Te apuntas?"),
(select ID_STEP from STEP where description = 
    "¿Que haces?")
)
,

(
"No",
"resultado",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Te apuntas?"),
(select ID_STEP from STEP where description = 
    "Abandonas la cantina. FIN")
)
,

(
"Si",
"",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Otra partida?"),
(select ID_STEP from STEP where description = 
    "Vuelves a perder, esta vez gana Hermione, que no se ha vuelto a dejar engañar por un pajarraco charlatán. Te retiras, no has logrado ganar dinero y ya buscaras otra forma. Abandonas la cantina. FIN")
)
,

(
"Jugar otra partida de poker en la mesa",
"Se hace la apuesta inicial, cada uno apuesta una ficha. Se reparten las dos cartas por jugador, te tocan el 3 de picas y la J de diamante",
user(),
now(),
(select ID_STEP from STEP where description = 
    "¿Que harás?"),
(select ID_STEP from STEP where description = 
    "¿Quieres volver a jugar?")
)
,

(
"Al lado de Mister Bean, crees que te dara suerte",
"Se hace la apuesta inicial, cada uno apuesta una ficha. Se reparten las dos cartas por jugador, te tocan el 3 de picas y la J de diamante",
user(),
now(),
(select ID_STEP from STEP where description = 
    "Necesitas dinero para comprar  RAM, ya que actualmente tu ordenador no puede correr dos maquinas virtuales simulataneamente y lo necesitas para un trabajo. Decides ir a jugar a Poker a la cantina interdimensional para conseguir dinero rapido. Llegas a la cantina y la unica mesa a la que te puedes unir es una que van a empezar Shrek, Tobey Maguire, mister Bean, Hermione Granger y un Loro Pirata entrenado. Decides unirte. Hay dos sillas libres, ¿Donde te sientas?"),
(select ID_STEP from STEP where description = 
    "¿Quieres volver a jugar?")
),
# Sergio
# Un examen desastroso
("Coges la moto.", "Tienes un accidente por culpa de la lluvia", user(), now(), (select ID_STEP from STEP where description = "Te despiertas un día cualquiera para ir al colegio, miras la hora y ves que no te ha sonado el despertador. Sabes que llegas tarde y tienes un examen de programación. Está lloviendo. ¿Que haces?"), (select ID_STEP from STEP where description = "Tu cuerpo rebosa adrenalina, ¿que haces?")),
("Coges el coche.", "Te pasas dos horas en la carretera por culpa de la caravana, llegas tarde al examen, pero seco. El/la profesor/a de programación te pregunta que ha pasado.", user(), now(), (select ID_STEP from STEP where description = "Te despiertas un día cualquiera para ir al colegio, miras la hora y ves que no te ha sonado el despertador. Sabes que llegas tarde y tienes un examen de programación. Está lloviendo. ¿Que haces?"), (select ID_STEP from STEP where description = "¿Que le dices?")),
("Te levantas, levantas la moto y sigues tu camino.","", user(), now(), (select ID_STEP from STEP where description = "Tu cuerpo rebosa adrenalina, ¿que haces?"), (select ID_STEP from STEP where description = "Al llegar a clase, haces el examen, lo apruebas pero te empiezas a encontrar mal. Los profesores llaman a una ambulancia, te llevan al hospital y te dicen que si hubieras ido en el momento del accidente estarías mejor. Te habías fisurado la clavícula pero al levantar la moto se ha hecho más grande la fisura y ahora te tienen que operar. Por lo que vas a faltar un mínimo de 2 meses al colegio, los cuales no podrás hacer exámenes.")),
("Pides que llamen una ambulancia.", "Te llevan al hospital y descubren que te has fisurado la clavícula. Le mandas un mensaje al/la profesor/a explicandole la situación y te dice que podrás hacer el examen más adelante. Pasan unos días y lo haces. De todos modos suspendes el examen.", user(), now(), (select ID_STEP from STEP where description = "Tu cuerpo rebosa adrenalina, ¿que haces?"), (select ID_STEP from STEP where description = "Estás triste por haber suspendido. ¿Que haces?")),
("Le cuentas la verdad", "Te dice que no puedes hacer el examen. Por lo tanto suspendes el examen", user(), now(), (select ID_STEP from STEP where description = "¿Que le dices?"), (select ID_STEP from STEP where description = "Estás triste por haber suspendido. ¿Que haces?")),
("Le dices que pensabas que el examen era otro día.", "Sorprendentemente te deja pasar y hacer el examen. Tienes 1:30h menos que el resto. De igual forma suspendes el examen.", user(), now(), (select ID_STEP from STEP where description = "¿Que le dices?"), (select ID_STEP from STEP where description = "Estás triste por haber suspendido. ¿Que haces?")),
("Te vas a llorar las penas con una cerveza.", "A la hora salen tus compañeros diciendo que les ha ido fatal, se te unen y cabais borrachos.", user(), now(), (select ID_STEP from STEP where description = "Estás triste por haber suspendido. ¿Que haces?"), (select ID_STEP from STEP where description = "Es hora de volver a casa, que haces?")),
("Te vas a casa.", "Al aparecer el coche te encuentras una cartera, la abres y encuentras 10.000 euros", user(), now(), (select ID_STEP from STEP where description = "Estás triste por haber suspendido. ¿Que haces?"), (select ID_STEP from STEP where description = "Hay mucho dinero. ¿Que haces?")),
("Decides mirar la dirección del propietario y se la llevas.", "", user(), now(), (select ID_STEP from STEP where description ="Hay mucho dinero. ¿Que haces?"), (select ID_STEP from STEP where description = "El propietario es un multimillonario que para agradecerte el buen gesto te ingresa 11 millones de euros en tu cuenta bancaria. Tu vives feliz por no tener que volver a trabajar y te olvidas del suspenso.")),
("Te la quedas.", "", user(), now(), (select ID_STEP from STEP where description = "Hay mucho dinero. ¿Que haces?"), (select ID_STEP from STEP where description = "Un vecino al que no le caes bien pasaba por allí, te vió guardartela y se lo dijo a la policía. Te detienen y te toca ir a juicio, pierdes el caso y acabas teniendo una deuda que no te va a permitir seguir estudiando.")),
("Coges el coche", "Te encuentras con un control de alcholemia, te paran, das positivo, te multan y te dicen que el coche se queda aquí", user(), now(), (select ID_STEP from STEP where description = "Es hora de volver a casa, que haces?"), (select ID_STEP from STEP where description = "Tienes que llamar a alguien para que te venga a buscar, a quien?")),
("Te esperas a que se te pase", "Te esperas dos horas jugando al Clash Royale. Finalmente entras en el coche.",user(), now(), (select ID_STEP from STEP where description = "Es hora de volver a casa, que haces?"), (select ID_STEP from STEP where description = "Piensa bien. ¿Que haces?")),
("Te vas a casa", "Al aparecer el coche te encuentras una cartera, la abres y encuentras 10.000 euros", user(), now(), (select ID_STEP from STEP where description = "Piensa bien. ¿Que haces?"), (select ID_STEP from STEP where description = "Hay mucho dinero. ¿Que haces?")),
("Te quedas durmiendo en el coche, no te fias de que puedan pararte", "", user(), now(), (select ID_STEP from STEP where description = "Piensa bien. ¿Que haces?"), (select ID_STEP from STEP where description = "Al día siguiente te espiertas y llegas a tiempo al siguiente examen, los apruebas y al menos estás felix, aunque hueles mal y te duele la espalda.")),
("Llamas a un amigo", "No te coge así que toca coger un taxi", user(), now(), (select ID_STEP from STEP where description = "Tienes que llamar a alguien para que te venga a buscar, a quien?"), (select ID_STEP from STEP where description = "Te lleva a casa pero te cobra 70 euros. Tu te das cuenta del horrible día que has tenido y que hubiera salido más a cuenta quedarte en casa.")),
("Llamas a un taxi", "", user(), now(), (select ID_STEP from STEP where description = "Tienes que llamar a alguien para que te venga a buscar, a quien?"), (select ID_STEP from STEP where description = "Te lleva a casa pero te cobra 70 euros. Tu te das cuenta del horrible día que has tenido y que hubiera salido más a cuenta quedarte en casa."));