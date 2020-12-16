#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
s1=str(random.randint(1,100))                           #s1=随机
print("这是一个位于1--100之间的数，你只能猜5次")
for s2 in range(1,6):                      #s2=猜的数字
    g1=input("请输入猜测的数")           #g1=猜的人
    if not g1.isdigit():
        print("请输入数字！！！")
    elif g1<s1:
        print("太小了")
    elif g1>s1:
        print("太大了")
    else:
        break
if (g1==s1):
    print("猜对了")
else:
    print("游戏结束")


# In[ ]:





# In[ ]:




