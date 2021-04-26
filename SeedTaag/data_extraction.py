import SeedTaag.Class as C
import libsbml


def create_sbml(filename):
    """ built libSBML object from a SBML file

    Args:
        filename (string): name of the sbml file to read

    Raises:
        ValueError: LibSBML package should have been installed
        ValueError: doc.printErrors()

    Returns:
        lisbml objet: object who contains all the information in the file
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
    """create dictionary of Metabo object from a libsbml object

    Args:
        model (libsbml object): object who contains all the information contains in sbml file

    Returns:
        dict: dictionary containing all the metabolites of the libsbml object as metabolite objects
    """
    DictOfSpecies = {species.id: C.Metabo(species.id, species.name, species.compartment, species.getBoundaryCondition(),
    species.getHasOnlySubstanceUnits(), species.constant) for species in model.getListOfSpecies()}
    return DictOfSpecies

# REACTIONS #
def extract_reactions(model, Metabos):
    """create a reaction object dictionary from a libsml object

    Args:
        model (libsbml object): object who contains all the information contains in sbml file   
        Metabos (metabo object dictionary): dictionary containing metabolites as metabolite objects

    Raises:
        ValueError: catch exception if the reactif or product list can't be correctly create

    Returns:
        dict: dictionary containing all the reaction of the libsbml object as reaction objects
    """
    DictOfReactions={}
    for reaction in model.getListOfReactions():
      try: 
        ListOfReactifs = [({'species': Metabos[reactif.species],'stochiometry':reactif.stoichiometry}) for reactif in reaction.getListOfReactants()]
        ListOfProducts = [({'species': Metabos[product.species], 'stochiometry':product.stoichiometry})for product in reaction.getListOfProducts()]
        DictOfReactions[reaction.id] = C.Reaction(reaction.id, reaction.name, reaction.reversible, ListOfReactifs, ListOfProducts,None)
      except Exception as e:
        raise ValueError (print(e))
    return DictOfReactions


