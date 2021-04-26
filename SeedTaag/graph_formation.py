import networkx as nx
import SeedTaag.Class as C


def extract_species(Metabos):
    """built and fill networkx graph with metabolite

    Args:
        Metabos (dict): dictionary of Metabo object

    Returns:
        networkx objet: graph built with networkx
    """                                                         
    G = nx.DiGraph()
    for key in Metabos:
            properties=Metabos[key].properties()
            G.add_node(key, id=properties['id'],name=properties['name'],compartiment=properties['compartment'],
                       boundaryConditions=properties['boundaryConditions'], hasOnlySubtanceUnit=properties['hasOnlySubtanceUnit'],
                       constant=['constant'])
    return G
   
def extract_reactions(Reactions, G):
    """fill networkx graph with reaction

    Args:
        Reactions (dict): dictionary of reaction object
        G (networkx object): networkx graph

    Returns:
        networkx object: graph built with networkx the reactions reflect the edges
    """ 
    for key in Reactions:
        properties = Reactions[key].properties()
        for reactant in properties['reactifs']:
            for product in properties['products']:
                G.add_edge(reactant.get_id(), product.get_id(), id=key,name=properties['name'],
                enzymes=properties['enzymes'])
                if (properties['reversible']):
                    G.add_edge(product.get_id(), reactant.get_id(), id=key,
                                name=properties['name'], enzymes=properties['enzymes'])
    return G


def dag_init(node,edge):
    """create networkx specific graph (directed acyclic graph)

    Args:
        node (dict): dictionary containing all the information about the nodes for build the graph
        edge (dict): dictionary containing all the information about the edge for build the graph

    Returns:
       networkx object:networkx graph (dag)
    """
    dag = nx.DiGraph()
    for key in node:
        dag.add_node(key, id='scc'+str(key), group=node[key]['groupe'],
        lenght=node[key]['lenght'])
    for key in edge:
        dag.add_edge(edge[key]['r'],edge[key]['p'], id=key)
    return dag
