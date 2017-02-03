"""try (sum)"""
m = [[1,4,6],[2,2,2],[5,6,6]]
g= (sum(row) for row in m)
print(next(g))