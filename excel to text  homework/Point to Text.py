#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 取每行前3列的数据
import xlrd
data = xlrd.open_workbook(r"C:\Users\Lenovo\Desktop\excel to text  homework\excel.xls") # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
Test_txt_file = open("C:\\Users\\Lenovo\\Desktop\\excel to text  homework\\test.txt",'w') # 打开txt文件
Test_txt_file.write("Point\n")
for i in range(nrows): # 遍历每行
	table.row_values(i)[:3] # 取前三列
	Test_txt_0 = int(table.row_values(i)[0]) #取三列
	Test_txt_1 = table.row_values(i)[1]
	Test_txt_2 = table.row_values(i)[2]
	Test_txt_file.write(str(Test_txt_0) + "\t" + str(Test_txt_1) + "\t" + str(Test_txt_2) + "\t" + "1.#QNAN 1.#QNAN" + "\n")
Test_txt_file.write("End\n")
Test_txt_file.close()