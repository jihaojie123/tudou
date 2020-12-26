

```python
import tkinter
import random
root=tkinter.Tk()
root.title('猜数字')
root['height']=300
root['width']=300
s1=int(random.randint(1,100))  

def caishuzi():
    for s2 in range(1,6):
        s2=0
        cai=int(shuzi.get())
    try:
       
        if s2==5:
            label2['text']='超过五次，游戏结束'
            shuzi.delete(0,'end')
        elif cai<s1:
            label2['text']='太小了'
            s2+=1
            shuzi.delete(0,'end')
        elif cai>s1:
            label2['text']='太大了'
            s2+=1
            shuzi.delete(0,'end')
        elif cai==s1:
            label2['text']='猜中了'
            s2+=1
            shuzi.delete(0,'end')
    except:
        label1['text']='请输入正确数字'
        print('请输入正确数字')
        
def answer():
    s1=random.randint(1,100)     
    
    




label1=tkinter.Label(root,text='请输入你猜测的数字')
label1.place(x=30,y=10,width=200,height=100)

label2=tkinter.Label(root,text='. ')
label2.place(x=100,y=150,width=200,height=100)

button1 = tkinter.Button(root,text='点击',command=caishuzi)
button1.place(x=30,y=250,height=30,width=80)

button2 = tkinter.Button(root,text='答案',command=answer)
button2.place(x=30,y=200,height=30,width=80)


shuzi=tkinter.StringVar(root)
entry1=tkinter.Entry(root,width=150,textvariable=shuzi)
entry1.place(x=30,y=70,width=100,height=40)









root.mainloop()
```

    请输入正确数字
    请输入正确数字
    


```python

```
