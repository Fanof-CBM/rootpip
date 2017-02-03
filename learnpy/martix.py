vec=[-4,-2,0,2,4]
[x*2 for x in vec]
print([x for x in vec if x>= 0])
print([abs(x) for x in vec])
freshfruit =['   banana      ','    loganberry','passion    fruit    ']
print([weapon.strip() for weapon in freshfruit])
print([(x,x**2) for x in range(10)])
vec=[[1,2,3],[4,5,6],[7,8,9],[1,2]]
print([num for elem in vec for num in elem])
from math import pi
print([str(round(pi,i)) for i in range(1,6)])
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(matrix)
print([[row[i] for row in matrix] for i in range(4)])
transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
transposed=[]
for i in range(4):
    transposed_row=[]
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
list(zip(*matrix))
