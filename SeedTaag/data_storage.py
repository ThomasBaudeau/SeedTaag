import SeedTaag.data_extraction as de
import SeedTaag.graph_formation as gf
import os

def init_data(file):
    """Create two dictionaries of reaction or metabo object from an sbml file

    :param file: Name of the sbml file
    :type file: string
    :returns: Two dictionaries containing objects of type metabo or of type reaction
    :rtype: dictionary
    :raises ValueError: Error if the file can't be open
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
    """Create networkx graph with two dictionaries of metabo or of reaction or create network x graph with dict of node and edge

    :param Metabos: Dictionary of metabo object
    :type Metabos: dict
    :param Reactions: Dictionary of reaction object
    :type Reactions: dict
    :param dag: Select function mode (default=False)
    :type dag: boolean
    :returns: networkx graph 
    :rtype: networkx_objet
    """
    if not dag:
        G = gf.extract_species(Metabos)
        G = gf.extract_reactions(Reactions,G)
    else:
        G = gf.dag_init(Metabos,Reactions)
    return G
