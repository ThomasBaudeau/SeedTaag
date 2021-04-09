import data_extraction as de
import Class as C
import graph_formation as gf

def init_data(filename):
    model=de.create_sbml(filename)
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

