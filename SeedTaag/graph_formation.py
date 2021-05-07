import networkx as nx
import SeedTaag.Class as C


def extract_species(Metabos):
    """Built and fill networkx graph with metabolite

    :param Metabos: Dictionary of Metabo object
    :type Metabos: dict 
    :returns: graph built with networkx
    :rtype: networkx_object
    """                                                         
    G = nx.DiGraph()
    for key in Metabos:
            properties=Metabos[key].properties()
            G.add_node(key, id=properties['id'],name=properties['name'],compartiment=properties['compartment'],
                       boundaryConditions=properties['boundaryConditions'], hasOnlySubtanceUnit=properties['hasOnlySubtanceUnit'],
                       constant=['constant'])
    return G
   
def extract_reactions(Reactions, G):
    """Edits networkx graph with reactions

    :param Metabos: dictionary of reaction object
    :param G: networkx graph
    :type Metabos: dict
    :type G: networkx_object
    :returns: graph built with networkx reactions are edges
    :rtype: networkx_object
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
    """Create networkx specific graph (directed acyclic graph)

    :param node: dictionary containing all the information about the nodes to build the graph
    :param edge: dictionary containing all the information about the edge to build the graph
    :type node: dict
    :type edge: dict 
    :Returns: networkx graph (dag)
    :rtype: networkx_object
    """
    dag = nx.DiGraph()
    for key in node:
        dag.add_node(key, id='scc'+str(key), group=node[key]['groupe'],
        lenght=node[key]['lenght'])
    for key in edge:
        dag.add_edge(edge[key]['r'],edge[key]['p'], id=key)
    return dag
