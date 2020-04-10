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


Students = [ "Name" , "Last Name" , "StudentID" , "Programme" , "Address" , "DOB" , "ZIP" , "City" , "Email" , "Counselor" , "Start Year" , "Gender" , "ProgrammeID" ]
Employees = [ "EmployeesID" , "Name" , "Last Name" , "Title" , "Department" , "Salary" , "FromDate" , "ToDate" , "DOB" , "Address" , "ZIP" , "City" , "Email" , "Gender" , "Counselor"]
Courses = ["Course Name", "ProgrammeID" , "Description" , "Lecturer" , "ECTS"]
Programmes = ["ProgrammeID" , "Degree" , "Name" , "Description" , "Language" , "Duration" , "Location" , "Tuition Fee"]
Results = ["Exam" , "Student" , "Passed"]
Exams=["Course" , "Room" , "Resit" , "Date" , "Time" ]

menubar = tk.Menu(window)
def view(table):
    global f
    f.destroy()
    f = tk.Frame(window)
    f.pack()
    tv = ttk.Treeview(f, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13 ,14,15) , show="headings" , height="50" )
    for i in range(15):
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

def addnew(table):
    newwin = tk.Toplevel()
    newwin.geometry("500x550")
    newwin.title("Add " + table)

    container = ttk.Frame(newwin)
    canvas = tk.Canvas(container , height=500,width=400)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    if table == "Students":

        label1 = tk.Label(scrollable_frame, text="Name")
        entry1 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry1.pack()

        label1 = tk.Label(scrollable_frame, text="Last Name")
        entry2 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry2.pack()

        label1 = tk.Label(scrollable_frame, text="StudentID")
        entry3 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry3.pack()

        label1 = tk.Label(scrollable_frame, text="Programme")
        entry4 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry4.pack()

        label1 = tk.Label(scrollable_frame, text="Address")
        entry5 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry5.pack()

        label1 = tk.Label(scrollable_frame, text="DOB")
        entry6 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry6.pack()

        label1 = tk.Label(scrollable_frame, text="ZIP")
        entry7 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry7.pack()

        label1 = tk.Label(scrollable_frame, text="City")
        entry8 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry8.pack()

        label1 = tk.Label(scrollable_frame, text="Email")
        entry9 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry9.pack()

        label1 = tk.Label(scrollable_frame, text="Counselor")
        entry10 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry10.pack()

        label1 = tk.Label(scrollable_frame, text="Start Year")
        entry11 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry11.pack()

        label1 = tk.Label(scrollable_frame, text="Gender")
        entry12 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry12.pack()

        label1 = tk.Label(scrollable_frame, text="ProgrammeID")
        entry13 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry13.pack()

        def fetch():
            print(entry1.get())
            print(entry2.get())
            print(entry3.get())
            print(entry4.get())
            print(entry5.get())
            print(entry6.get())
            print(entry7.get())
            print(entry8.get())
            print(entry9.get())
            print(entry10.get())
            print(entry11.get())
            print(entry12.get())
            print(entry13.get())

    elif table == "Employees":

        label1 = tk.Label(scrollable_frame, text="EmployeesID")
        entry1 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry1.pack()

        label1 = tk.Label(scrollable_frame, text="Name")
        entry2 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry2.pack()

        label1 = tk.Label(scrollable_frame, text="Last Name")
        entry3 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry3.pack()

        label1 = tk.Label(scrollable_frame, text="Title")
        entry4 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry4.pack()

        label1 = tk.Label(scrollable_frame, text="Department")
        entry5 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry5.pack()

        label1 = tk.Label(scrollable_frame, text="Salary")
        entry6 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry6.pack()

        label1 = tk.Label(scrollable_frame, text="From Date")
        entry7 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry7.pack()

        label1 = tk.Label(scrollable_frame, text="To Date")
        entry8 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry8.pack()

        label1 = tk.Label(scrollable_frame, text="DOB")
        entry9 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry9.pack()

        label1 = tk.Label(scrollable_frame, text="Adress")
        entry10 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry10.pack()

        label1 = tk.Label(scrollable_frame, text="ZIP")
        entry11 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry11.pack()

        label1 = tk.Label(scrollable_frame, text="City")
        entry12 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry12.pack()

        label1 = tk.Label(scrollable_frame, text="Email")
        entry13 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry13.pack()

        label1 = tk.Label(scrollable_frame, text="Gender")
        entry14 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry14.pack()

        label1 = tk.Label(scrollable_frame, text="Counselor")
        entry15 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry15.pack()

        def fetch():
            print(entry1.get())
            print(entry2.get())
            print(entry3.get())
            print(entry4.get())
            print(entry5.get())
            print(entry6.get())
            print(entry7.get())
            print(entry8.get())
            print(entry9.get())
            print(entry10.get())
            print(entry11.get())
            print(entry12.get())
            print(entry13.get())
            print(entry14.get())
            print(entry15.get())

    
    
    elif table == "Programmes":

        label1 = tk.Label(scrollable_frame, text="ProgrammeID")
        entry1 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry1.pack()

        label1 = tk.Label(scrollable_frame, text="Degree")
        entry2 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry2.pack()

        label1 = tk.Label(scrollable_frame, text="Name")
        entry3 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry3.pack()

        label1 = tk.Label(scrollable_frame, text="Description")
        entry4 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry4.pack()

        label1 = tk.Label(scrollable_frame, text="Language")
        entry5 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry5.pack()

        label1 = tk.Label(scrollable_frame, text="Duration")
        entry6 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry6.pack()

        label1 = tk.Label(scrollable_frame, text="Location")
        entry7 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry7.pack()

        label1 = tk.Label(scrollable_frame, text="Tuition Fee")
        entry8 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry8.pack()

        def fetch():
            print(entry1.get())
            print(entry2.get())
            print(entry3.get())
            print(entry4.get())
            print(entry5.get())
            print(entry6.get())
            print(entry7.get())
            print(entry8.get())


    elif table == "Courses":

        label1 = tk.Label(scrollable_frame, text="Course Name")
        entry1 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry1.pack()

        label1 = tk.Label(scrollable_frame, text="ProgrammeID")
        entry2 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry2.pack()

        label1 = tk.Label(scrollable_frame, text="Description")
        entry3 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry3.pack()

        label1 = tk.Label(scrollable_frame, text="Lecturer")
        entry4 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry4.pack()

        label1 = tk.Label(scrollable_frame, text="ECTS")
        entry5 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry5.pack()

        def fetch():
            print(entry1.get())
            print(entry2.get())
            print(entry3.get())
            print(entry4.get())
            print(entry5.get())


    elif table == "Exams":

        label1 = tk.Label(scrollable_frame, text="Course")
        entry1 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry1.pack()

        label1 = tk.Label(scrollable_frame, text="Room")
        entry2 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry2.pack()

        label1 = tk.Label(scrollable_frame, text="Resit")
        entry3 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry3.pack()

        label1 = tk.Label(scrollable_frame, text="Date")
        entry4 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry4.pack()

        label1 = tk.Label(scrollable_frame, text="Time")
        entry5 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry5.pack()

        def fetch():
            print(entry1.get())
            print(entry2.get())
            print(entry3.get())
            print(entry4.get())
            print(entry5.get())

    elif table == "Results":

        label1 = tk.Label(scrollable_frame, text="Exam")
        entry1 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry1.pack()

        label1 = tk.Label(scrollable_frame, text="Student")
        entry2 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry2.pack()

        label1 = tk.Label(scrollable_frame, text="Passed")
        entry3 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry3.pack()

        def fetch():
            print(entry1.get())
            print(entry2.get())
            print(entry3.get())


    addbut = tk.Button(newwin , text="Add" , command=lambda: fetch())
    addbut.pack(side="bottom")

    
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
submenup.add_command(label="Students", command= lambda: addnew("Students"))
submenup.add_command(label="Teachers", command= lambda: addnew("Employees"))
submenup.add_command(label="Studies", command= lambda: addnew("Programmes"))
submenup.add_command(label="Courses", command= lambda: addnew("Courses"))
submenup.add_command(label="Exams", command= lambda: addnew("Exams"))
submenup.add_command(label="Results", command= lambda: addnew("Results"))
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