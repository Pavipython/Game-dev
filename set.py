a={}
print(type(a))
b=set()
print(type(b))
c=[1,2,3,4,3,2]
c=set(c)
print(c)
for i in c:
    print(i)
c.add(5)
c.remove(3)
c.discard(7)
print(c)
d={3,4,5,6}
# operations
# union
print(c.union(d))
print(c|d)
print(c.intersection(d))
print(c&d)
print(c.symmetric_difference(d))
print(c^d)
print(c.difference(d))
print(c-d)
print(d.difference(c))
print(d-c)