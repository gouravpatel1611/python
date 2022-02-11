print('''

No.  NAME.        QTY.        PRIZE
1.   Milk         1L          250/-
2.   Powder       1kg         350/-
3.   choklate     1 pies      300/-
''')


a = {1:['milk',1,250],2:['powder',1,350],3:['choklate',1,300]}

user_itm = {}
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
            
            print("{:12} {:9} {:10}".format("NAME","QTY","PRIZE"))
            for j in user_itm:
                print("{:10} {:5} {:10}".format(user_itm[j][0],user_itm[j][1],user_itm[j][2]*user_itm[j][1]))
            break
    else :
        print("Wrong input ! Try again ")