import SeedTaag.data_extraction as de
import SeedTaag.graph_formation as gf
import os

def init_data(file):
    try:
        open(file)
    except Exception as e:
        raise ValueError(e, ' Error')
    model=de.create_sbml(file)
    Metabos = de.extract_species(model)
    Reactions = de.extract_reactions(model, Metabos)
    return Metabos,Reactions


def init_graph(Metabos, Reactions,dag=False):
    if not dag:
        G = gf.extract_species(Metabos, gf.create_graphe)
        G = gf.extract_reactions(Reactions,G)
    else:
        G = gf.dag_init(Metabos,Reactions)
    return G
