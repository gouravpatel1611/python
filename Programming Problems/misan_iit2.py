list1 = []
user_input = int(input("Enter Your Number :- "))

for i in range(1,user_input):
    list2 = []
    for k in range(user_input-i):
        list2.append(1)
    list2.append(i)
    
    list1.append(list2)
    
    

    
    
for i in list1:
    print(i)
    lis = i
    temp = -1
    # print(lis[temp] ,"l", list1[temp])
    while True:
        if lis[temp-1] ==1:    
            if lis[temp] - lis[temp-1]>1:
                lis[temp] = lis[temp]-1
                lis[temp-1] = lis[temp-1]+1
                print("ook")