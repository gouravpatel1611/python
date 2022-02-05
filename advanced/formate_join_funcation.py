# formate
# 
user = ["rahul","gourav","mehul","sandeep"]
mobails = ["oppo","samsang","sarkari","Poco"]

for i in range(len(user)):
    template = "Mobaile Used By {} is {}".format(user[i],mobails[i])
    print(template)
    
# Join funcation
print(" and ".join(user))
