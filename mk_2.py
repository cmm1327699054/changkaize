#！/usr/bin/python
#-*-coding:utf-8-*-
# import  sys
# print(sys.path.append(r'E:\kkkkkkkk\python111\py_1908\mk_2.py'))
# print(sys.path)
# import random
# from python111.py_1908 import mk_1
# print(dir(random))

#打开一个文件，如果没有这个文件的话则创建
# a=open('a.txt','w',encoding='utf-8')
#向文件中写入内容，如果文件里原本由内容的话就会覆盖
# a.write('qwe'+'\n')
# a.write('ewq')
#关闭打开的文件
# a.close()

# a=open(r'c:\Users\Admin\Desktop\新建文本文档 (2).txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         a.write('%d*%d=%d\t'%(j,i,i*j))
#     a.write('\n')

# a=open(r'C:\Users\Admin\Desktop\CHPG4MD1C$TVBPB3DLR4V$3.png','rb')
# b=a.read()
# a.close()
# c = open('a.jpg','wb')
# c.write(b)
# c.close()
#
# from ruamel.yaml import YAML
# # 第一步，创建一个yaml对象
# yaml = YAML(typ='safe')
# with open('aa.yaml','r',encoding='utf-8')as y:
#     data = yaml.load(y)
# print(data['grandpa']['name'])

'给excel写99乘法表'
# import xlwt
# #给excel文件写入编码格式
# book = xlwt.Workbook(encoding='utf-8')
# sheet = book.add_sheet('py_1908')
# #往单元格里添加内容
# for i in range(10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'%d*%d=%d'%(i,j,i*j))
# sheet.write( )
# book.save('acc.xls')

# import xlrd
# #打开一个xls文件
# open_book = xlrd.open_workbook('aa.xls')
# #统计标签页的个数
# count_sheet = open_book.nsheets
# print(count_sheet)
# #第一种获取标签页的方法，通过索引值获取
# # huoQuSheet = open_book.sheets()
# # sheet = huoQuSheet[0]
# # sheet = huoQuSheet[1]
# #第二种获取标签页的方法，通过名称获取
# sheetName = open_book.sheet_names()
# print(sheetName)
# sheet = open_book.sheet_by_name('py_1908')
#
# #获取行数
# count_row = sheet.nrows
# print(count_row)
#
# #获取列数
# count_col = sheet.ncols
# print(count_col)
# #获取一行数据
# for i in range(9):
#     line_data = sheet.row_values(i)
#     print(line_data)
# #获取一列数据，输出是一个列表，0代表第一列
# lie_data = sheet.col_values(0)
#



# a=input('>>>>>')
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b=b+j*10**(len(a)-1-i)
#             break
# print(b)
#












# # 将 excel 中内容 导入到txt 中
# import xlrd
# geshi = xlrd.open_workbook('aa.xls') #xlwt.Workbook()
# a=geshi.nsheets   #统计有多少个标签页
# b = geshi.sheets()[0]  #通过过索引值进入标签页
# txt = open(r'E:\kkkkkkkk\py_1908\a.txt','w',encoding='utf-8')
# for i in range(1,10):
#     z = b.cell(i,0).value   # 循环获取格子里的内容
#     txt.write('\t')
#     txt.write(z)
# txt.close()


# from xlutils.copy import copy
# import xlrd
# src_excle = xlrd.open_workbook('aa.xls')
# #复制文件并不是直接在文件里操作而是
# #复制一份在操作，只有写入功能，没有读功能
# excel = copy(src_excle)
# #获取标签页，xlrd中的获取方法不能用只能用get_sheet(0) 0是第一
# #个标签页的位置
# sheet = excel.get_sheet(0)
# #写入内容
# sheet.write(10,10,'内容')
# #保存是还用复制的文件来保存就可以了
# excel.save('aa.xls')


# try:
#     a=1+[23]
# except Exception as e:
#     #这个可以看异常类型
#     print(type(e).__name__)
#     #这个可以看异常描述
#     print(e)


# try:
#     a = 'adfgall'+123
# except NameError as e:  #只避免某个异常
#     print('helo')
# except TypeError as f
# print()


# try:
#     a = 1+2
# except:
#     print('hello')
# finally:
#     print('world')

# a=open(r'E:\kkkkkkkk\py_1908\a.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         a.write('%d*%d=%d\t'%(j,i,i*j))
#     a.write('\n')

import time
# # shijian=time.time()    #从1970年到8点现在的秒数
# # print(shijian)
# a=time.time()
# def hanshu():
#     for i in range(1000000):
#         pass
# hanshu()
# b=time.time()
# print(f'{b-a}')

# a = time.localtime(9999999999) #以结构化时间显示本地时间
# print(a)

# a=time.gmtime() #以结构化时间显示uct时间
# print(a)

# import time
#将结构化时间转换为格式化时间
# a = time .strftime('%y-%m-%d\n%X',time.localtime())
# print(a)
# #将格式化时间转换为结构化时间
# c=time.strptime('2019-12-16 11:24:30','%Y-%m-%d %X')
# print(c)

#以结构化时间显示本地时间
# a=time.localtime(123)
# #将结构花时间转换为时间戳
# b=time.mktime(a)
# print(a)

# import time
# # a = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# # print(a)

# import random
# a=random.randint(1,10)
# for i in range(3):
#     b=int(input('>>>>>'))
#     if b>a:
#         print('大了，你还有%d次机会'%(2-i))
#     elif b<a:
#         print('小了，你和有%d次机会'%(2-i))
#     elif b==a:
#         print('对了')
#         break
# else:
#     print('fae')



# a=[1,2,3,4,5,6,7,8]
# b=int(input('>>>>>'))
# for i in range(len(a)):
#     if b<=a[i]:
#         a.insert(i,b)
#         break
#     elif b>a[-1]:
#         a.insert(a[-1],b)
#     else:
#         continue
# print(a)




















