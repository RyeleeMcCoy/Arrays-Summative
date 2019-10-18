#-------------------------------------------------------------------------------
# Name: Shopping List (Summative)
# Purpose:
#
# Author: Ryelee McCoy
#
# Created:     11/10/2019
# Copyright:   (c) ryelee.mccoy 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


shoplist = {}


def setup():
    addlist = True
    while addlist == True:
        shopping = input(str("What do you need at the store today? type done when you have everything "))
        if shopping == "done":
            addlist = False
        else:
            cost = float(input("What is the cost of that item? " ))
            shoplist[shopping] = cost
    dellist = True
    while dellist == True:
        print(shoplist)
        pick = input(str("Type remove if you have to remove an item or type change if you have to change the cost of an item or type done if everything is correct "))
        if pick == "remove" :
            pickremove = input(str("Which item do you want to remove? "))
            del shoplist[pickremove]
        elif pick == "change":
            pickchange = input(str("What item do you need to change? "))
            costchange = float(input("What is the cost of the item? "))
            shoplist[pickchange] = costchange
        elif pick == "done":
            dellist = False
        else:
            print("Thats not a option sorry try again!")
    totalcost = sum(shoplist.values())
    print(shoplist)
    print("Your total cost is", totalcost)

setup()