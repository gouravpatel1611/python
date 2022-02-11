

# enter=str(input("Press Enter to continue :"))

# print('''


#                 ----WELCOME TO SUPERMARKET----


# ''')
# a=str(input("Enter your name : \n"))
# b=str(input("Enter your Address : \n"))
# c=int(input("Enter your Phone No : \n"))

print('''

     OPTIONS

    1.BUY ITEM
    2.EXIT  

''')

item_list = {"MILK":250,"CORN FLAKES":130,"WHEAT":100,"TEA POWER":150,"COFFE POWER":500 }


while True:
    options=int(input("Enter your options : \n"))
    if options == 1:
        print('''

    GROCERY LISTS :

    S.NO                PRODUCT              QUANTITY             PRICE
    1.                  MILK                   1L                 250 
    2.                  CORN FLAKES            1KG                130   
    3.                  WHEAT                  1KG                100                   
    4.                  TEA POWDER             1KG                150  
    5.                  COFFE POWDER           1KG                500
    
    
    ''')
        item_qty = {}
        while True:
            try:
                item = int(input("Enter the sn. which item you want to buy"))
                temp = " Enter the Qntity of "+list(item_list.keys())[item-1]+ " "
                qty = int(input(temp))
                value = input("press C for continew and Q for exit")
                if value == "c":
                    continue
                elif value == "q" and value == "Q":
                    print(item_qty)
                    break
                else:
                    print("worng input")
            except:
                print("wrong input")
            item_qty[list(item_list.keys())[item-1]] = qty
        break
    elif options == 2 :
        print('''
    

    -----THANKYOU VISIT AGAIN-----

    
    ''')
        break

    else :
        print("INVALID OPTION ENTERED")
