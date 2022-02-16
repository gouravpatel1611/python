import random
input("CLICK ENTER TO CONINUE : \n")
r={}
k=0
prices={
        1:['DORMATRY',1,400],
        2:['ORDINARY ROOM',1,1200],
        3:['STANDARD ROOM',1,3400],
        4:['SUITE ROOM',1,7000]
}

name=str(input("Enter your name : \n"))

print(f'''
Welcome {name}, to Xploiter Hotel Booking 

1.Room Booking
2.Exit

Kindly choose options, To proceed further

''')
options=int(input("Enter your option : \n"))

while True :
    if options == 1:
        print('''

        1.Rooms Info
        2.Book Rooms
        3.Payment
        4.Receipt

        Choose your options,
        NOTE : Before proceeding to Book rooms Check the rooms info
        
        ''')
        option=int(input("Enter your options : \n"))
        while True:
            if option == 1:
                print('''
                
                                    ---------- ROOMS INFO ---------


                DORMATRY      : SINGLE BED,COMMON BATHROOM,HOT WATER AVAILABLE , PRICE- 400
                ORIDNARY ROOM : TV, SINGLE BED, HOT WATER, PRICE - 1200 
                STANDARD ROOM : TV, DOUBLE BED, HOT WATER, AC, WIFI, PRICE, FOOD - 3400
                SUITE ROOM    : 2 ATTACHED ROOMS, FOOD , WIFI , ACCESS TO SWIMMING POOL,BAR ACCESS,GAMING ZONE ACCESS PRICE - 7000 
                ''')
                temp = int(input("Press 0 to go to main menu"))
                if temp == 0:
                    break
            elif option == 2 :
                namee=input("Enter your name : \n")
                pno=input("Enter your Phone number : \n")
                add=input("Enter your Adress : \n ")
                print('''

                            S.NO    ROOMS AVAILABLE
                            1.       DORMATRY
                            2.       ORDINARY ROOM
                            3.       STANDARD ROOM
                            4.       SUITE ROOM

                            Choose from the above options            
                ''')
                room=int(input("Enter your options : \n"))
                while True:
                    if room <= len(prices):
                        days=int(input(f"How many days you wanna stay in {prices[room][0]} : \n"))
                        a=random.randint(51112,60000)
                        price=days*(prices[room][2])
                        r[k]=[prices[room][0],days,price,a]
                        print('ROOM BOOKED SUCCESSFULLY')
                        
                        print(f'''

                        Booking id is {a}

                        Amount to be paid is {price}, Go to Payment section to the amount

                        ''')
                        temp = input("Press 0 to exit : \n")
                        if temp == 0:
                            break
                    break       
                break
        
            elif option == 3 :
                print(f'''
                
                Please select your payment Mode
                Amount to be paid is {price}

                
                Your booking details
                
                ROOM                DAYS                AMOUNT              BOOKING ID
                {r[0][0]}           {r[0][1]}           {price}             {r[0][3]}
                ''')
                debit=int(input("Enter your debit card details : \n"))
                edate=int(input("enter your expire date : \n"))
                eyear=int(input("enter your epired year : \n"))
                cvv=int(input("Enter you card CVV : \n"))
                print(f'''
                
                Payment successfull

                Your booking id is {r[0][3]}

                Exit from here and go to Receipt tab and genrate your receipt
                
                ''')
                exit=int(input("PRESS 0 TO EXIT : \n"))
                if exit==0:
                    break
            elif option==4:
                print(namee)
                print(pno)
                print(add)
                print("----------------RECEPIT---------------")
                print("{:15}{:15}{:15}{:15}".format('ROOM','DAYS','PRICE','BOOKING ID'))
                for value in r.items():
                    print("{:15}{:15}{:15}{:15}".format(r[0][0],r[0][1],r[0][2],r[0][3]))
                print("Nice knowing you, See you at the hotel")
                break
               
                            
                  


                
                

    else:
        print(f"Nice knowing you,{name}")
        break