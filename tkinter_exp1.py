from tkinter import *
from tkinter.messagebox import *

def show_answer():

	if num1.get() != '' and num2.get() != '':
		AnsK = int(float(num1.get())) * 1.60934
		AnsM = int(float(num2.get())) * 0.6213711
		blank.insert(0, AnsK)
		blank.insert(0, " / ")
		blank.insert(0, AnsM)
	else: blank.insert(0, "The Kilometers and Miles must NOT be Empty or String")

def reset():

	num1.delete(0, END)
	num2.delete(0, END)
	blank.delete(0, END)


main = Tk()
#main.geometry("400x400")

main.title("Conversion")
Label(main, text = "Enter kilometers:").grid(row=0)
Label(main, text = "Enter miles:").grid(row=1)
Label(main, text = "Kilometers & Miles after conversion:").grid(row=2)


num1 = Entry(main)
num2 = Entry(main)
blank = Entry(main)
blank.grid(row=2,column=1,padx=120,ipadx=120,pady=5,ipady=5)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
blank.grid(row=2, column=1)



Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(main, text='Show', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)
Button(main, text='Reset', command=reset).grid(row=4, column=2, sticky=W, pady=4)

mainloop()