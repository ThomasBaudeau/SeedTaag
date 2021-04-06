import SeedTaag.Class as C
import libsbml


def create_sbml(filename):
    """
    built libSBML object from a SBML file
    """
    reader = libsbml.SBMLReader()
    if reader == None:
        raise ValueError('LibSBML package should have been installed')
    doc = reader.readSBML(filename)
    if doc.getNumErrors() > 0:
        raise ValueError(doc.printErrors())
    model = doc.getModel()
    return model

def extract_species(model):
    """
    extract information about species in model libSMBL object
    """
    Metabos={}
    for specie in model.getListOfSpecies():
        id_sp = specie.getId()
        constant_sp = specie.getConstant()
        bdrcdt_sp = specie.getBoundaryCondition()
        onlyUnit_sp = specie.getHasOnlySubstanceUnits()
        name_sp = specie.getName()
        sboTerm_sp = specie.getSBOTermID()
        comptment_sp = specie.getCompartment()
        Metabos[id_sp]=C.Metabo(id_sp,name_sp,comptment_sp)
    return Metabos



def extract_reactions(model,Metabos):
    """
    extract information about reaction in model libSMBL object
    """
    Reactions={}
    for reaction in model.getListOfReactions():
        reaction_id = reaction.getId()
        reaction_name_ = reaction.getName()
        reaction_reversible = reaction.getReversible()
        reactants=[]
        for reactant in reaction.getListOfReactants():
            if not reactant in Metabos:
                raise ValueError(print("Error: sbml file not complet"))
            else:
                reactants.append(reactant)
        products =[]
        for product in reaction.getListOfProducts():
            if not product in Metabos:
                raise ValueError(print("Error: sbml file not complet"))
            else:
                products.append(product)
        Reactions[reaction_id]=C.Reaction(reaction_id,reaction_name_,reaction_reversible,reactants,products)

"""a voir si on garde
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
    return ListOfReaction
"""
