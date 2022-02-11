item_list = {"MILK":250,"CORN FLAKES":130,"WHEAT":100,"TEA POWER":150,"COFFE POWER":500 }
item = 0
qty = 5
item_qty = {}
item_qty[list(item_list.keys())[item-1]] = qty
print(item_qty)