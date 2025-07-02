class E_Shopping():
    def __init__(self,name):
        self.name=name
        self.sellers=[]
        self.customers=[]
    
    def add_sellers(self, seller):
        self.sellers.append(seller)
    def add_customer(self,customer):
        self.customers.append(customer)