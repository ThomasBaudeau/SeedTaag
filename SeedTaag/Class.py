class Metabo():

    def __init__(self, id, name, compartment):
        self.id = id
        self.name = name
        self.compartment = compartment
        self.link={}

    def properties(self):
        return {'id': self.id, 'name': self.name, 'compartment': self.compartment}


class Reaction():

    def __init__(self, id, name, reversible, reactifs, products):
        self.id = id
        self.name = name
        self.reversible = reversible
        self.__reactifs = reactifs
        self.__products = products

    def get_reactifs(self, stoichiometry=False):
        if stoichiometry:
            return self.__reactifs
        else:
            return [reactif for reactif, stoich in self.__reactifs]

    def get_products(self, stoichiometry=False):
        if stoichiometry:
            return self.__products
        return [product for product, stoich in self.__products]

    def properties(self):
        return {'id': self.id, 'name': self.name, 'reversible': self.compartment,
                'reactifs': self.get_reactifs(), 'products': self.get_products()}

    def getReversible(self):
        return self.reversible

    def equation(self):
        text = str(self.name)+" : "
        for reactif, stoich in self.__reactifs:
            text += str(stoich) + "*" + reactif.id + " + "
        text = text[:-2]+"=> "
        for product, stoich in self.__products:
            text += str(stoich) + "*" + product.id + " + "
        return text[:-2]

    def get_enzymes_names(self):
      return {'reactifs' : [reactif.name for reactif in self.get_reactifs()],
              'products' : [product.name for product in self.get_products()]
      }

    def isinreaction(self,a,b):
        if a in self.__reactifs and b in self.__products:
            return True
        elif a in self.__products and b in self.__reactifs:
            return False
        else:
            return None
