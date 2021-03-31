class Metabo():
    
    def __init__(self, id, name, compartment):
        self.id=id
        self.name=name
        self.compartment=compartment
        
    def properties(self):
        return {'id': self.id, 'name' : self.name, 'compartiment' : self.compartment}
    

class Reaction():
    
    def __init__(self, id, name, reversible, reactifs, products):
        self.id=id
        self.name=name
        self.reversible=reversible
        self.__reactifs=reactifs
        self.__products=products

    def get_reactifs(self, stoichiometry=False):
        if stoichiometry:
            return self.__reactifs
        else: 
            return [reactif for reactif, stoich in self.__reactifs]
        
        
    def get_products(self, stoichiometry = False):
        if stoichieometry:
            return self.__products
        return [product for product, stoich in self.__products]
    
    
    def properties(self):
        return {'id': self.id, 'name' : self.name, 'reversible' : self.compartment,
               'reactifs' : self.reactifs, 'products' : self.products}
    
    def equation(self):
        text=str(self.name)+" : "
        for reactif, stoich in self.reactifs:
            text+=str(stoich) + "*" + reactif + " + "
        text = text[:-2]+"=> "
        for product, stoich in self.products:
            text+= str(stoich) + "*" + product + " + "
        return text[:-2]
        
        


#metabo_1=get_species(model)[0]        
#metabo_1.properties()
#metabo_1.name
#model = import_data(filename)
#get_species(model)
#get_reactions(model)[0].equation()
#'Phosphofructokinase : 1*M_atp_c + 1*M_f6p_c => 1*M_adp_c + 1*M_fdp_c + 1*M_h_c '
