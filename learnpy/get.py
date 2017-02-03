# method of get

d={'t':1}

#index but with a default
value = d.get('haha',0) 
print(value)

value1 = d['t'] if 'haha' in d else 0
print(value1)