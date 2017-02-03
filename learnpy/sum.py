"""try (sum)"""
m = [[11,0,19],[2,12,2],[5,6,6]]
g= (sum(row,0) for row in m)
s= (next(g),next(g),next(g))
print(s)
print(list(map(sum,m)))

SUM= {sum(row) for row in m}
print(SUM)
keyvalue = {i:sum(m[i]) for i in range(3)}
print(keyvalue)