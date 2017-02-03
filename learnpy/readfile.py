# learn file object

# read file
# for the script, the content in file no matter what type it is, the file content is always a string

f= open('.\generate\start.txt','r')


# nomal use read() to read file
data = f.read()
print(data)
print ('\n')

# file content is always string
print(data.split())

# because python has automatic recovery, when the var f above used, it closed.
f_0= open('.\generate\start.txt','r')

# use for to read file is the best
for char in f_0:
	print(char)