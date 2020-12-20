from tkinter import *
from tkinter.messagebox import *

def show_answer():
    AnsK = int(float(num1.get())) * 1.60934
    AnsM = int(float(num2.get())) * 0.6213711
    blank.insert(0, AnsK)
    blank.insert(0, " / ")
    blank.insert(0, AnsM)


main = Tk()
main.title("Conversion")
Label(main, text = "Enter kilometers:").grid(row=0)
Label(main, text = "Enter miles:").grid(row=1)
Label(main, text = "Kilometers & Miles after conversion:").grid(row=2)


num1 = Entry(main)
num2 = Entry(main)
blank = Entry(main)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
blank.grid(row=2, column=1)


Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(main, text='Show', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)

mainloop()