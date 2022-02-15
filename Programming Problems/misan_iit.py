list1 = []
user_input = int(input("Enter Your Number :- "))

for i in range(1,user_input):
    list2 = []
    for k in range(user_input-i):
        list2.append(1)
    list2.append(i)
    
    list1.append(list2)
    
len = 0
for i in list1:
    len += 1
    print(len,i)
    temp = i
    t_num = -2
    while True:
        if temp[-1] - temp[t_num] >1:
            temp[-1] = temp[-1] -1
            temp[t_num] = temp[t_num] +1
            len +=1
            print(len,temp)
        else:
            if temp[t_num] == temp[0]:
                break
            else:
                t_num = t_num -1
len += 1
print(f"{len} [{user_input}]")