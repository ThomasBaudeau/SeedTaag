import data_extraction as de
import Class as C
import graph_formation as gf
import os

def init_data(file):
    try:
        open(file)
    except Exception as e:
        raise ValueError(e, ' Error')
    model=de.create_sbml(file)
    Metabos = de.extract_species(model)
    Reactions=de.extract_reactions(model, Metabos)
    return Metabos,Reactions


def init_graph(Metabos, Reactions,mode=True):
    if mode:
        G = gf.extract_species(Metabos, gf.create_graphe)
        G=gf.extract_reactions(Reactions,G)
    else:
        G = gf.extract_species(Metabos, gf.create_graphe)
        G = G = gf.extract_reactions(Reactions, G,False)
    return G
