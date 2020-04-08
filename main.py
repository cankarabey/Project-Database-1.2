import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image


db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2501',
    database='inh'
)
mydb = db_connection.cursor()
sql_statement= 'SELECT * FROM '

window = tk.Tk()
window.geometry("1200x600")
window.title("INH Database")

window.configure(background='grey')

f = tk.Frame(window)
f.pack()

path = "Inholland.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(f, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")


Students = [ "Name" , "Last Name" , "StudentID" , "Programme" , "Address" , "DOB" , "ZIP" , "City" , "Email" , "Courcelor" , "Start Year" , "Gender" , "ProgrammeID" ]
Employees = [ "EmployeesID" , "Name" , "Last Name" , "Title" , "Department" , "Salary" , "FromDate" , "ToDate" , "DOB" , "Address" , "ZIP" , "City" , "Email" , "Gender"]
Courses = ["Course Name" , "ProgrammeID" , "Lecturer" , "ECTS"]
Programmes = ["ProgrammeID" , "Degree" , "Name" , "Duration" , "Location" , "Tuition Fee"]
Results = ["Exam" , "Student" , "Passed"]
Exams=["Course" , "Room" , "Resit" , "Date" , "Time" ]

menubar = tk.Menu(window)
def view(table):
    global f
    f.destroy()
    f = tk.Frame(window)
    f.pack()
    tv = ttk.Treeview(f, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13 ,14) , show="headings" , height="50" )
    for i in range(14):
        tv.column(i , width=110 , anchor="center")
    tv.pack()
    count = 0
    if table == "Students":
        for x in Students:
            count +=1
            tv.heading(count , text=x)
    elif table == "Employees":
        for x in Employees:
            count +=1
            tv.heading(count , text=x)
    elif table == "Programmes":
        for x in Programmes:
            count +=1
            tv.heading(count , text=x)
    elif table == "Results":
        for x in Results:
            count +=1
            tv.heading(count , text=x)
    elif table == "Exams":
        for x in Exams:
            count +=1
            tv.heading(count , text=x)
    elif table == "Courses":
        for x in Courses:
            count +=1
            tv.heading(count , text=x)
    mydb.execute(sql_statement + table)
    output = mydb.fetchall()
    for x in output:
        tv.insert('', 'end', values=x)

def addnew():
    newwin = tk.Toplevel()
    L1 = tk.Label(newwin, text="User Name")
    L1.pack()
    E1 = tk.Entry(newwin, bd =5, width=100)
    E1.pack()
    L2 = tk.Label(newwin, text="User Name")
    L2.pack()
    E2 = tk.Entry(newwin, bd =5, width=100)
    E2.pack()
    addbut = tk.Button(newwin , text="Add")
    addbut.pack()



filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Students",command=lambda: view("Students"))
filemenu.add_command(label="Teachers",command=lambda: view("Employees"))
filemenu.add_command(label="Programmes" ,command=lambda: view("Programmes"))
filemenu.add_command(label="Courses" ,command=lambda: view("Courses"))
filemenu.add_command(label="Exams" , command=lambda: view("Exams"))
filemenu.add_command(label="Results",command=lambda: view("Results"))

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="View", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)

submenup = tk.Menu(window)
submenup.add_command(label="Students", command=addnew)
submenup.add_command(label="Teachers")
submenup.add_command(label="Studies")
submenup.add_command(label="Courses")
submenup.add_command(label="Exams")
submenup.add_command(label="Results")
editmenu.add_cascade(label='Add', menu=submenup, underline=0)


editmenu.add_separator()

submenum = tk.Menu(window)
submenum.add_command(label="Students")
submenum.add_command(label="Teachers")
submenum.add_command(label="Studies")
submenum.add_command(label="Courses")
submenum.add_command(label="Exams")
submenum.add_command(label="Results")
editmenu.add_cascade(label='Delete', menu=submenum, underline=0)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
helpmenu.add_command(label="Manual")
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
window.mainloop()