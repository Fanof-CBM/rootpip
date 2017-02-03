# learn file object

# make a new file in output mode

f= open('.\generate\start.txt','w')

#write strings of bytes to it
f.write('to celebrate!\n')

# Close to flush output buffers to disk
f.close()

"""
	Absolute path 
	C:\Users\Lenovo\Desktop\python\generate\start.txt
	Relative path 
	.\generate\start.txt
"""
