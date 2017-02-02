# pow and abs -- digital processing

import math

n1 = math.pi, math.e  #common constants
n2 = math.sin(2 * math.pi / 180)  # sine, tangent, cosine
n3 = math.sqrt(144), math.sqrt(2)  # Square root
n4 = pow(2,4), 2 ** 4  # exponentiation (power)
n5 = abs(-42.5), sum ((1,2,3,4))
n6 = min (3,1,2,4), max (4,5,6,79)
n7 = sum((1,4)), sum((1,4)), sum((1,4))

for pr in n1,n2,n3,n4,n5,n6,n7:
	print(pr)