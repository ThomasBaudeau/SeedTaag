import os.path
from libsbml import *
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def import_data(filename):
    doc = readSBML(filename)
    model=doc.getModel()
    return model
  
def get_species(model):
    ListOfSpecies=[ Metabo(species.id, species.name, species.compartment) for species in  model.getListOfSpecies()]
    return ListOfSpecies

def get_reactions(model):
    ListOfReactions=[]
    for reaction in model.getListOfReactions():
        ListOfReactifs=[(reactif.species, int(reactif.stoichiometry)) for reactif in reaction.getListOfReactants()]
        ListOfProducts=[(product.species, int(product.stoichiometry)) for product in reaction.getListOfProducts()] 
        ListOfReactions.append(Reaction(reaction.id, reaction.name, reaction.reversible, ListOfReactifs, ListOfProducts))
    return ListOfReactions
