#!/usr/bin/env python
# coding: utf-8

# In[ ]:


file = open('C:\\Users\\jihao\\Desktop\\学号.csv','r')
lines = file.readlines()
students = {}
for line in lines:
    tmp_list = line.split(',')
    xuehao = tmp_list[0]
    xingming = tmp_list[1]
    students[xuehao] = xingming
    
    print(students)
import random

num = input("请输入你要抽取的人数")
xuehao_list = random.sample(students.keys(),num)
xuehao_list
for xuehao in xuehao_list:
    print(students[xuehao])

