#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class BMI:
    
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        self.bmi=self.weight/(self.height*self.height)
    def get_name(self):
        #print()
        return self.name
    
    def get_bmi(self):
        
         return self.bmi
    
    def get_status(self):
        
        if self.bmi<18.5:
            self.status="偏瘦"
        
        else:
            self.status="正常"


# In[ ]:





# In[ ]:




