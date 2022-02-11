#--------------Global variable-------------------
name =""
address = ""
contect_no = ""
user_itm = {}
a = {
    1:['milk',"1 L",250],
    2:['powder',"1 Kg",350],
    3:['choklate',"1 piece",300]
    }
#~~~~~~~~~~~~~~~~~~~~~~~~~~~End~~~~~~~~~~~~~~~~~~

# # ---------------User detailse ----------------
def user_entry():
    global name, address, contect_no
    print(" \t ~~ Welcome To Online Markate ~~")
    print("\n")
    name = input("Enter you name :- ")
    address = input(" Enter Your address:- ")
    contect_no = input(" Enter Your Contect No. :-")
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~End~~~~~~~~~~~~~~~~~~

#--------------------- Print Item List ----------------
def grocery_list():
    print("\n")
    print(" \t ~~ Grocery List ~~")
    t_num = 1
    print("{:3} {:13} {:15} {:10}".format("No.","NAME","QTY","PRIZE"))
    for i in a:
        print("{:3} {:13} {:9} {:10}".format(t_num,a[i][0],a[i][1],a[i][2]))
        t_num += 1
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~End~~~~~~~~~~~~~~~~~~


#---------------------Product List ------------------
def add_itm():
    k = 0
    while True:
        k += 1
        num = int(input("Enter your product no. :- "))
        if num <= len(a):
            qty = int(input(f"Enter Qty of {a[num][0]}  :-  "))
        
            user_itm[k]= [a[num][0],qty,a[num][2]]
            temp = input("A for Add more item else any :- ")
            if temp == 'A' or temp == 'a':
                pass
            else:
                bill_print()
                break
        else :
            print("Wrong input ! Try again ")
            temp = input("A for Add item else any :- ")
            if temp == 'A' or temp == 'a':
                pass
            else:
                break
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~End~~~~~~~~~~~~~~~~~~

#--------------------- Bill Print ------------------

def bill_print():
    print("\n")
    print("\t ~~ Your Bill ~~")
    print("Name :-", name)
    print("Address :-", address)
    print("Contect Number :-", contect_no)
    print("{:3} {:20} {:9} {:10}".format("No.","NAME","QTY","PRIZE"))
    t_n = 0
    total_rs = 0
    for j in user_itm:
        t_n += 1
        print("{:3} {:13} {:9} {:10}".format(t_n,user_itm[j][0],user_itm[j][1],user_itm[j][2]*user_itm[j][1]))
        total_rs += user_itm[j][2]*user_itm[j][1]
    print("\n")
    print(" {:10} {:12} {:5}".format("Total Prize :",total_rs,"/-"))
    print(" {:10} {:9} {:5}".format("Online tex 2.5% :",total_rs*2.5/100,"/-"))
    print(" {:10} {:15} {:5}".format("Final Prize :",total_rs+total_rs*2.5/100,"/-"))
    print(" ")
    print("\t ~~ Thanks For Comming Our Site ~~")


# #~~~~~~~~~~~~~~~~~~~~~~~~~~~End~~~~~~~~~~~~~~~~~~

    
def main():
    # user_entry()
    grocery_list()
    add_itm()
    
    
    
if __name__=="__main__":
    main()