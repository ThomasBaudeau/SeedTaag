import SeedTaag.data_extraction as de
import SeedTaag.Class as C
import SeedTaag.graph_formation as gf

def init_data(filename):
    model=de.create_sbml(filename)
    Metabos = de.extract_species(model)
    Reactions=de.extract_reactions(model, Metabos)
    return Metabos,Reactions


def init_graph(Metabos, Reactions):
    G = gf.extract_species(Metabos, gf.create_graphe)
    G=gf.extract_reactions(Reactions,G)
    return G