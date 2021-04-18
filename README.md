*<h2>Install </h2>*

**import**




**Node server installation  set up** 




**Usage** 


**Authors**  

Students of the Bioinformatics Master of the University of Bordeaux 

Thomas BAUDEAU – thomas.baudeau@etu.u-bordeaux.fr   

Asmae BELMAHI  –  asmae.belmahi@etu.u-bordeaux.fr 

Grégory BORDIER – gregory.bordier@etu.u-bordeaux.fr 

Agathe KOMAROFF – agathe.komaroff@etu.u-bordeaux.fr 


__Programs versions used__

Google Chrome 
Firefox 


**API**   
__Table of Contents__

init_data (str → tuple) 
	à partir d'un nom de fichier. Sbml créé un modèle et renvoie les métabolites et les réactions 
kind : global funciton 
parameters : file de type str 
description : nom de fichier .sbml
return : couple composé des métabolites et des réactions 

init_graph (métabos, Reaction, mode → objet ) 
	génère le graphe à partir d'une liste de métabolites et de réactions 
kind : global function 
return ; graph networkx 
parameters : métabos de type objet
Reaction de type objet
description : liste des objets métabos
mode : affichage du graphe avec réactions et métabolites 

create_graphe () 
	built multidigraph object

extract_species () 
	extract informations of the dictionnary and built graph node 

extract_reactions () 
	extract information about reaction in model libsBML object 


shortest_path (Graph → liste) 
	renvoie une liste contenant les chemins les + courts entre les nœuds entre les différents métabolismes possibles 
Kind : fonction globale 
return : list : contenant les chemins les + courts 
parameters : Graph de type objet 
description : Graph composé des réactions et des métabolites 

degree_centrality () 
	renvoie un dictionnay of nodes with a degree centrality as a value 
c'est un degré de centralité normalisé sur le maximum de degré possible pour le graphe

betweenness_centrality() 
	renvoie un dictionnay of nodes with a betweenness centrality as a value 

all_pairs_nodes_connectivity () 
	renvoie dictionary with nodes connectivity between all pairs of nodes in G

degree () 

diameter () 

tarjan () 
 	renvoie une liste des composants strictement convexes du graphe 

all_tp () 
	renvoie tous les tris topologiques du graphe possibles 

taagseed () 



display_all () 

display_shortest_path () 

display_centrality () 

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

create_sbml ()
	build libSBML object from a SBML file

extract_species ()
	extract informations about species in model libSBML object

extract_reactions () 
	extract information about reaction in model libSBML object 


