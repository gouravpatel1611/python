# *args and **kwargs



# def fun(*args):
#     if (len(args)==3):
#         print("The name is ",args[0]," and age is ",args[1])
#         print("Roll number is :- ",args[2])
#     elif(len(args)==2):
#         print("The name is ",args[0]," and age is ",args[1])
    
        

    
    
# fun("Gourav Patel",19,1611)
# fun("rahul patel",18)
# list = [ "sandeep patel", 19, 45634]
# fun(*list)


       
# **kwargs

def func(**kwargs):
    for key,value in kwargs.items():
        print(key,"-",value)
        
        
marks_list = {
    "Gourav": 55,
    "Rahul" : 70,
    "sandeep": 80,
    "Dikesh" : 93,
}

func(**marks_list)