# map
a = [1,2,3,4,5,6,7]
b = [x**2 for x in a] #list comprehension
def sqr(n):
    return n**2
c = list(map(sqr,a))
print(a)
print(b)
print(c)

# filter 
def even(n):
    if n%2 ==0:
        return True
    else:
        return False
    
d = list(filter(even,a))
e = [x for x in a if x%2==0] #list comprehension

print(d)
print(e)


# reduce 
from functools import reduce

def sum(a,b):
    return a+b


f = reduce(sum, a)
print(f)