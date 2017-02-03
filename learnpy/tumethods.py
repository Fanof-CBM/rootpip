# tuple methods

a=0.3434
T=(0,'abc',a,a,1,3.4)

print(T.index(3.4))
print(T.count(a))

p=input()
q=input()
MixTu =([1,2,3],[[2,3],[p,q]],3.4,0.34,3.4,p,'aaa')
print(MixTu[1][1][0])

# tuple can not use .append (AttributeError: 'tuple' object has no attribute 'append')
""" MixTu.append()"""