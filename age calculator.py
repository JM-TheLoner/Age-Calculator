from tkinter import *  # type: ignore
from datetime import date

root=Tk()
root.geometry("600x600")
root.title("Age Calculator")
root.resizable(False,False)
root.config(bg="white")

def calculate():
    n = name.get()
    y = int(year.get())
    m = int(month.get())
    d = int(day.get())

    today=date.today()
    birthdate=date(year=y, month=m, day=d)

    after = today.year-birthdate.year
    before = after - 1

    if birthdate.month<today.month:
        if today.day>=birthdate.day:
            months = (today.month-birthdate.month)
        else:
            months=0
    elif birthdate.month>today.month:
        months = 12-(birthdate.month-today.month)
    elif birthdate.month==today.month:
        if today.day>=birthdate.day:
            months=0
        else:
            months=11

    days = abs(birthdate.day-today.day)        

    if today.month > birthdate.month:
        age = after
    if today.month < birthdate.month:
        age = before
    if today.month == birthdate.month:
        if today.day < birthdate.day:
            age = before
        else:
            age = after

    

    open = (f"{n} you are {age} years {months} months and {days} days old")  # type: ignore
    spell.config(text=open)

imag=PhotoImage(file="Py_Project Directory\Age calculator  .png")   # type: ignore
photo=Label(image=imag)
photo.place(x=210,y=20)

icon = root.iconphoto(False, imag)
 
Label(root, text="Name", font=("calibri", 12)).place(x=100, y=230)
name=Entry(width=30, font=("arial", 13), bd=0, border=3, bg="white")
name.place(x=180, y=230)

Label(root, text="Year", font=("calibri", 12)).place(x=100, y=290)
year=Entry(width=30, font=("arial", 13), bd=0, border=3, bg="white")
year.place(x=180, y=290)

Label(root, text="Month", font=("calibri", 12)).place(x=100, y=350)
month=Entry(width=30, font=("arial", 13), bd=0, border=3, bg="white")
month.place(x=180, y=350)

Label(root, text="Day", font=("calibri", 12)).place(x=100, y=410)
day=Entry(width=30, font=("arial", 13), bd=0, border=3, bg="white")
day.place(x=180, y=410)

Button(root, text="Calculate Age", font=("calibri", 12), bg="black", fg="white", command=calculate).place(x=180,y=470)

spell = Label(root, fg="black", font=("calibri", 13))
spell.place(x=180, y=500)

mainloop()