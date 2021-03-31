import libsbml

def create_sbml(filename):
    """
    built libSBML object from a SBML file
    """ 
    reader=libsbml.SBMLReader()
    if reader==None:
        raise ValueError('LibSBML package should have been installed')
    doc=reader.readSBML(filename)
    if doc.getNumErrors()>0:
        raise ValueError(doc.printErrors())
    model=doc.getModel()
    return model

def extract_species(model):
    """
    extract information about species in model libSMBL object
    """
    for specie in model.getListOfSpecies():
        id_sp=specie.getId()
        constant_sp=specie.getConstant()
        bdrcdt_sp=specie.getBoundaryCondition()
        onlyUnit_sp=specie.getHasOnlySubstanceUnits()
        name_sp=specie.getName()
        sboTerm_sp=specie.getSBOTermID()
        comptment_sp=specie.getCompartment()

def extract_reactions(model):
    """
    extract information about reaction in model libSMBL object
    """
    for reaction in model.getListOfReactions():
        reaction_id=reaction.getId()
        reaction_name_=reaction.getName()
        reaction_reversible=reaction.getReversible()
        reactants=[reactant.getSpecies()  for reactant in reaction.getListOfReactants()]
        products = [product.getSpecies()  for product in reaction.getListOfProducts()]

model=create_sbml('e_coli_core_simp_noEX.sbml')
extract_species(model)
extract_reactions(model)