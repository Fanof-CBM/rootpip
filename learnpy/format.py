# try [] in .format
somelist = list('SPAM')
x = list(range(0,int(input())))  # 以列表的形式生成变量
x[0] = 'first = {0[0]}, third = {0[2]}'.format(somelist)
x[1] = 'first = {0}, last = {1}'.format(somelist[0], somelist[-1])
parts = somelist[0], somelist[-1], somelist[1:3]
x[2] = 'first = {0}, last = {1}, middle = {2}'.format(*parts)
for i in x:
    print(i)