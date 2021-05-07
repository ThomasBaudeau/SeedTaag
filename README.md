*<h2>Install </h2>*

**Installation**

Clone the repository:

<pre>
git clone https://github.com/ThomasBaudeau/SeedTaag <br> 
cd SeedTaag
</pre>

Install SeedTaag:

<pre>
sudo python3 setup.py install
</pre>


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
<strong> <em> https://thomasbaudeau.github.io/SeedTaag/python_api/index.html </em></strong>


*<h2><strong> <em> create_sbml (filename) </em></strong> <br> </h2>*

build a libSBML object from a SBML file <br>
kind: global function <br>

| Param | Type | Description |
|----------|----------|------ |
|  filename  | String	 |object who contains all the information in the file |
<br>

*<h2><strong> <em> extract_species (model) </em></strong> <br> </h2>*
extract information about species in a libSBML model <br>
kind: global function <br>
| Param | Type | Description |
|----------|----------|------ |
|  model | String	 |dictionary containing all the metabolites of the libsbml object as metabolite objects  |
<br>
 

*<h2><strong> <em> extract_reactions (model, Metabos → objet ) </em></strong> <br> </h2>*
create a reaction object dictionary from a libsml object<br>
kind : global function <br>
| Param | Type | Description |
|----------|----------|------ |
|  model | dict| libsbml object, object that contains all the information of the file |
|	Metabos| dict 	|dictionary containing all the reaction of the libsbml object as reaction objects	 |
<br>

*<h2><strong> <em> init_data (file) </em></strong> <br> </h2>*
Create two dictionaries of reaction or metabo object from an sbml file <br>
kind : global funciton <br>

| Param | Type | Description |
|----------|----------|------ |
|  file| String	 |Two dictionaries containing objects of type metabo or of type reaction|
<br>

*<h2><strong> <em> init_graph (métabos, Reaction, mode → objet ) </em></strong> <br> </h2>*
Create networkx graph with two dictionaries of metabo or of reaction or create network x graph with dict of node and edge <br>
kind : global function <br>

| Param | Type | Description |
|----------|----------|------ |
|  Metabos |dict	 |list of Métabos objects|
|Reactions	| dict	|	list of Reactions objects |
|dag| boolean	|	Select function mode |
<br>
return : graph networkx <br>
<br>

*<h2><strong> <em> _init_ (id, name, compartment, boundaryc, hosu, constant → objet ) </em></strong> <br> </h2>*
objet listing all parameters associated to metabolite  <br>
kind: global function <br> 

| Param | Type | Description |
|----------|----------|------ |
|  id| String	 |identifier of a metabolite |
|	name| String	|name of a metabolite	 |
|compartment	| String	|	name of the compartment |
|boundaryc	| boolean	| status of the boundary condition	 |
|hosu	| boolean	|	tell if has only substance unit |
|constant	| boolean	|	tell if it is constant |
<br>

*<h2><strong> <em> properties (self) </em></strong> <br> </h2>*
gives a dictionary containing all the parameters of a metabolite <br>
kind: global function <br> 

| Param | Type | Description |
|----------|----------|------ |
|  properties | dict |dictionary of parameters |
<br>

*<h2><strong> <em> get_id(self) </em></strong> <br> </h2>*
return metabolite's id <br
kind: global function <br> 

| Param | Type | Description |
|----------|----------|------ |
|  get_id | String |metabolite's id |
<br>


*<h2><strong> <em> _init_ (id, name, reversible, reactifs, products, ename → objet ) </em></strong> <br> </h2>*
object listing all parameters associated with reactions <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|  id| String	 |identifier of a metabolite |
|	name| String	|name of a metabolite	 |
|reversible	| boolean|	indicates if the reaction is reversible |
|ename	| list	| names of the enzyme	 |
|reactif	| dict	|	list of the pair of reagents identifiers and the stochiometric coefficient|
|constant	| dict	|	list of the pair of product identifiers and stochiometric coefficient |
<br>

*<h2><strong> <em> get_reactifs(self, stoichiometry=False) </em></strong> <br> </h2>*
return list of metabolite object or return dict of metabolite with stochiometry <br>
kind: global function <br> 

| Param | Type | Description |
|----------|----------|------ |
|stochiometry	| boolean|	default false define return mode with or without stochiometry |
<br>
return: metabolite object
<br>


*<h2><strong> <em> get_products(self, stoichiometry=False) </em></strong> <br> </h2>*
return list of metabolite object or return dict of metabolite with stochiometry <br>
kind: global function <br> 

| Param | Type | Description |
|----------|----------|------ |
|stochiometry	| boolean|	define return mode with or without stochiometry, defaults to `False`| 
<br>
return: metabolite object 
<br>

*<h2><strong> <em> properties(self) </em></strong> <br> </h2>*
return dictionary containing all parameters of reaction <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|properties| dict|	dictionary of parameters | 
 <br>
 
 *<h2><strong> <em>  get_reversible(self) </em></strong> <br> </h2>*
