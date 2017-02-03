# python 3 种方法计算平方根，性能留待后面介绍

import math
n1 = math.sqrt(256) # module
n2 = 256 ** 0.5	# expression
n3 = pow(256, .5) # built-in

n4 = math.sqrt(1234567890)
n5 = 1234567890 ** .5
n6 = pow(1234567890, .5)

for pr in n1,n2,n3,n4,n5,n6:
	print (pr)