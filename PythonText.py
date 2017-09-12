# # -*- coding: UTF-8 -*-
# print ('hello 北京');print ("天安门")
#
# if True:
#     print ("我是好人")
# else :
#     print ("我是坏人")
#
# str1 = "sss"
# str2 = "aaa"
# str3 = "ddd"
# temp = str1 +\
#     str2 +\
#     str3
# print (temp)
#
# # python 的数据类型不用规定，赋给什么类型就是什么类型
#
# num = 1000 #整型
# strhe = "你好中国" #string类型
# strhe1 = '我不好' #string类型 单双引号不区分都表示字符串
# ffff = 1000.1 #浮点型
# name = 'john' #字符串
# print num
# print strhe
# print strhe1
# print ffff
# print name
#
#
# a = b = c = 1
# print a
# print b
# print c
# a,b,c = 1,2,'john'
# print a
# print b
# print c
#
# #标准数据类型
# #在内存中存储的数据可以有多种类型，例如，一个人的年龄可以用个数字来存储，
# #python 定义了一些标准类型，用于存储各种类型的数据
# #python有五个标准的数据类型
# #Numbers（数字#）
# #string（字符串）
# list（列表）
# tuple（元组）
# dictionary（字典）
#
# #python 四种不同的数字类型
# int (有符号整型)
# long （长整型，也可以代表八进制和十六进制）
# float（浮点型）
# conplex（复数）
#
# python字符串
# s = 'ilovepython'
# s[1:5]的结果是love
# 当使用以冒号分隔的字符串，python返回一个新的对象结果包含了以这对偏移标识的连续的内容，

# python列表
# list（列表）是python中使用最频繁的数据类型，列表可以完成大多数集合类的数据结构实现，它支持字符数字，字符串升值看可以包含
# 包含列表用 [ ] 标识，是python中使用最频繁的数据类型
# 列表中值的切割也可以用到变量 [ 头下表：尾下标 ]，就可以截取相应的列表，从左到右默认0开始，，
# 从右到左默认-1开始，下标可以为可为空，表示取到头或尾。
# 加号 + 是列表连接运算符，* 是重复操作，如下实例
# 实例（python 2.0+）




#!/user/bin/python
#_*_ coding: utf8 _*_
list = [ 'runoob',786,2.23,'john',70.2 ]
tinylist = [ 123 , 'john' ]

print list  #输出完整列表
print list[0] #输出列表的第一个元素
print list[1:3] #输出第二个至第三个元素
print list[2:] #输出从第三个开始至列表未尾的所有元素
print tinylist * 2 #输出列表两次
print list + tinylist #打印组合的列表





































