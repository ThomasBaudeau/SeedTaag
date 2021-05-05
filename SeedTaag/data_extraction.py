import SeedTaag.Class as C
import libsbml


def create_sbml(filename):
    """ built libSBML object from a SBML file

    :param filename : name of the sbml file to read
    :type filename: string 
    :returns: object who contains all the information in the file
    :rtype: lisbml_object

    :raises ValueError: Incorrect sbml file
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
    """extract information about species in a libSBML model

    :param model: libsbml object containing all the information from an sbml file
    :type model: string 
    :returns: dictionary containing all the metabolites of the libsbml object as metabolite objects 
    :rtype : dict 
    """
    DictOfSpecies = {species.id: C.Metabo(species.id, species.name, species.compartment, species.getBoundaryCondition(),
    species.getHasOnlySubstanceUnits(), species.constant) for species in model.getListOfSpecies()}
    return DictOfSpecies

# REACTIONS #
def extract_reactions(model, Metabos):
    """create a reaction object dictionary from a libsml object

    :param model: libsbml object containing all informations contained in sbml file
    :type model: libsbml_object
    :param dict Metabos: dictionary containing metabolites as metabolite objects
    :type Metabo: Metabos_object
    :returns:dictionary containing all the reaction of the libsbml object as reaction objects
    :rtype:dict 
    :raises ValueError: catch exception if the reactant or product list can't be correctly create
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