return the reversibility of reactionkind: global function <br> 
kind: global function <br> 

| Param | Type | Description |
|----------|----------|------ |
|get_reversible| boolean|state of the reversibility | 
 <br>
 
 *<h2><strong> <em> equation(self) </em></strong> <br> </h2>*
return the stochiometric equation of reaction <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|equation| string|	return the stochiometric equation | 
 <br>

*<h2><strong> <em> get_enzyme_name(self) </em></strong> <br> </h2>*
return enzyme name <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|enzyme name| string|	return the enzyme name | 
 <br>
 
 
 *<h2><strong> <em> add_enzyme(self,enzyme) </em></strong> <br> </h2>*
add the enzyme to the list enzyme  <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|enzyme| string|	name of the enzyme responsible of the reaction | 
 <br>
 
  *<h2><strong> <em> isinreaction(self,a,b) </em></strong> <br> </h2>*
find the link between two metabolites <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|isinreaction|boolean| return True if a is the source of the reaction, `False` if it's the opposite and `None` if one of the elements is not in the reaction|
|a| string|metabolite's id | 
|b| string|metabolite's id | 
 <br>
 
  *<h2><strong> <em> extract_species(Metabos) </em></strong> <br> </h2>*
Built and fill networkx graph with metabolite  <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Metabos| dict|	extract species from Metabos | 

return a graph built with networkx
 <br>
 
 
 *<h2><strong> <em> extract_reactions(Reactions, G) </em></strong> <br> </h2>*
Edits networkx graph with reactions  <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Reactions| dict|	extract reactions from Reactions| 
| G |  networkx_object|	graph built with networkx reactions are edges | 

 <br>
  
 *<h2><strong> <em> dag_init(node,edge) </em></strong> <br> </h2>*
Create networkx specific graph (directed acyclic graph) <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|node| dict|	dictionary containing all the information about the nodes to build the graph| 
|edge |dict |	dictionary containing all the information about the edge to build the graph | 

return a networkx graph
 <br>
 
 *<h2><strong> <em> shortest_path(Graph) </em></strong> <br> </h2>*
Measure all shortest paths of the graph <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	gives the shortest paths | 

return a dict
 <br>
 
  *<h2><strong> <em> degree_centrality(Graph) </em></strong> <br> </h2>*
Measure the degree centrality of each nodes <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	give the degree centrality | 

return a dict
 <br>
 
   *<h2><strong> <em>  betweenness_centrality(Graph) </em></strong> <br> </h2>*
Measure the betweenness centrality of each nodes <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	give the betweeness centrality | 

return a dict
 <br>
 
   *<h2><strong> <em> all_pairs_nodes_connectivity(Graph) </em></strong> <br> </h2>*
Measure the connectivity of each pairs of nodes <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	give the connectivity of each pairs of nodes  | 

return a dict
 <br>
 
 *<h2><strong> <em> degree (Graph) </em></strong> <br> </h2>*
Save the degree of each nodes <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	degree of each nodes | 

return a dict
 <br>
 
 *<h2><strong> <em> diameter (Graph) </em></strong> <br> </h2>*
Measure the graph diameter <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph| graph diameter | 

return a dict
 <br>
 
  *<h2><strong> <em> eccenticity (Graph) </em></strong> <br> </h2>*
Measure the eccentricity of each nodes <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	eccentricity of nodes | 

return a dict
 <br>
 
 
  *<h2><strong> <em> tarjan (Graph) </em></strong> <br> </h2>*
Find the strongly connected component of the graph with the tarjan algorithm <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	give the SCC with the algorithm named Tarjan | 

return a dict
 <br>
 
 
  *<h2><strong> <em> taagseed(Metabo,Reaction, Graph) </em></strong> <br> </h2>*
Measure the graph diameter <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Metabo| dict|	Dictionary of metabo objects | 
|Reaction| dict|	Dictionary of reaction objects | 
|Graph| Networkx graph|	graph diameter | 

return Dictionary of seeds 
 <br>
 
  *<h2><strong> <em> ancestors (Graph) </em></strong> <br> </h2>*
Find the ancestor of one node <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 |
|node| dict| Dictionary of nodes in the graph	 | 

return a dict
 <br>
 
   *<h2><strong> <em> display_all(Graph, Reactions, Metabo) </em></strong> <br> </h2>*

kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Metabo| dict|	Dictionary of metabo objects | 
|Reactions| dict|	Dictionary of Reaction object | 
|Graph| Networkx graph|	Display all topology results of the graph on the terminal | 

 <br>
 
 *<h2><strong> <em> display_shortest_path(Graph) </em></strong> <br> </h2>*
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	Display all shortest paths of the graph on the terminal | 

 <br>
 
  *<h2><strong> <em> display_degree_centrality(Graph) </em></strong> <br> </h2>*
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	Display the degree centrality of each nodes on the terminal | 

 <br>
 
 *<h2><strong> <em> display_betweenness_centrality(Graph) </em></strong> <br> </h2>*
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	Display the betweenness centrality of each nodes on the terminal| 

 <br>
 
  *<h2><strong> <em> display_connectivity(Graph) </em></strong> <br> </h2>*
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	Display the connectivity of each pairs of nodes on the ter | 

 <br>
 
  *<h2><strong> <em> display_degree(Graph) </em></strong> <br> </h2>*
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	Display the degree of each nodes on the terminal | 

 <br>
 
  *<h2><strong> <em> display_diameter(Graph) </em></strong> <br> </h2>*
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	Display the graph diameter on the terminal | 

 <br>
 
  *<h2><strong> <em> display_eccentricity (Graph) </em></strong> <br> </h2>*
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	Display the eccentricity of each nodes on the terminal | 

 <br>
 
 
  *<h2><strong> <em>  display_seed(Graph, Reactions, Metabo) </em></strong> <br> </h2>*
Display all seeds of the metabolic network on the terminal <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 
|Reactions| dict|Dictionary of Reaction object	 | 
|Metabo|dict|Dictionary of Metabo object	 | 

<br>
 
 
  *<h2><strong> <em> save_all(Graph, Reactions, Metabo) </em></strong> <br> </h2>*
Save all topology results of the graph in a JSON file <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 
|Reactions| dict|Dictionary of Reaction object	 | 
|Metabo|dict|Dictionary of Metabo object	 | 

<br>

   *<h2><strong> <em> save_shortest_path(Graph) </em></strong> <br> </h2>*
Save all shortest paths of the graph in a JSON file <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 

<br>
 
  *<h2><strong> <em> save_degree_centrality(Graph) </em></strong> <br> </h2>*
Save the degree centrality of each nodes in a tsv file <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 

<br>

  *<h2><strong> <em> save_connectivity(Graph) </em></strong> <br> </h2>*
Save the connectivity of each pairs of nodes in a tsv file <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 

<br>

 *<h2><strong> <em> save_degree(Graph) </em></strong> <br> </h2>*
Save the degree of each nodes in a tsv file <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 

<br>


 *<h2><strong> <em> save_diameter(Graph) </em></strong> <br> </h2>*
Save the graph diameter in a JSON file <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 

<br>
 
*<h2><strong> <em> save_eccentricity(Graph) </em></strong> <br> </h2>*
Save the eccentricity of each nodes in a JSON file <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 

<br>

*<h2><strong> <em> save_betweenness_centrality (Graph) </em></strong> <br> </h2>*
Save the betweenness centrality of each nodes in a tsv file <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 

<br>


*<h2><strong> <em> save_seed(Graph, Reaction, Metabo) </em></strong> <br> </h2>*
Save all seeds of the metabolic network in a JSON file <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Graph| Networkx graph|	 | 
|Reactions| dict | Dictionary of Reaction object	 | 
|Metabo| dict| Dictionary of Metabo object 	 | 

<br>

*<h2><strong> <em> defelements(Metabos, Reactions) </em></strong> <br> </h2>*
Built a list of data from dictionary object of type Metabo and Reaction <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Reactions| dict | Dictionary of Reaction object	 | 
|Metabo| dict| Dictionary of Metabo object 	 | 

return a list of all the informations extracts from the object

<br>

*<h2><strong> <em> defcsc(Metabos, Reactions, S) </em></strong> <br> </h2>*
Built a list of data for create Dash graph with apparent strongly connected component <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Reactions| dict | Dictionary of Reaction object	 | 
|Metabo| dict| Dictionary of Metabo object 	 | 
|S| dict| Dictionary of strongly connected component	 | 

return a list of all the informations for built Dash graph with apparent strongly connected component
<br>


*<h2><strong> <em> defdag(node, edge) </em></strong> <br> </h2>*
Built a list of data for create Dash graph with strongly connected component as node <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|node| dict |Dictionary of strongly connected component| 
|edge| dict| Dictionary of strongly connected component link | 

return a list of all the informations for built Dash graph with strongly connected component as nodes
<br>

*<h2><strong> <em> visualise(Metabo, react, graph) </em></strong> <br> </h2>*
Built a list of data for create Dash graph with strongly connected component as node <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Metabos| dict |Dictionary of Metabo object| 
|Reactions | dict| Dictionary of Reaction object | 
|Graph| Networkx graph|	 | 

return a list of all the informations for built Dash graph with strongly connected component as nodes
<br>

*<h2><strong> <em> update_layout(value) </em></strong> <br> </h2>*
Uptdate the graph between three types of visualisation <br>
kind: global function <br> 
| Param | Type | Description |
|----------|----------|------ |
|Value | string |Name of the selected graph| 

return a list of the graph representation
<br>
