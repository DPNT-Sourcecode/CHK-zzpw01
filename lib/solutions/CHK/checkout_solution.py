
# noinspection PyUnusedLocal
# skus = unicode string
from lib.solutions.CHK.table import item


def checkout(skus):
    # Init price table and offers
    itemA = Item("A",50,3,130)
    itemB = item("B",30,2,45)
    itemC = Item("C",20,0,0)
    itemD = Item("D",15,0,0)
    items = [itemA,itemB,itemC,itemD]
    table = Table(items)
    # calculate checkout
    return skus
    

