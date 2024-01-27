
# noinspection PyUnusedLocal
# skus = unicode string


from .table.item import Item
from .table.offer import Offer

def checkout(skus):
    # Init price table and offers
    itemAOffer = Offer("A",5,200)
    itemAOffer2 = Offer("A",3,130)
    itemAOffers = [itemAOffer,itemAOffer2]
    itemA = Item("A",50,itemAOffers)

    itemBOffer = Offer("B",2,45)
    itemBOffers = [itemBOffer]
    itemB = Item("B",30,itemBOffers)

    itemC = Item("C",20,[])

    itemD = Item("D",15,[])

    itemEOffer = Offer("B",2,0)
    itemEOffers = [itemEOffer]
    itemE = Item("E",40,itemEOffers)

    items = {"A":itemA,"B":itemB,"C":itemC,"D":itemD,"E":itemE}

    checkoutValue = 0
    discountItems={"A":0,"B":0,"C":0,"D":0,"E":0}

    for sku in skus:
        if sku in items:
            # calculate value
            currentItem = items[sku]
            if len(currentItem.offer)>0:
                discountItems[sku]+=1
            else:
                checkoutValue += currentItem.price
        else:
            return -1
    # calculate checkout from items with discount
    print(discountItems,checkoutValue)
    for discountItem in discountItems:
        currentItem = items[discountItem]
        nItems = discountItems[discountItem]
        summed=False
        for offer in currentItem.offer:
            if nItems >= offer.offerAmount and currentItem.ID == offer.ItemID:
                nDiscount = nItems/offer.offerAmount
                nRemovedItems = int(nDiscount)*offer.offerAmount
                while(int(nDiscount)>0):
                    checkoutValue += offer.OfferPrice
                    nDiscount-=1
                    print(checkoutValue,nDiscount)
                currentItems= nItems-nRemovedItems
                print(currentItems,checkoutValue)
                checkoutValue +=currentItems*currentItem.price
                nItems=currentItems
                summed=True

            elif nItems >= offer.offerAmount and currentItem.ID != offer.ItemID and offer.ItemID in skus :
                checkoutValue += nItems*currentItem.price
                freeItemID = offer.ItemID
                freeItemValue = items[freeItemID].price
                checkoutValue -= freeItemValue
                summed=True
        if not summed:
            checkoutValue += nItems*currentItem.price
    return checkoutValue




