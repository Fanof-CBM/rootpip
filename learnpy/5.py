#! usr\bin\python

#test
a = str(3.1415) + str(float("1.5"))
b = float(str(3.1415)) + float("1.5")
print(a,b)
input()

# generate next character
# chr -- chr(115) -- 's'
# ord -- ord('s') -- 115

S = '1'
S = chr(ord(S)+1)
print(S)
input()