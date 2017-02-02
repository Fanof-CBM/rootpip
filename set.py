# what is set

# make a set in 2.6 or 3.0
x = set('spam')

# make a set with new 3.0
y = {'h','d','e'}
print(x,y)

# function of set
print(x&y)  #intersection
print(x|y)  #union
print(x-y)	#difference

# set comprehensions in 3.0
forset= {x**2 for x in [1,2,3,4]}
print(forset)