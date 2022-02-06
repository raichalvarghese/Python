class Shopping:
    def __init__(self,basket,buyer):
        self.basket=list(basket)
        self.buyer = buyer
    def __len__(self):
        count = len(self.basket)
        return count*2
shopping = Shopping(['Shoes','dress'],'Raichal')
print(len(shopping))
