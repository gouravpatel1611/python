# print("%s is a play boy"%('rahul patel'))
# print("this is a stetment 1 ",end="")
# print("this is a stetment 2")
# print("rahul "*8)

# #list 

# name = ['rahul','gourav','sandeep','ankit']
# print(name[10])
# name[0]= "rahul patel"
# print(name[0])

# print(name)
# print(name[1:3])
# list2 = ['table','fan','chair','bord','computer']
# list2.append('mobile')
# print(list2)
# list2.insert(0,'fridge')
# print(list2)
# list2.remove('table')
# print(list2)
# print(name + ['mehul','ankit','dikesh'])
# print(name)
# print(len(name))
# print(max(name))
# print(min(name))


# # Tuples

# tupl = (14,2,3,)
# print(tupl[2])
# lis = list(tupl)
# print(lis[0])


# # dictionaries
# marks = {
#             'gourav': 5,
#             'rahul': 7,
#             'sandeep':9,
#             'ankit':8  }
# print(marks)
# print(marks['gourav'])
# print(marks['rahul'])
# marks['rahul'] = 10
# print(marks['rahul'])
# print(marks.keys())
# print(marks.values())




# #if and else 

# num = int(input("enter your % :- "))

# if (num>90 and num<100):
#     grade = 'A'
# elif(num<80 and num<100 ):
#     grade = 'B'
# else:
#     grade = "Don't know"
# print("your grade is :- ",grade)


# #loops

# lim = int(input("Enter how many times You want to run Loop :- "))
# for i in range(0,lim):
#     print(i)

# list2 = ['table','fan','chair','bord','computer']
# for i in list2:
#     print(i)


# # while loop

# num = int(input("Enter your number :- "))
# while(num>4):
#     print("number is gretar then 4 ")
#     num = int(input("Enter your number :- "))
#     if (num ==9):
#         break # continew
    
        
# # funcation 

# def avg(a,b):
#     return a+b/2

# print(avg(2,3))

    
# # String 

# str ="this is a string"
# print(str[0])
# print(str[-1])
# print(str[3:7])
# print(len(str))
# print(str[0:16:2])
# print(str.capitalize())
# print(str.find("this"))
# print(str.find("thids"))
# print(str.replace("is","are"))
# print(str)

# # File Io


# file1 = open("gp.txt","wb")
# print(file1.mode)
# print(file1.name)

# file1.write(bytes("this is wrriten by a python ","UTF-8"))
# file1.close()


# file2 = open("gp.txt","r+")
# t_to_r = file2.read()
# print(t_to_r)
# file2.close()



# #OOP object oriyented prigramin


# class Employee:
#     __name = None
#     __id = 0
#     __salary = 0
    
    
#     def __init__(self,name,id,salary,):
#         self.__name = name
#         self.__id = id
#         self.__salary = salary
        
        
        
#     def set_name(self, name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
        
        
        
# # gourav = Employee() // whitout init
# # gourav.name = "gourav patel"     
# # print(gourav.name)
# # gourav.set_name("gourav")
# # print(gourav.get_name())


# raul = Employee("rahul patel",18,50000)
# print(raul.get_name())

    