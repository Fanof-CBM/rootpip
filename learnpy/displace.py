# python displacement & boolean

# displacement use in bin numerber for move the numerber

x = 1 # in bin is 0001
b = bin(x << 2) # Shift left 2 bits: 0100
print(b)

#按位进行掩码的运算，使我们可以对一个整体进行多个标志位和值进行编码。
c = x | 2 # bitwise OR: 0011
d = 0b0001 & 0b0001
print(c,d)

# python allow us to code and check the number by bit string in bin and hex

init = 0b0001 #binary literals

a = bin (init<<2)
b = bin (init | 0b010)
c = bin (init & 0b1)
d = 0xFF
e = bin(d)
f = d ^ 0b10101010 # bitwise XOR
g = bin(f)

for pr in a,b,c,e,f,g:
	print(pr)
	
# bit_length
x = 100
a = bin(x), x.bit_length()
b = bin(256), x.bit_length()
c = len(bin(256))-2

for pr in a,b,c:
	print(pr)