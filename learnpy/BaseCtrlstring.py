# python Base Ctrl string

S0 = ''		# void string
S0_1 = ""	
S1 = "spam's"	# double quote same as single quote
S2 = 's\np\ta\x00m'		# Unicode
S3 = """..."""	# Triple-quoted strings

S4 = r'\temp\spam'		# Raw string--在引号左侧加R或r关闭转义
"""注意，一个raw字符串不能以单个的反斜杠结尾，因为反斜杠会转义后续引用的字符，仍然必须转义外围引号字符以将其嵌入到该字符串中。也就是说，r“…\”不是一个有效的字符串常量，一个raw字符串不能以奇数个反斜杠结尾。如果需要用单个的反斜杠结束一个raw字符串，可以使用两个反斜杠并分片掉第二个反斜杠(r’1\nb\tc\\’[:-1])、手动添加一个反斜杠(r’1\nb\tc’+’\\’)，或者忽略raw字符串语法并将常规字符串中的反斜杠改为双反斜杠(\1\\nb\\tc\\’)。以上三种形式都会创建同样的8字符的字符串，其中包括3个反斜杠。"""

S5 = b'spam'	# bytes string in python 3.0
S6 = u'spam'	# Unicode string only use in python 2.6

# 

"""
S7 = S1 + S2		# Combine
S7 * 3		# Copy(repeat)
S7[i]		# index
S7[i:j]		# section
len(S7)		# length	
"""

# 

name = 'Leo'
'worker %s' % name
num = 1230080058
'%s %s %s %s' % ('Worker', name, 'Number', num)
'%s---%s---%s' % (42, 3.14, [1,2,3])
# 在%的左边放置一个字符串，字符串里面放置了一个或者多个使用%开头的嵌入对象。	 在%的右边放入一个（或多个，嵌入元组当中）对象，这些对象将插入到左边的转换目标位置上。
S8 = "a {0} parrot".format('kind')		# stringformatting in 2.6/3.0
S9 = "search Worker & Number : {0} ; {1}".format(name,num)

# 

s = "222222this is string example....wow!!!2222222"
s.find('pa')	# search keyword in string
s.rstrip('2')		# Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）。
s.replace('is', 'is not')	# replace
s.split()		#Python split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
s.split('!', 1)		# split(str="", num=string.count(str))str 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。num 分割次数。
s.isdigit()		# Only digit in this string
# s = "1232131"		 s.isdigit() 	 	True
s.lower()		# String case conversion

# 

s.endswith('spam')		# str.endswith(suffix, start, end) suffix:该参数可以是一个字符串或者是一个元素。start:字符串中的开始位置。end:字符中结束位置。
"""str = "this is string example....wow!!!";

suffix = "wow!!!";
print str.endswith(suffix);
print str.endswith(suffix,20);

suffix = "is";
print str.endswith(suffix, 2, 4);
print str.endswith(suffix, 2, 6);"""

# 

'-'.join(strlist)	# insert delimiter -- strlist = ("a","b")  a-b

s.encode('latin-1','strict')	#str.encode(encoding='UTF-8',errors='strict')
#以encoding指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。

# 

"""	
for x in S:print(x)
'spam' in S
[c * 2 for c in s]
"""

# 

# map() 可接收函数名或可迭代对象
ls = [1,2,3]
rs = map(str, ls)
It [1,2,3,4,5]
def addself(num):
	return num+1
rs = map(addself, It)

""" 标准库re模块（正则表达式）支持更高级的基于模式的字符串处理，XML解析器 更高级的文本处理工具。"""