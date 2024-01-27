
# noinspection PyUnusedLocal
# skus = unicode string


from .table.item import Item
from .table.table import Table

def checkout(skus):
    # Init price table and offers
    itemA = Item("A",50,3,130)
    itemB = Item("B",30,2,45)
    itemC = Item("C",20,0,0)
    itemD = Item("D",15,0,0)
    items = {"A":itemA,"B":itemB,"C":itemC,"D":itemD}

    checkoutValue = 0
    discountItems={"A":0,"B":0}

    for sku in skus:
        if sku in items:
            # calculate value
            currentItem = items[sku]
            if currentItem.offerAmount>0:
                discountItems[sku]+=1
            else:
                checkoutValue += currentItem.price
        else:
            return -1
    print(discountItems)
    # calculate checkout from items with discount
    for discountItem in discountItems:
        currentItem = items[discountItem]
        nItems = discountItems[discountItem]

        nDiscount = nItems/currentItem.offerAmount
        nRemovedItems = nDiscount*currentItem.offerAmount
        print(int(nDiscount))
        while(int(nDiscount)>0):
            checkoutValue += currentItem.OfferPrice
            nDiscount-=1
        currentItems= nItems-nRemovedItems
        print(currentItems,nItems,nRemovedItems)
        checkoutValue +=currentItems*currentItem.price
    return checkoutValue







