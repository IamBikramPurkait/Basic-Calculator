# simple Calculator using tkinter module
# Author : Bikram Purkait 

# import tkinter module
from tkinter import *
root = Tk()
root.title("Calculator")    # set the title as Calculator
root.resizable(False,False)
icon_photo=PhotoImage(file='icon.png')
root.iconphoto(False,icon_photo)

# create a entry for taking number from user and packing with grid method
e=Entry(root,relief=RAISED,bd=3,bg="#ffe6e6",font=('Helvetica', 15 ,'bold'))
e.grid(row=0,column=0,columnspan=3,sticky=NSEW)


math = None       # declare global variable with NONE
f_num = None

# create function for buttion click
def button(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

# create function for clear
def button_clear():
	e.delete(0, END)

# create function for addition
def button_add():
	first_number = e.get()
	global f_num        # create a local variable that is linked to the global variable
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

# create function for result or equal
def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

# create function for subtraction
def button_subtraction():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

# create function for multiplication
def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

# create function for division
def button_division():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)

# create button and packing with grid method
btn7=Button(root,padx=30,pady=30,text="7",relief=RAISED,bd=2,command=lambda: button(7),bg="#00ffff",font=('Helvetica', 15 ,'bold'))
btn7.grid(row=1,column=0)
btn8=Button(root,padx=30,pady=30,text="8",relief=RAISED,bd=2,command=lambda: button(8),bg="#80ff00",font=('Helvetica', 15 ,'bold')).grid(row=1,column=1)
btn9=Button(root,padx=30,pady=30,text="9",relief=RAISED,bd=2,command=lambda: button(9),bg="#00ff80",font=('Helvetica', 15 ,'bold')).grid(row=1,column=2)

btn4=Button(root,padx=30,pady=30,text="4",relief=RAISED,bd=2,command=lambda: button(4),bg="#bf00ff",font=('Helvetica', 15 ,'bold')).grid(row=2,column=0)
btn5=Button(root,padx=30,pady=30,text="5",relief=RAISED,bd=2,command=lambda: button(5),bg="#0080ff",font=('Helvetica', 15 ,'bold')).grid(row=2,column=1)
btn6=Button(root,padx=30,pady=30,text="6",relief=RAISED,bd=2,command=lambda: button(6),bg="#cc3333",font=('Helvetica', 15 ,'bold')).grid(row=2,column=2)

btn1=Button(root,padx=30,pady=30,text="1",relief=RAISED,bd=2,command=lambda: button(1),bg="#ff0080",font=('Helvetica', 15 ,'bold')).grid(row=3,column=0)
btn2=Button(root,padx=30,pady=30,text="2",relief=RAISED,bd=2,command=lambda: button(2),bg="#ffbf00",font=('Helvetica', 15 ,'bold')).grid(row=3,column=1)
btn3=Button(root,padx=30,pady=30,text="3",relief=RAISED,bd=2,command=lambda: button(3),bg="#00ff80",font=('Helvetica', 15 ,'bold')).grid(row=3,column=2)

btn0=Button(root,padx=30,pady=30,text="0",relief=RAISED,bd=2,command=lambda: button(0),bg="#ffb3b3",font=('Helvetica', 15 ,'bold')).grid(row=4,column=0)
btnequal=Button(root,padx=73,pady=30,text="=",relief=RAISED,bd=2,command=button_equal,bg="#808080",font=('Helvetica', 15 ,'bold')).grid(row=4,column=1,columnspan=2)
btnclear=Button(root,padx=32,pady=30,text="C",relief=RAISED,bd=2,command=button_clear,bg="#990000",font=('Helvetica', 15 ,'bold')).grid(row=0,column=3)

btnplus=Button(root,padx=33,pady=30,text="+",relief=RAISED,bd=2,command=button_add,bg="#ff0040",font=('Helvetica', 15 ,'bold')).grid(row=4,column=3)
btnsubtraction=Button(root,padx=34,pady=30,text="-",relief=RAISED,bd=2,command=button_subtraction,bg="#0040ff",font=('Helvetica', 16 ,'bold')).grid(row=3,column=3)
btnmultiply=Button(root,padx=33,pady=30,text="*",relief=RAISED,bd=2,command=button_multiply,bg="#bfff00",font=('Helvetica', 16 ,'bold')).grid(row=2,column=3)
btndivision=Button(root,padx=35,pady=30,text="/",relief=RAISED,bd=2,command=button_division,bg="#ff4d4d",font=('Helvetica', 16 ,'bold')).grid(row=1,column=3)

# create a mainloop for application run
root.mainloop()
