#!/usr/bin/env python
# coding: utf-8

# In[ ]:


del move(players,step):
     num=step-1
    while num > 0:
        tmp = list1.pop(0)
        list1.append(tmp)
        num = num-1
    return players
def play(players,step,alive):
    
    
    """
    模拟约瑟夫游戏的函数：
    input：
    players：参加游戏的人数
    step：数到step人数的人淘汰
    alive：幸存人数，即游戏结束
    
    output：
    返回一个列表，列表中元素为幸存者编号
    """
    
    
    #生成一个列表，从[1.......players]


    list1=[i for i in range(1,players+1)]
    
    
    #进入游戏循环，数到step淘汰，step之前的移到后面
    #游戏结束条件：列表剩余人数小于alive


    while len(list1)>alive:
    
    
    #移动step前的元素到列表末尾
    #将step的元素删除
    list1.pop(0)                  #此时的step元素在列表第一个位置，使用pop（0）从列表删除
    return list1

