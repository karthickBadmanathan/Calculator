from tkinter import *  
root =Tk()
root.title ("simple calucluator")
e = Entry(width=35,borderwidth=5,fg="blue",bg="white") 
e.grid(row=0, column=0, columnspan=3)

def ButtonClick(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number)) 

def ButtonClear():
    e.delete(0,END)
 
def ButtonAdd():
    global f_num
    global math
    math=1
    firstnumber=e.get()
    f_num=int(firstnumber)
    e.delete(0,END)
    
def ButtonSub():
    global f_num
    global math
    math=2
    firstnumber=e.get()
    f_num=int(firstnumber)
    e.delete(0,END)
    
def ButtonMul():
    global f_num
    global math
    math=3
    firstnumber=e.get()
    f_num=int(firstnumber)
    e.delete(0,END)
    
def ButtonDiv():
    global f_num
    global math
    math=4
    firstnumber=e.get()
    f_num=int(firstnumber)
    e.delete(0,END)    

def ButtonEqual():
   secondnumber=e.get()
   e.delete(0,END)
   
   if math==1:
      e.insert(0, f_num+int(secondnumber))
      
   elif math==2:
        e.insert(0, f_num-int(secondnumber))
      
   elif math==3:
        e.insert(0, f_num*int(secondnumber))
      
   elif math==4:
        e.insert(0, f_num/int(secondnumber))

Button1 = Button(text=1, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(1)).grid(row=1,column=0)
Button2 = Button(text=2, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(2)).grid(row=1,column=1)
Button3 = Button(text=3, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(3)).grid(row=1,column=2)

Button4 = Button(text=4, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(4)).grid(row=2,column=0)
Button5 = Button(text=5, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(5)).grid(row=2,column=1)
Button6 = Button(text=6, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(6)).grid(row=2,column=2)

Button7 = Button(text=7, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(7)).grid(row=3,column=0)
Button8 = Button(text=8, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(8)).grid(row=3,column=1)
Button9 = Button(text=9, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(9)).grid(row=3,column=2)

Button0 = Button(text=0, padx=40,pady=20,fg="blue",bg="black", command=lambda:ButtonClick(0)).grid(row=4,column=0)
ButtonClear = Button(text="clear", padx=78,pady=20,fg="white",bg="black",command=ButtonClear).grid(row=4,column=1,columnspan=2)

ButtonAdd = Button(text="+", padx=40,pady=20,fg="white",bg="black",command=ButtonAdd).grid(row=5,column=0)
ButtonSub = Button(text="-", padx=40,pady=20,fg="white",bg="black",command=ButtonSub).grid(row=5,column=1)
ButtonMul = Button(text="*", padx=40,pady=20,fg="white",bg="black",command=ButtonMul).grid(row=5,column=2)

ButtonDiv = Button(text="/", padx=40,pady=20,fg="white",bg="black",command=ButtonDiv).grid(row=6,column=0)
ButtonEqual = Button(text="=", padx=88,pady=20,fg="white",bg="black",command=ButtonEqual).grid(row=6,column=1,columnspan=2)

root.mainloop()
