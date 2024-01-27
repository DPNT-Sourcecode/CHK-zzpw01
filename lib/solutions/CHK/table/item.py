class Item:
    def __init__(self,ID,price,offerAmount,OfferPrice):
        self.ID=ID
        self.price=price
        self.offerAmount=offerAmount
        self.OfferPrice=OfferPrice
    
    def calculateDiscount(self,quantity):
        return 0