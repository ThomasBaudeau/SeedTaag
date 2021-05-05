import SeedTaag.data_extraction as de
import SeedTaag.graph_formation as gf
import os

def init_data(file):
    """create two dictionaries of reaction or metabo object from an sbml file

    :param string file : name of the sbml file

    :returns: two dictionaries containing objects of type metabo or of type reaction

    :rtype: dictionary

    :Raises ValueError: Error if the file can't be open
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

    :param dict Metabos:dictionary of metabo object
    :param dict Reactions:dictionary of reaction object
    :param boolean dag: select function mode (default=False)

    :returns: networkx graph 
    :rtype: networkx_objet
    """
    if not dag:
        G = gf.extract_species(Metabos)
        G = gf.extract_reactions(Reactions,G)
    else:
        G = gf.dag_init(Metabos,Reactions)
    return G
