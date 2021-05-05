*<h2>Install </h2>*

**import**




**Node server installation  set up** 




**Usage** 


*<h2>Authors </h2>* 

Students of the Bioinformatics Master of the University of Bordeaux 

Thomas BAUDEAU – thomas.baudeau@etu.u-bordeaux.fr   

Asmae BELMAHI  –  asmae.belmahi@etu.u-bordeaux.fr 

Grégory BORDIER – gregory.bordier@etu.u-bordeaux.fr 

Agathe KOMAROFF – agathe.komaroff@etu.u-bordeaux.fr 


*<h2>Programs versions used </h2>*

Google Chrome 87.0.4280.163 <br>
Firefox 72.0.2 <br>


*<h2>API </h2>*
__Table of Contents__

<strong> <em> create_sbml () </em></strong> <br>
build libSBML object from a SBML file <br>
kind: global function <br>
parameters: file de type str <br>
description : name of the sbml file to read <br>
return: libsbml objet <br>

</strong> <em> extract_species () </em></strong> <br>
	extract informations about species in model libSBML object

<strong> <em> extract_reactions () </em></strong> <br>
	extract information about reaction in model libSBML object 

 <strong><em>init_data (str -> tuple) </em></strong> <br>
à partir d'un nom de fichier Sbml créé un modèle et renvoie les métabolites et les réactions <br>
kind : global funciton <br>
parameters : file de type str <br>
description : nom de fichier .sbml<br>
return : couple composé des métabolites et des réactions <br>

 <strong><em>init_graph (métabos, Reaction, mode → objet ) </em></strong> <br>
génère le graphe à partir d'une liste de métabolites et de réactions  <br>
kind : global function <br>
return : graph networkx <br>
parameters : métabos de type objet<br>
Reaction de type objet<br>
description : liste des objets métabos<br>
mode : affichage du graphe avec réactions et métabolites <br>

<strong><em>create_graphe ()  </em></strong> <br>
built multidigraph object

<strong><em>extract_species ()  </em></strong> <br>
extract informations of the dictionnary and built graph node <br>

 <strong><em> extract_reactions () </em></strong> <br>
extract information about reaction in model libsBML object <br>


 <strong><em> shortest_path (Graph → liste) </em></strong> <br>
renvoie une liste contenant les chemins les + courts entre les nœuds entre les différents métabolismes possibles <br>
Kind : fonction globale <br>
return : list : contenant les chemins les + courts <br>
parameters : Graph de type objet <br>
description : Graph composé des réactions et des métabolites <br>

 <strong><em> degree_centrality () </em></strong> <br>
renvoie un dictionnay of nodes with a degree centrality as a value <br>
c'est un degré de centralité normalisé sur le maximum de degré possible pour le graphe <br>

  <strong><em> betweenness_centrality() </em></strong> <br>
renvoie un dictionnay of nodes with a betweenness centrality as a value <br>
Kind : 
mode :
paramereters : 
description 
return 

 <strong><em> all_pairs_nodes_connectivity () </em></strong>  <br>
renvoie dictionary with nodes connectivity between all pairs of nodes in G <br>
Kind : 
mode :
paramereters : 
description 
return 

 <strong><em> degree () </em></strong>  <br> 
 Kind : 
mode :
paramereters : 
description 
return 

 <strong><em> diameter () </em></strong>  <br> 
Kind : 
mode :
paramereters : 
description 
return 

  <strong><em> tarjan () </em></strong>  <br>  
 renvoie une liste des composants strictement convexes du graphe 
Kind : 
mode :
paramereters : 
description 
return 

 <strong><em> all_tp ()  </em></strong>  <br> 
renvoie tous les tris topologiques du graphe possibles 
Kind : 
mode :
paramereters : 
description 
return 

 <strong><em> taagseed ()  </em></strong>  <br> 
Kind : 
mode :
paramereters : 
description 
return 


d <strong><em> display_all () </em></strong>  <br>  
Kind : 
mode :
paramereters : 
description 
return 

 <strong><em>  display_shortest_path ()  </em></strong>  <br>
 Kind : 
mode :
paramereters : 
description 
return 

<strong><em> display_centrality ()  </em></strong>  <br> 
 Kind : 
mode :
paramereters : 
description 
return 

display_connectivity () 

display_degree () 

display_diameter () 

display_seed () 

save_all () 

save_shortest_path () 

save_centrality () 

save_connectivity () 

save_degree () 

save_seed () 

find_seed ()
	find seed element in a directed acyclic graph

scc_species ()
	build dictionary of all the species of graph

scc_link ()
	build dictionary of links between all the species 

dag_init () 




