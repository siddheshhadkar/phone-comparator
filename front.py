from tkinter import *


root=Tk()
root.title("Python Project")
root.resizable(width=False,height=False)
root.geometry('600x400')



def disp():
    if(var1.get()=='a'):                  
        t1.set(a['name'])
        r1.set(a['ram'])
        s1.set(a['storage'])
        c1.set(a['color'])
        p1.set(a['price'])
    if(var1.get()=='b'):                  
        t1.set(b['name'])
        r1.set(b['ram'])
        s1.set(b['storage'])
        c1.set(b['color'])
        p1.set(b['price'])
    disp2()
def disp2():
    if(var2.get()=='c'):                  
        t2.set(c['name'])
        r2.set(c['ram'])
        s2.set(a['storage'])
        c2.set(a['color'])
        p2.set(a['price'])
    if(var2.get()=='d'):                  
        t2.set(d['name'])
        r2.set(d['ram'])
        s2.set(d['storage'])
        c2.set(d['color'])
        p2.set(d['price'])
        



#Option Menu 1


mylist=['a','b']
var1=StringVar()
var1.set("Select Mobile 1")
mymenu=OptionMenu(root,var1,*mylist)
mymenu.grid(row=1,column=2)
mymenu.config(font=('calibri',(10)),bg='white',width=12)
mymenu['menu'].config(font=('calibri',(10)),bg='white')








#Option Menu 2


mylist2=['c','d']
var2=StringVar(root)
var2.set("Select Mobile 2")
mymenu=OptionMenu(root,var2,*mylist2)
mymenu.grid(row=1,column=3)
mymenu.config(font=('calibri',(10)),bg='white',width=12)
mymenu['menu'].config(font=('calibri',(10)),bg='white')







a={'name':'Mi','ram':'4','storage':'64','color':'white','price':'11'}
b={'name':'Vivo','ram':'5','storage':'128','color':'black','price':'12'}
c={'name':'Samsung','ram':'6','storage':'256','color':'gold','price':'13'}
d={'name':'Sony','ram':'7','storage':'122','color':'pink','price':'14'}



    




#Function to set the values of labels
'''
nm=StringVar()
nm.set("Name")
def name():
    global nm
    if (var1.get()=='a'):
        nm.set(a['name'])
    elif (var1.get()=='b'):
        nm.set(b['name'])


'''






#declaring labels

lwelcome=Label(root,text="WELCOME TO MOBILE COMPARISON APPLICATION",fg="black")
lname=Label(root,text="NAME",fg="red")
lram=Label(root,text="RAM",fg="red")
lstorage=Label(root,text="STORAGE",fg="red")
lcolor=Label(root,text="COLOUR",fg="red")
lprice=Label(root,text="PRICE",fg="red")






#Declaring text variables

t1=StringVar()
t2=StringVar()
r1=StringVar()
r2=StringVar()
s1=StringVar()
s2=StringVar()
c1=StringVar()
c2=StringVar()
p1=StringVar()
p2=StringVar()



#Entries to be fetched from the DB

name1=Label(root,text="name1",textvariable=t1)
name2=Label(root,text="name2",textvariable=t2)
ram1=Label(root,text="ram1",textvariable=r1)
ram2=Label(root,text="ram2",textvariable=r2)
store1=Label(root,text="store1",textvariable=s1)
store2=Label(root,text="store2",textvariable=s2)
col1=Label(root,text="col1",textvariable=c1)
col2=Label(root,text="col2",textvariable=c2)
price1=Label(root,text="pr1",textvariable=p1)
price2=Label(root,text="pr2",textvariable=p2)


#For Image

'''

pic1=PhotoImage(file="mob.ppm")
lpic1=Label(root,image=pic1)
lpic1.grid(row=8,column=5)

'''





#Compare button

button=Button(root,text="COMPARE",command=disp)







#Placing the Labels using grid layout

lwelcome.grid(row=0,column=3)
lname.grid(row=3,column=1)
lram.grid(row=4,column=1)
lstorage.grid(row=5,column=1)
lcolor.grid(row=6,column=1)
lprice.grid(row=7,column=1)


#Placing the Entry Labels using grid layout

name1.grid(row=3,column=2)
name2.grid(row=3,column=3)
ram1.grid(row=4,column=2)
ram2.grid(row=4,column=3)
store1.grid(row=5,column=2)
store2.grid(row=5,column=3)
col1.grid(row=6,column=2)
col2.grid(row=6,column=3)
price1.grid(row=7,column=2)
price2.grid(row=7,column=3)





#PLACING SHOW BUTTON




button.grid(row=8,column=3)







root.mainloop()
