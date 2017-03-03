#! /usr/bin/python
# _*_ coding:utf-8 _*_

Martix = {}
Martix[(2,3,4)] = 88
Martix[(7,8,9)] = 98
print(Martix)
X = int(input())
Y = int(input())
Z = int(input())

#Check for key before fetch
if (X,Y,Z) in Martix:
	print(Martix[(X,Y,Z)])
else:
	print(0)

# try to index / Catch and recover
try:												
	print(Martix[(X,Y,Z)])
except KeyError:
	print(0)

# Exists: fetch and return / Doesn't exist: use default arg
print(Martix.get((X,Y,Z), 0))
print(list(Martix.keys()))

input()