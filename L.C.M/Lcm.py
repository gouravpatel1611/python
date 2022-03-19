import math
print("\t ~ Welcome to L.C.M. Project ~")

num = int(input("Enter your number :- "))

lcm_list = []
divider = 2
main_num = num
while True:
    if main_num == 1:
        print(1)
        break
    elif main_num/divider == 1:
        lcm_list.append(divider)
        print(lcm_list)
        break
    elif math.ceil(main_num/divider) == math.floor(main_num/divider):
        lcm_list.append(divider)
        main_num = main_num/divider
    else:
        divider += 1
    
