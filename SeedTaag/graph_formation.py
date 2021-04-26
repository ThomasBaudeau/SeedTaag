import networkx as nx
import SeedTaag.Class as C


def extract_species(Metabos):
    G = nx.DiGraph()
    """
    extract informations of the dictionnary and built graph node
    """
    for key in Metabos:
            properties=Metabos[key].properties()
            G.add_node(key, id=properties['id'],name=properties['name'],compartiment=properties['compartment'],
                       boundaryConditions=properties['boundaryConditions'], hasOnlySubtanceUnit=properties['hasOnlySubtanceUnit'],
                       constant=['constant'])
    return G
   
def extract_reactions(Reactions, G):
    """
    extract information about reaction in model libSMBL object
    """
    for key in Reactions:
        properties = Reactions[key].properties()
        for reactant in properties['reactifs']:
            for product in properties['products']:
                G.add_edge(reactant.get_id(), product.get_id(), id=key,name=properties['name'],
                enzymes=properties['enzymes'])
                if (properties['reversible']):
                    G.add_edge(product, reactant, id=key,
                                name=properties['name'], enzymes=properties['enzymes'])
    return G


def dag_init(node,edge):
    dag = nx.DiGraph()
    for key in node:
        dag.add_node(key, id='scc'+str(key), group=node[key]['groupe'],
        lenght=node[key]['length'])
    for key in edge:
        dag.add_edge(edge[key]['r'],edge[key]['p'], id=key)
    return dag