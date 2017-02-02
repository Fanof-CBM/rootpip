# allow to check object type

L =[int( input())]

if type(L) == type([]):
	print('list')

if type(L) == int:
	print('int')
	
if isinstance(L, str):
	print('yes')

print(type(L))
