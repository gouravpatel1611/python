add = lambda a,b: a+b

print(add(5,6))

a = [(1,2),(2,3),(5,6),(3,4),(8,4)]
a.sort(key=lambda x:x[1])
print(a)