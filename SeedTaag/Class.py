class Metabo():
    """objet representing metabolites
    """
    def __init__(self, id, name, compartment, boundaryc, hosu, constant):

        self.id = id
        self.name = name
        self.compartment = compartment
        self.boundaryc=boundaryc #Boundary condition
        self.hosu=hosu  #has Only Substance Unit
        self.constant=constant

    def properties(self):
        return {'id': self.id, 'name': self.name, 'compartment': self.compartment,
        'boundaryConditions':self.boundaryc,'hasOnlySubtanceUnit':self.hosu,'constant':self.constant}

    def get_id(self):
        return self.id

class Reaction():

    def __init__(self, id, name, reversible, reactifs, products,ename):
        self.id = id
        self.name = name
        self.enzymes=[ename]
        self.reversible = reversible
        self.__reactifs = reactifs
        self.__products = products

    def get_reactifs(self, stoichiometry=False):
        if stoichiometry:
            return self.__reactifs
        else:
            return [(reactif['species']) for reactif in self.__reactifs]

    def get_products(self, stoichiometry=False):
        if stoichiometry:
            return self.__products
        return [(product['species']) for product in self.__products]

    def properties(self):
        return {'id': self.id, 'name': self.name, 'reversible': self.reversible,
                'reactifs': self.get_reactifs(), 'products': self.get_products(),'enzymes':self.get_enzyme_name()}

    def get_reversible(self):
        return self.reversible

    def equation(self):
        text = str(self.name)+" : "
        for reactif, stoich in self.__reactifs:
            text += str(stoich) + "*" + reactif.id + " + "
        text = text[:-2]+"=> "
        for product, stoich in self.__products:
            text += str(stoich) + "*" + product.id + " + "
        return text[:-2]

    def get_enzyme_name(self):
      return self.enzymes

    def add_enzyme(self,enzyme):
        self.enzymes.apppend(enzyme)


    def isinreaction(self,a,b):
        """find the link between two metabolites

        Args:
            a (string): metabolite's id
            b (string): metabolite's id

        Returns:
            Boolean: True if a is the source of the reaction False if its the opposite and None if one of the elements is not in the reaction
        """
        reactifs = self.get_reactifs()
        products = self.get_products()
        if a in reactifs and b in products:
            return True
        elif a in products and b in reactifs:
            return False
        else:
            return None
