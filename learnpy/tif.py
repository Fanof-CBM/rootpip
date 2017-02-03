# find keys in dictionary but don't know which key do we have, so we need to run a test

# this is the problem we meet
d = {'a':1}
d['b']=10

# want to get a key but it doesn't exist
"""d['h']"""  #error

#so
'f' in d
if not 'f' in d:
	print('not exist')