import libsbml
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Kosaraju():  
    
    #On initialise les paramètres de la classe:
    def __init__(self, G, classic=False):
        # On introduit le graphe dans la classe comme propriété
        self.G=G
        # On récupère les espèces du graphe 
        self.classic=classic
        if self.classic :
            self.species_nodes=G.nodes
        else:
            self.species_nodes=get_species(G)
        
        self.reset_visit(self.species_nodes) 
        
    def reset_visit(self, nodes):
        # un dictionnaire qui indique si un noeud a été visité pou run noeud
        self.visited = {node: False for node in nodes} 
        self.suffix=1 
        
    def neighbors(self,G,node):
        if self.classic:
            return G.neighbors(node)
        else :
            return get_neighbors(G,node)
        
    def explore(self,G, start_node):
        self.visited[start_node]=True
        for neighbor in self.neighbors(G,start_node): 
            if not self.visited[neighbor]:  
                self.explore(G, neighbor)
        
        self.suffix_order[start_node]=self.suffix  
        self.suffix+=1  
    
    def all_visited(self): 
        #On compte le nombre de noeud visité, si la clé vaut true -> 1 et si false -> 0
        nb_visit=sum([self.visited[key] for key in self.visited]) 
        #On returne vrai si tous les noeuds ont été visités, faux sinon
        return len(self.visited)==nb_visit 
        
    def dfs(self, G, nodes):  
        self.suffix_order = {node: 0 for node in self.species_nodes} 
        self.reset_visit(nodes) 
        start_tree=[]  
        while not self.all_visited():
            for key,value in self.visited.items(): 
                if value==False:
                    start_node=key
                    break
            start_tree.append(start_node)  
            self.explore(G, start_node)
        return start_tree 
            
    def get_SCC(self):  
        self.dfs(self.G, self.species_nodes) 
        order=sorted(self.suffix_order.items(), key=lambda item:item[1],reverse=True)  
        order=[k for k,v in order]
        Gt=self.G.reverse()
        start_tree=self.dfs(Gt, order)
        l=[]
        s=None 
        for node in order: 
            if node in start_tree: 
                l.append(s)
                s=[node] 
            else:
                s.append(node)
        l.append(s) 
        return l[1:] 


#Permet de selectionner les noeuds pour chaque type
def get_species(G):
    return [n for (n,ty) in     nx.get_node_attributes(G,'Type').items() if ty == 'species'] #on sélectionne les nodes avec le type espèce 

def get_reactions(G):
    return [n for (n,ty) in     nx.get_node_attributes(G,'Type').items() if ty == 'reaction'] #on sélectionne les nodes avec le type réaction

#on dessine le graphe 
def plot_graphe(G):
    species_nodes = get_species(G)
    reaction_nodes = get_reactions(G)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=species_nodes,         node_color='blue', node_shape='o',alpha=.5)
    nx.draw_networkx_nodes(G, pos, nodelist=reaction_nodes,         node_color='red', node_shape='s',alpha=.5)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    plt.show()

#permet de sélectionner les espèces "voisines" d'une espèce (les produits des réactifs)
def get_neighbors(G,reagent):
    neighbors=[]
    for reaction in G.neighbors(reagent):
        neighbors+=list(G.neighbors(reaction))
    return neighbors

def create_sbml(filename):
    """
    built libSBML object from a SBML file
    """ 
    G=nx.MultiDiGraph()
    reader=libsbml.SBMLReader()
    if reader==None:
        raise ValueError('LibSBML package should have been installed')
    doc=reader.readSBML(filename)
    if doc.getNumErrors()>0:
        raise ValueError(doc.printErrors())
    model=doc.getModel()
    return model,G

def extract_species(model,G):
    """
    extract information about species in model libSMBL object
    """
    for specie in model.getListOfSpecies():
        id_sp=specie.getId()
        
        constant_sp=specie.getConstant()
        bdrcdt_sp=specie.getBoundaryCondition()
        only_unit_sp=specie.getHasOnlySubstanceUnits()
        name_sp=specie.getName()
        sbo_term_sp=specie.getSBOTermID()
        comptment_sp=specie.getCompartment()
        G.add_node(id_sp, constante=constant_sp, bd_condition=bdrcdt_sp,unite=only_unit_sp, name=name_sp, sbo=sbo_term_sp, compartiment=comptment_sp,Type="species")
    return G

def extract_reactions(model,G):
    """
    extract information about reaction in model libSMBL object
    """
    for reaction in model.getListOfReactions():
        reaction_id=reaction.getId()
        reaction_name_=reaction.getName()
        reaction_reversible=reaction.getReversible()
        reactants=[reactant.species for reactant in reaction.getListOfReactants()]
        products = [product.species for product in reaction.getListOfProducts()]
        for reactant in reactants:
            for product in products:
                G.add_edge(reactant,product,id=reaction_id,name=reaction_name_)
                if (reaction_reversible):
                   G.add_edge(product, reactant, id=reaction_id,name=reaction_name_)
    return G
model,G=create_sbml('e_coli_core_simp_noEX.sbml')
G=extract_species(model, G)
G=extract_reactions(model, G)
test=Kosaraju(G) # on appelle l'objet qui enregistre le graphe et qui contient l'algorithme 
SCC=test.get_SCC() # on récupère les composantes convexes
C=[
    c
    for c in sorted(
        nx.kosaraju_strongly_connected_components(G), key=None, reverse=False)
    ]
print(C)
print(SCC)
plot_graphe(G)
plt.show()