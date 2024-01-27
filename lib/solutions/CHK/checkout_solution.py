
# noinspection PyUnusedLocal
# skus = unicode string


from .table.item import Item
from .table.offer import Offer

def checkout(skus):
    # Init price table and offers
    itemAOffer = Offer("A",3,130)
    itemAOffers = [itemAOffer]
    itemA = Item("A",50,itemAOffers)

    itemBOffer = Offer("B",2,45)
    itemBOffers = [itemBOffer]
    itemB = Item("B",30,itemBOffers)

    itemC = Item("C",20,[])

    itemD = Item("D",15,[])

    items = {"A":itemA,"B":itemB,"C":itemC,"D":itemD}

    checkoutValue = 0
    discountItems={"A":0,"B":0,"C":0,"D":0}

    for sku in skus:
        if sku in items:
            # calculate value
            currentItem = items[sku]
            for offer in currentItem.offer:
                if offer.offerAmount>0:
                    discountItems[sku]+=1
                else:
                    checkoutValue += currentItem.price
        else:
            return -1
    # calculate checkout from items with discount
    for discountItem in discountItems:
        currentItem = items[discountItem]
        nItems = discountItems[discountItem]
        for offer in currentItem.offer:
            if nItems >= offer.offerAmount:
                nDiscount = nItems/offer.offerAmount
                nRemovedItems = int(nDiscount)*offer.offerAmount
                while(int(nDiscount)>0):
                    checkoutValue += offer.OfferPrice
                    nDiscount-=1
                currentItems= nItems-nRemovedItems
                checkoutValue +=currentItems*currentItem.price
                print(checkoutValue)
        else:
            checkoutValue += nItems*currentItem.price
    return checkoutValue


