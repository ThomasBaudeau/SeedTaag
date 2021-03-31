import os.path
from libsbml import *
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Metabo():
    
    def __init__(self, id, name, compartment):
        self.id=id
        self.name=name
        self.compartment=compartment
        
    def properties(self):
        return {'id': self.id, 'name' : self.name, 'compartiment' : self.compartment}
    

class Reaction():
    
    def __init__(self, id, name, reversible, reactifs, products):
        self.id=id
        self.name=name
        self.reversible=reversible
        self.__reactifs=reactifs
        self.__products=products

    def get_reactifs(self, stoichiometry=False):
        if stoichiometry:
            return self.__reactifs
        else: 
            return [reactif for reactif, stoich in self.__reactifs]
        
        
    def get_products(self, stoichiometry = False):
        if stoichieometry:
            return self.__products
        return [product for product, stoich in self.__products]
    
    
    def properties(self):
        return {'id': self.id, 'name' : self.name, 'reversible' : self.compartment,
               'reactifs' : self.reactifs, 'products' : self.products}
    
    def equation(self):
        text=str(self.name)+" : "
        for reactif, stoich in self.reactifs:
            text+=str(stoich) + "*" + reactif + " + "
        text = text[:-2]+"=> "
        for product, stoich in self.products:
            text+= str(stoich) + "*" + product + " + "
        return text[:-2]
        
        


#metabo_1=get_species(model)[0]        
#metabo_1.properties()
#metabo_1.name
#model = import_data(filename)
#get_species(model)
#get_reactions(model)[0].equation()
#'Phosphofructokinase : 1*M_atp_c + 1*M_f6p_c => 1*M_adp_c + 1*M_fdp_c + 1*M_h_c '

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


