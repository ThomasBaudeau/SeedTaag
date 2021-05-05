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

<strong> <em> create_sbml (str -> ) </em></strong> <br>
construit un objet libSBML à partir d'un fichier SBML <br>
kind: global function <br>
parameters: file de type str <br>
description : nom du fichier sbml à lire <br>
return: libsbml objet: objet qui contient toutes les informations du fichier <br>

<strong> <em> extract_species (str -> ) </em></strong> <br>
extraire des informations sur les espèces dans un modèle libSBML <br>
Kind: global function <br>
parameters:  <br> 
description: créer un dictionnaire d'objet Metabo à partir d'un objet libsbml <br>
return :  dictionnaire contenant tous les métabolites de l'objet libsbml sous forme d'objets métabolites <br>
   

<strong> <em> extract_reactions (str -> ) </em></strong> <br>
extraire des informations sur les réactions dans un modèle libSBML <br>
kind : global function <br>
parameters: <br>
    Args :
        model (libsbml object) : objet qui contient toutes les informations contenues dans le fichier sbml   
        Metabos (dictionnaire d'objets metabo) : dictionnaire contenant les métabolites en tant qu'objets métabolites
    Raises :
        ValueError : attrape une exception si la liste des réactifs ou des produits ne peut pas être créée correctement.
    Retourne :
        dict : dictionnaire contenant toutes les réactions de l'objet libsbml sous forme d'objets de réaction.




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
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

 <strong><em> all_pairs_nodes_connectivity () </em></strong>  <br>
renvoie dictionary with nodes connectivity between all pairs of nodes in G <br>
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

 <strong><em> degree () </em></strong>  <br> 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

 <strong><em> diameter () </em></strong>  <br> 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

  <strong><em> tarjan () </em></strong>  <br>  
 renvoie une liste des composants strictement convexes du graphe 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

 <strong><em> all_tp ()  </em></strong>  <br> 
renvoie tous les tris topologiques du graphe possibles 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

 <strong><em> taagseed ()  </em></strong>  <br> 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>


<strong><em> display_all () </em></strong>  <br>  
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

 <strong><em>  display_shortest_path ()  </em></strong>  <br>
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em> display_centrality ()  </em></strong>  <br> 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em>  display_connectivity ()   </em></strong>  <br>
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em>  display_degree ()  </em></strong>  <br> 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em>  display_diameter ()  </em></strong>  <br> 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em> display_seed ()  </em></strong>  <br> 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br> 

<strong><em>  save_shortest_path ()  </em></strong>  <br> 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em>  save_centrality ()  </em></strong>  <br>
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em>  save_connectivity ()   </em></strong>  <br>
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em>  save_degree ()   </em></strong>  <br>s
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br> 

<strong><em>  save_seed ()  </em></strong>  <br> 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em>  find_seed ()  </em></strong>  <br>
	find seed element in a directed acyclic graph
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br> 

<strong><em>  scc_species ()  </em></strong>  <br>
	build dictionary of all the species of graph
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br> 

<strong><em>  scc_link ()  </em></strong>  <br>
	build dictionary of links between all the species 
Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>

<strong><em>  dag_init ()   </em></strong>  <br>

Kind : <br>
mode :<br>
paramereters :<br> 
description <br>
return <br>


