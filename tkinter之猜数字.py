#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter
import random


# In[7]:


root=tkinter.Tk()
root.title('猜数字')
root['height']=300
root['width']=300
s1=str(random.randint(1,100))  


def caishuzi():
    for s2 in range(1,6):
        a=str(shuzi)
        if a<s1:
            result="太小了"
        elif a>s1:
            result="太大了"
        else:
            result="游戏结束"
            continue
       
        if (a==s1):
            result="猜对了"
        else:
            result="游戏结束"
        shuzi.set(result)


label1=tkinter.Label(root,text='请输入你猜测的数字')
label1.place(x=30,y=10,width=200,height=100)

button = tkinter.Button(root,text='点击',command=caishuzi)
button.place(x=30,y=250,height=30,width=80)

shuzi=tkinter.StringVar(root)
entryBmi=tkinter.Entry(root,width=150,textvariable=button)
entryBmi.place(x=30,y=70,width=100,height=40)









root.mainloop()


# In[ ]:




