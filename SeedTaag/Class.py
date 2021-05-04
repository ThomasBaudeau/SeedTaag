class Metabo():
    """objet representing metabolites
    """
    def __init__(self, id, name, compartment, boundaryc, hosu, constant):
    """
    objet repertoriant tous les paramètres associés aux métabolites 

    Args: 
        id( string): identifiant d'un métabolite 
        name(string): nom du métabolite
        compartment (string) : compartiment 
        boundary
        hosu 
        constant
    """
        self.id = id
        self.name = name
        self.compartment = compartment
        self.boundaryc=boundaryc #Boundary condition
        self.hosu=hosu  #has Only Substance Unit
        self.constant=constant

    def properties(self):
        """
        donne un dictionnaire contenant tous les paramètres d'un métabolite 
        
        Returns : 
            dict: dictionnaire des paramètres 
        """
        return {'id': self.id, 'name': self.name, 'compartment': self.compartment,
        'boundaryConditions':self.boundaryc,'hasOnlySubtanceUnit':self.hosu,'constant':self.constant}

    
    def get_id(self):
        """
        donne l'identifiant d'un métabolite
        
        Returns : 
            string: identifiant des métabolites 
        """
        
        return self.id

class Reaction():
  
    def __init__(self, id, name, reversible, reactifs, products,ename):
        """
        objet repertoriant tous les paramètres associés aux réactions

    Args: 
        id( string): identifiant d'un métabolite 
        name(string): nom du métabolite
        enzyme (string) : nom de l'enzyme
        reversible (boolean): indique si la réaction est réversible
        reactifs (list <tuples>) : liste du couple des identifiants des réactifs et du coefficient stochiométrique 
        products (list <tuples>) : liste du couple des identifiants des produits et du coefficient stochiométrique 
        """
        self.id = id
        self.name = name
        self.enzymes=[ename]
        self.reversible = reversible
        self.__reactifs = reactifs
        self.__products = products

    def get_reactifs(self, stoichiometry=False):
        """
        renvoie la liste des identifiants des réactifs ou si le paramètre stochiométrique est vrai renvoie la liste des tuples (reactifs-coefficients stochiométriques )
        Args : 
            stochiometry (boolean): indique si l'on souhaite les coefficients stochiométriques
        """
        if stoichiometry:
            return self.__reactifs
        else:
            return [(reactif['species']) for reactif in self.__reactifs]

    def get_products(self, stoichiometry=False):
        """
        
        renvoie la liste des identifiants des produits ou si le paramètre stochiométrique est vrai renvoie la liste des tuples (produits-coefficients stochiométriques )
        Args : 
            stochiometry (boolean): indique si l'on souhaite les coefficients stochiométriques
        """
        if stoichiometry:
            return self.__products
        return [(product['species']) for product in self.__products]

    def properties(self):
        """
        
        donne un dictionnaire contenant tous les paramètres d'une réaction
        
        Returns : 
            dict: dictionnaire des paramètres 
        """
        return {'id': self.id, 'name': self.name, 'reversible': self.reversible,
                'reactifs': self.get_reactifs(), 'products': self.get_products(),'enzymes':self.get_enzyme_name()}

    def get_reversible(self):
        """
       donne la réversibilité d'une réaction
        
        Returns : 
            boolean:  indique si la réaction est réversible 
        """
        return self.reversible

    def equation(self):
        """
        à partir d'une réaction renvoie l'équation chimique de la réaction 
        Return : 
            string (équation)
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
         donne le nom d'une enzyme
        
        Returns : 
            string: le nom de l'enzyme 
        
        """
      return self.enzymes

    def add_enzyme(self,enzyme):
        """
        rajoute l'enzyme à la liste des enzymes 
        """
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
