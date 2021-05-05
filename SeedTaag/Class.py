class Metabo():
    """objet listing all parameters associated to metabolite 

        :param string id: id of a metabolite
        :param string name: name of a metabolite
        :param string compartment: name of the compartment
        :param boolean boundaryc : status of the boundary condition
        :param boolean hosu: tell if has only substance unit  
        :param boolean constant: tell if it is constant
    """

    def __init__(self, id, name, compartment, boundaryc, hosu, constant):
        """Constructor"""
        self.id = id
        self.name = name
        self.compartment = compartment
        self.boundaryc=boundaryc #Boundary condition
        self.hosu=hosu  #has Only Substance Unit
        self.constant=constant

    def properties(self):
        """gives a dictionary containing all the parameters of a metabolite
        
        :returns : dictionary of parameters
        :rtype: dictionary 
        """
        return {'id': self.id, 'name': self.name, 'compartment': self.compartment,
        'boundaryConditions':self.boundaryc,'hasOnlySubtanceUnit':self.hosu,'constant':self.constant}

    
    def get_id(self):
        """return metabolite's id 
        
        :returns : metabolite's id
        :rtype: string
        """
        
        return self.id

class Reaction():
    """object listing all parameters associated with reactions

    : param string id: identifier of a metabolite
    : param string name: name of the metabolite
    : param list enzyme: names of the enzyme
    : param boolean reversible: indicates if the reaction is reversible
    : param reactants dict: list of the pair of reagents identifiers and the stochiometric coefficient
    : param products dict: list of the pair of product identifiers and stochiometric coefficient
    """
  
    def __init__(self, id, name, reversible, reactifs, products,ename):
        """Constructor"""
        
        self.id = id
        self.name = name
        self.enzymes=[ename]
        self.reversible = reversible
        self.__reactifs = reactifs
        self.__products = products

    def get_reactifs(self, stoichiometry=False):
        """return list of metabolite object or return dict of metabolite with stochiometry

        :param boolean stochiometry: default false define return mode with or without stochiometry

        :returns: metabolite object
        :rtype: list or dict
        """
        if stoichiometry:
            return self.__reactifs
        else:
            return [(reactif['species']) for reactif in self.__reactifs]

    def get_products(self, stoichiometry=False):
        """return list of metabolite object or return dict of metabolite with stochiometry

        :param boolean stochiometry: default false define return mode with or without stochiometry

        :returns: metabolite object
        :rtype: list or dict
        """
        if stoichiometry:
            return self.__products
        return [(product['species']) for product in self.__products]

    def properties(self):
        """
        return dictionary containing all parameters of reaction
        
        :returns: dictionary of parameters
        :rtype: dict 
        """
        return {'id': self.id, 'name': self.name, 'reversible': self.reversible,
                'reactifs': self.get_reactifs(), 'products': self.get_products(),'enzymes':self.get_enzyme_name()}

    def get_reversible(self):
        """
        return the reversibility of reaction
        
        :returns: state of the reversibility
        :rtype: boolean
        """
        return self.reversible

    def equation(self):
        """
        return the stochiometric equation of reaction

        :return: equation
        :rtype:string 
        """
        text = str(self.name)+" : "
        for reactif, stoich in self.__reactifs:
            text += str(stoich) + "*" + reactif.id + " + "
        text = text[:-2]+"=> "
        for product, stoich in self.__products:
            text += str(stoich) + "*" + product.id + " + "
        return text[:-2]

    def get_enzyme_name(self):
        """
         return enzyme name
        
        :returns: enzyme name
        :rtype:string 
        """
        return self.enzymes

    def add_enzyme(self,enzyme):
        """
        add the enzyme to the list enzyme 

        :param string enzyme:name of the enzyme responsible of the reaction
        """
        self.enzymes.apppend(enzyme)


    def isinreaction(self,a,b):
        """find the link between two metabolites

        :param string a: metabolite's id
        :param string b: metabolite's id

        :returns:True if a is the source of the reaction, False if it's the opposite and None if one of the elements is not in the reaction
        :rtype: Boolean 
        """
        reactifs = self.get_reactifs()
        products = self.get_products()
        if a in reactifs and b in products:
            return True
        elif a in products and b in reactifs:
            return False
        else:
            return None
