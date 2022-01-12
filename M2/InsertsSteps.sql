use project;

# Historia 1

# Primer Paso

insert into STEP(description,the_end,start,user_creation,date_creation,date_mod,user_mod,FK_ID_ADVENTURE)
 values ("Estás en una misión dentro de unas mazmorras con el fin de conseguir el gran tesoro; Una RTX3090. Te encuentras un arsenal lleno de armas de todo tipo, que escoges?", 0,1,user(),now(),now(),user(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida"));

insert into STEP(description,the_end,start,user_creation,date_creation,date_mod,user_mod,FK_ID_ADVENTURE)
 values ("Aparece Joseph Joestar, que haces?", 0,0,user(),now(),now(),user(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida"));
 
 #Final 1
 
 insert into STEP(description,the_end,start,user_creation,date_creation,date_mod,user_mod,FK_ID_ADVENTURE)
 values ("Le caes bien, os haceis amigos y buscais la grafica juntos. Finalmente la acabas vendiendo por esteroides y te vuelves culturista. FIN", 1,0,user(),now(),now(),user(),(select ID_ADVENTURE from ADVENTURE where adventure_name = "En busca de la gráfica perdida"));