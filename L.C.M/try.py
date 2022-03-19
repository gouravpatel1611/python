import random
name=input("Enetr your good name:> ")
print(f"Hello {name}")
inteligent=0
chutiya=0
a=0
while(a<=10):
    i = random.randint(1,2)
    number=int(input("Enter your choice:>"))
    if(i==number):
        print("Your are inteligent")
        inteligent+=1
        print(f"you are inteligwnt at {inteligent}:— times")
    if(i!=number):
        print("You are chutiya")
        chutiya+=1
        print(f"you are chutiya at {chutiya}:— times")