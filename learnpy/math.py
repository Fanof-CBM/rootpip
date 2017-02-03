# python math

import math
a = math.floor(2.5)
b = math.floor(-2.5)
c = math.trunc(2.5) 
d = math.trunc(-2.5)

print(a,b,c,d)

e = 5/2,5/-2
f = 5//2,5//-2
g = 5/2.00,5/-2.0
h = 5//2.0,5//-2.0 #5//-2.0 = -3.0

print(e,f,g,h)

# make 5/-2 = -2 otherwise it will become -2.5, use '//
# will become -3
i = math.trunc(5 / -2)
print(i)
