list_1 = [30, 48, 14, 33, 1, 4, 18,21, 1, 14, 22, 6, 39, 7]
print("list comprehension",[item for item in list_1 if item%3 ==0])


dict_1 = {
    'a' : 45,
    'b' : 5,
    'A' : 7,
}

print("Dictionary coprehension",{k.lower():dict_1.get(k.lower(),0)+dict_1.get(k.upper(),0) for k in dict_1.keys()})

set1 = {x**2 for x in [1,2,56,4,58,41,5,14,4,5,4,54,14,4,5,41,45,41,4,]}

print(set1)
