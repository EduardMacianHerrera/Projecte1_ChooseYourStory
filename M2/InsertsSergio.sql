use project;


# Inserts STEP
insert into STEP(description,the_end,start,user_creation,date_creation,ID_ADVENTURE) values
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
("Te esperas a que se te pase", "Te esperas dos horas jugando al Clash Royale. Finalmente entras en el coche.", user(), now(), (select ID_STEP from STEP where description = "Es hora de volver a casa, que haces?"), (select ID_STEP from STEP where description = "Piensa bien. ¿Que haces?")),
("Te vas a casa", "Al aparecer el coche te encuentras una cartera, la abres y encuentras 10.000 euros", user(), now(), (select ID_STEP from STEP where description = "Piensa bien. ¿Que haces?"), (select ID_STEP from STEP where description = "Hay mucho dinero. ¿Que haces?")),
("Te quedas durmiendo en el coche, no te fias de que puedan pararte", "", user(), now(), (select ID_STEP from STEP where description = "Piensa bien. ¿Que haces?"), (select ID_STEP from STEP where description = "Al día siguiente te espiertas y llegas a tiempo al siguiente examen, los apruebas y al menos estás felix, aunque hueles mal y te duele la espalda.")),
("Llamas a un amigo", "No te coge así que toca coger un taxi", user(), now(), (select ID_STEP from STEP where description = "Tienes que llamar a alguien para que te venga a buscar, a quien?"), (select ID_STEP from STEP where description = "Te lleva a casa pero te cobra 70 euros. Tu te das cuenta del horrible día que has tenido y que hubiera salido más a cuenta quedarte en casa.")),
("Llamas a un taxi", "", user(), now(), (select ID_STEP from STEP where description = "Tienes que llamar a alguien para que te venga a buscar, a quien?"), (select ID_STEP from STEP where description = "Te lleva a casa pero te cobra 70 euros. Tu te das cuenta del horrible día que has tenido y que hubiera salido más a cuenta quedarte en casa."));


