import Class as C
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
    DictOfSpecies={species.id: C.Metabo(species.id, species.name, species.compartment) for species in  model.getListOfSpecies()}
    return DictOfSpecies

# REACTIONS #
def extract_reactions(model, Metabos):
    DictOfReactions={}
    for reaction in model.getListOfReactions(): 
        ListOfReactifs=[(Metabos[reactif.species], int(reactif.stoichiometry)) for reactif in reaction.getListOfReactants()]
        ListOfProducts=[(Metabos[product.species], int(product.stoichiometry)) for product in reaction.getListOfProducts()] 
        DictOfReactions[reaction.id] = C.Reaction(reaction.id, reaction.name, reaction.reversible, ListOfReactifs, ListOfProducts)
    return DictOfReactions
