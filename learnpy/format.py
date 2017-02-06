# try [] in .format
somelist =  list('SPAM')
x = [0, 100] #以列表的形式生成变量
x[0] = 'first = {0[0]}, third = {0[2]}'.format(somelist)
x[1] = 'first = {0}, last = {1}'.format(somelist[0],somelist[-1])
for i in x:
    print(i)