#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter 
import tkinter.messagebox


def BMI():
    tkinter.messagebox.showinfo(title="BMI",message=msgbox())

def msgbox():
    tizhong=float(weight.get())
    shengao=float(height.get())
    
    bmi_get=tizhong/(shengao**2)
    #b=round(bmi_get,1)
   
    if bmi_get < 18.5:
        result = ('偏瘦')
    elif 18.5 <= bmi_get <= 25:
        result = ('正常')
    elif 25 <= bmi_get <= 28:
        result = ('有点胖')
    elif 28 <= bmi_set <= 32:
        result = ('肥胖')
    
    healthy.set(result)

    
        
root=tkinter.Tk()
root['height']=300
root['width']=300



label1=tkinter.Label(root,text="身高m")
label1.place(x=10,y=40,width=50,height=30)

label2=tkinter.Label(root,text="体重kg")
label2.place(x=10,y=80,width=50,height=30)

button = tkinter.Button(root,text='计算BMI',command=msgbox)
button.place(x=10,y=250,height=30,width=80)

weight=tkinter.StringVar(root)
entryBmi=tkinter.Entry(root,width=150,textvariable=weight)
entryBmi.place(x=70,y=20,width=100,height=40)


height=tkinter.StringVar(root)
entryBmi=tkinter.Entry(root,width=150,textvariable=height)
entryBmi.place(x=70,y=70,width=100,height=40)




healthy=tkinter.StringVar(root)
entryBmi=tkinter.Entry(root,width=150,textvariable=healthy)
entryBmi.place(x=100,y=250,width=100,height=40)


root.mainloop()

