#!/usr/bin/env python
# coding: utf-8

# In[30]:


from collections import Counter


# In[31]:


f=open(r'C:\Users\jihao\Desktop\Walden.txt','r')


# In[32]:


lines=f.readlines()


# In[33]:


print(type(lines))


# In[34]:


print(lines)


# In[35]:


line=str(lines)


# In[36]:


a=list(line.split(' '))


# In[37]:


print(Counter(a))


# In[ ]:




