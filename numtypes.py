# python new numeric types

a= 1/3
print(a)

b= (1/3)+(3/4)
print(b)

import decimal
d = decimal.Decimal('3.141')
print(d+1)

decimal.getcontext().prec = 2
c = decimal.Decimal('1')/ decimal.Decimal('3')
print(c)

from fractions import Fraction
f = Fraction(2,3)
print(f)
print(f+1)
print(f+ Fraction(1,2))