from tkinter import *


window=Tk()

l1=Label(window,text= "Product Id")
l1.grid(row=0,column=0)

l2=Label(window,text="Product name")
l2.grid(row=0,column=2)

l3=Label(window,text="Price")
l3.grid(row=1,column=0)

l4=Label(window,text="quantity")
l4.grid(row=1,column=2)

productid=StringVar()
e1=Entry(window,textvariable="productid")
e1.grid(row=0,column=1)

name=StringVar()
e2=Entry(window,textvariable="name")
e2.grid(row=0,column=3)

cost=StringVar()
e3=Entry(window,textvariable="cost")
e3.grid(row=1,column=1)

quantity=StringVar()
e4=Entry(window,textvariable="quantity")
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b2=Button(window,text="view products",width=12)
b2.grid(row=2,column=3)

b3=Button(window,text="search product",width=12)
b3.grid(row=3,column=3)

b4=Button(window,text="Add new",width=12)
b4.grid(row=4,column=3)

b5=Button(window,text="update list",width=12)
b5.grid(row=5,column=3)

b6=Button(window,text="delete selected",width=12)
b6.grid(row=6,column=3)

b7=Button(window,text="close manager",width=12)
b7.grid(row=7,column=3)

window.mainloop()
