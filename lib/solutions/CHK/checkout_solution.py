
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
    for sku in skus:

    # calculate checkout
    return skus
    




