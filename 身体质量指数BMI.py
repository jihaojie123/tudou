#!/usr/bin/env python
# coding: utf-8

# In[ ]:



class BMI:
    
    def __init__(self,name,age,weight,high):
        self.name=name
        self.age=age
        self.weight=weight
        self.high=high
       
        bmi=self.weight/(self.high**2)
        
        
        
        
        health=input("输入BMI值得到健康状态：")
        if health<=18.5:
            print("偏瘦")
        elif 18.5<health<=25.5:
            print("正常")
        elif 25.5<health<=30:
            print("偏胖")
        else:
            print("肥胖")
       
            
            
            
    def say_age(self):
        print("年龄是{n}.format(n=self.age)")
    def say_weight(self):
        print("体重是{m}.format(m=self.weight)")
    def say_high(self):
        print("身高是{b}.format(b=self.high)")
    def say_bmi(self):
        print("BMI值是{v}.format(v=self.bmi)")
    
    
    
    
    
zhangsan=BMI("张三",31,78,1.80)

  
        
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





