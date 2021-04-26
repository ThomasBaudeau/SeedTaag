import SeedTaag.data_extraction as de
import SeedTaag.graph_formation as gf
import os

def init_data(file):
    """create two dictionaries reaction or metabo object from an sbml file

    Args:
        file (string): name of the sbml file

    Raises:
        ValueError: Error if the file can't be open

    Returns:
        dictionaries: two dictionaries containing objects of type metabo or of type reaction
    """
    try:
        open(file)
    except Exception as e:
        raise ValueError(e, ' Error')
    model=de.create_sbml(file)
    Metabos = de.extract_species(model)
    Reactions = de.extract_reactions(model, Metabos)
    return Metabos,Reactions


def init_graph(Metabos, Reactions,dag=False):
    """create networkx graph with two dictionaries of metabo or of reaction or create network x graph with dict of node and edge

    Args:
        Metabos (dict): dictionary containing objects of type Metabo or dictionary of node
        Reactions (dict): dictionary containing objects of type Reaction or  dictionary of edge
        dag (bool, optional): set the networkx x graph to dag mode . Defaults to False.

    Returns:
        networkx object: graph built with networkx
    """
    if not dag:
        G = gf.extract_species(Metabos)
        G = gf.extract_reactions(Reactions,G)
    else:
        G = gf.dag_init(Metabos,Reactions)
    return G
