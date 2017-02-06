#! usr/bin/python

# design .format/%

txtbox_0 = str(input("name:\t"))
txtbox_1 = str(input("age:\t"))
vars()
x = "this is worker profile --%(txtbox_0)s --%(txtbox_1)s" % vars()
print (x)