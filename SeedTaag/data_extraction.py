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

def get_all_reversible(Reactions, name=False):
  all_reversible=[]
  for reaction in Reactions.values():
    if reaction.reversible:
      if name :
        all_reversible.append(reaction.name)
      else :
        all_reversible.append(reaction)
  return all_reversible

def get_all_transport(Reactions, name=False):
  all_transport=[]
  for reaction in Reactions.values():
    if reaction.transport:
      if name :
        all_transport.append(reaction.name)
      else :
        all_transport.append(reaction)
  return all_transport
