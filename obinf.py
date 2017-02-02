
# set a binary file
file = open('.\generate\data1.bin', 'w')
file.write('b\x00\x00\x00\x07spam\x00\x08')
file.close()

# open binary file
data = open('.\generate\data1.bin', 'rb').read()
print(data)
print(data[0:len(data)])