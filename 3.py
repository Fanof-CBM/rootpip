#! usr\bin\python

# split
myjob = "hacker"
myjob[0:3]

# third items mean stride步进
print(myjob[:len(myjob):1])
# stride also can negative[::-1]-reverse
print(myjob[len(myjob)::-1])

# 分片等同用一个分片对象进行索引
'spam'[1:3]
'spam'[slice(1,3)]
'spam'[slice(none,none,-1)]
'spam'[::-1]
# same
input()