import networkx as nx
import SeedTaag.Class as C

def create_graphe():
    """
    built multidigraph object
    """
    G = nx.DiGraph()
    return G


def extract_species(Metabos, G):
    G = nx.DiGraph()
    """
    extract informations of the dictionnary and built graph node
    """
    for key in Metabos:
        properties=Metabos[key].properties()
        G.add_node(key, id=properties['id'],name=properties['name'],compartiment=properties['compartment'])
    return G


def extract_reactions(Reactions, G,Mclass=True):
    """
    extract information about reaction in model libSMBL object
    """
    for key in Reactions:
        if Mclass:
            reactants=Reactions[key].get_reactifs()
            products = Reactions[key].get_products()
            reversible = Reactions[key].getReversible()
            for reactant in reactants:
                for product in products:
                    G.add_edge(reactant, product, id=key)
                    if (reversible):
                        G.add_edge(product, reactant, id=key)
        else:
            G.add_edge(Reactions[key]['r'], Reactions[key]['p'], id=key)
    return G
