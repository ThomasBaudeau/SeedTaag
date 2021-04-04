import networkx as nx
import SeedTaag.Class as C

def create_graphe():
    """
    built multidigraph object
    """
    G = nx.MultiDiGraph()
    return G


def extract_species(Metabos, G):
    """
    extract informations of the dictionnary and built graph node
    """
    for key in Metabos:
        G.add_node(key)
    return G


def extract_reactions(Reactions, G):
    """
    extract information about reaction in model libSMBL object
    """
    for key in Reactions:
        reactants=Reactions[key].get_reactifs()
        products = Reactions[key].get_products()
        reversible = Reactions[key].getReversible()
        for reactant in reactants:
            for product in products:
                G.add_edge(reactant, product, id=key)
                if (reversible):
                   G.add_edge(product, reactant, id=key)
    return G
