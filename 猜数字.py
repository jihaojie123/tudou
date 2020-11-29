#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
s1=random.randint(1,100)                           #s1=随机
print("这是一个位于1--100之间的数，你只能猜5次")
for s2 in range(1,6):                      #s2=猜的数字
    g1=input("请输入猜测的数")           #g1=猜的人
    if g1.isdigit():
        a=int()
    else:
        print("你输入的不是数字")
    if a==0:
        break
    if a<s1:
        print("太小了")
    elif a>s1:
        print("太大了")
    else:
        break
if (a==s1):
    print("猜对了")
else:
    print("游戏结束")


# In[ ]:




