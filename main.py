import tkinter as tk
#from tkinter import *
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

sqlstudentnumbers = "SELECT StudentNumber FROM Students"
mydb.execute(sqlstudentnumbers)
studentnumberlist = mydb.fetchall()
studentids = []
for x in range(0,len(studentnumberlist)):
    studentids.append(str(studentnumberlist[x][0]))

loginscreen = tk.Tk()
loginscreen.geometry("500x150")
loginscreen.title("Login")
loginscreen.iconbitmap("inhLogo.ico")
labelusername = tk.Label(loginscreen, text="Username/Student No.")
entryusername = tk.Entry(loginscreen, bd =2, width=50)
labelusername.pack()
entryusername.pack()
labelpasswd = tk.Label(loginscreen, text="Password")
entrypasswd = tk.Entry(loginscreen,show="*", bd =2, width=50)
labelpasswd.pack()
entrypasswd.pack()
adminlogon = False
studentlogon = False
def open():
    global adminlogon , username , studentlogon
    username = entryusername.get()
    passwd = entrypasswd.get()
    if username == "admin" and passwd == "admin":
        loginscreen.destroy()
        adminlogon = True
        studentlogon = False
    elif username in studentids and passwd == '123':
        loginscreen.destroy()
        studentlogon = True
        adminlogon = False
    else:
        warningbox = tk.Toplevel(loginscreen)
        warningbox.geometry("200x50")
        warningbox.title("Warning")
        warningbox.iconbitmap("inhLogo.ico")
        warnlabel = tk.Label(warningbox,text="Wrong Username or Password.")
        warnlabel.pack()
        def warnclose():
            warningbox.destroy()
        closebutt = tk.Button(warningbox , text="OK" , command=warnclose)
        closebutt.pack()
        
loginbutton = tk.Button(loginscreen,text="Login" , command=open)
loginbutton.pack()
loginscreen.mainloop()

def viewstudent():#Student login info
    Resultsgrades = ["Exam", "ExamId", "Student", "Grade", "Passed"]
    studentwindow = tk.Tk()
    studentwindow.geometry("600x600")
    studentwindow.title("Your Grades")
    studentwindow.iconbitmap("inhLogo.ico")
    sgrades = ttk.Treeview(studentwindow, columns=(1,2,3,4,5) , show="headings" , height="50" )
    for i in range(6):
        sgrades.column(i , width=110 , anchor="center")
    sgrades.pack()
    count = 0
    for x in Resultsgrades:
        count +=1
        sgrades.heading(count , text=x)
    mydb.execute("SELECT * FROM RESULTS WHERE STUDENT = " + str(username))
    gradesfst = mydb.fetchall()
    for x in gradesfst:
        sgrades.insert('', 'end', values=x)
    studentwindow.mainloop()


window = tk.Tk()
window.geometry("1200x630")
window.title("INHOLLAND Database")
window.iconbitmap("inhLogo.ico")
window.configure(background='white')

f = tk.Frame(window)
f.pack()

path = "logo_inholland_academy.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(f, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")


Students = [ "FirstName" , "Last Name" , "StudentID" , "Programme" , "Address" , "DateOfBirth" , "ZIP" , "City" , "Email" , "Counselor" , "Start Year" , "Gender" , "ProgrammeID" ]
Employees = [ "EmployeesID" , "FirstName" , "Last Name" , "Title" , "Department" , "Salary" , "FromDate" , "ToDate" , "DOB" , "Address" , "ZIP" , "City" , "Email" , "Gender" , "Counselor"]
Courses = ["Course Name", "ProgrammeID" , "Description" , "Lecturer" , "ECTS"]
Programmes = ["ProgrammeID" , "Degree" , "Name" , "Description" , "Language" , "Duration" , "Location" , "Tuition Fee"]
Results = ["Exam" , "ExamID" , "Student" , "Grade" , "Passed"]
Exams=["Course" , "idExam" ,  "Room" , "Resit" , "Date" , "Time" ]

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
            count += 1
            tv.heading(count, text=x)

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
    newwin.iconbitmap("inhLogo.ico")

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
            studentname = entry1.get()
            studentlastname = entry2.get()
            studentid = int(entry3.get())
            studentprogramme = entry4.get()
            studentaddresss = entry5.get()
            studentdob = entry6.get()
            studentzip = entry7.get()
            studentcity = entry8.get()
            studentemail = entry9.get()
            studentcounselor = entry10.get()
            if studentcounselor == "":
                studentcounselor = None
            studentstartyear = entry11.get()
            studentgender = entry12.get()
            studentprogid = entry13.get()
            sql_insert = "INSERT INTO Students(FirstName , LastName, StudentNumber , Programme , Address , DateOfBirth , PostalCode , City , Email , Counselor , StartYear , Gender , ProgrammeID) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (studentname,studentlastname,studentid , studentprogramme , studentaddresss , studentdob , studentzip , studentcity , studentemail , studentcounselor , studentstartyear , studentgender , studentprogid)
            mydb.execute(sql_insert,values)
            db_connection.commit()
            newwin.destroy()
            view("Students")
    
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
            empid = int(entry1.get())
            empname = entry2.get()
            emplastname = entry3.get()
            emptitle = entry4.get()
            empdepartment = entry5.get()
            empsalary = int(entry6.get())
            empfromdate = entry7.get()
            emptodate = entry8.get()
            if emptodate == "":
                emptodate = None
            empdob = entry9.get()
            empaddress = entry10.get()
            empzip = entry11.get()
            empcity = entry12.get()
            empemail = entry13.get()
            empgender = entry14.get()
            empcounselor = entry15.get()
            if empcounselor == "":
                empcounselor = None
            sql_insert= "INSERT INTO Employees(idEmployees,FirstName,LastName,Title,Department,Salary,FromDate,ToDate,DateOfBirth,Address,PostalCode,City,Email,Gender,Counselor) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (empid , empname,emplastname,emptitle , empdepartment , empsalary , empfromdate , emptodate , empdob , empaddress , empzip , empcity , empemail , empgender , empcounselor)
            mydb.execute(sql_insert , values)
            db_connection.commit()
            newwin.destroy()
            view("Employees")

    
    
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
            programmeid = int(entry1.get())
            progdegree = entry2.get()
            progname = entry3.get()
            progdesc = entry4.get()
            proglang = entry5.get()
            progduration = int(entry6.get())
            proglocation = entry7.get()
            progfee = entry8.get()
            sql_insert = "INSERT INTO Programmes(idProgramme,Degree,ProgrammeName,Description,Language,Duration,ProgrammeLocation,TuitionFee) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (programmeid,progdegree,progname,progdesc,proglang,progduration,proglocation,progfee)
            mydb.execute(sql_insert,values)
            db_connection.commit()
            newwin.destroy()
            view("Programmes")


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
            coursename = entry1.get()
            courseprogid = int(entry2.get())
            coursedesc = entry3.get()
            courselec = int(entry4.get())
            courseects = int(entry5.get())
            sql_insert = "INSERT INTO Courses(CourseName,Programme,Description,LECTURER,ECTS) values(%s,%s,%s,%s,%s)"
            values = (coursename,courseprogid,coursedesc,courselec,courseects)
            mydb.execute(sql_insert,values)
            db_connection.commit()
            newwin.destroy()
            view("Courses")


    elif table == "Exams":

        label1 = tk.Label(scrollable_frame, text="Course")
        entry1 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry1.pack()

        label1 = tk.Label(scrollable_frame, text="idExam")
        entry22 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry22.pack()

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
            examcourse = entry1.get()
            examid = int(entry22.get())
            examroom = entry2.get()
            examresit = entry3.get()
            examdate = entry4.get()
            examtime = entry5.get()
            sql_insert = "INSERT INTO Exams(Course,idExam,Room,Resit,Date,Time) values(%s,%s,%s,%s,%s,%s)"
            values = (examcourse,examid,examroom,examresit,examdate,examtime)
            mydb.execute(sql_insert,values)
            db_connection.commit()
            newwin.destroy()
            view("Exams")

    elif table == "Results":

        label1 = tk.Label(scrollable_frame, text="Exam")
        entry1 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry1.pack()

        label1 = tk.Label(scrollable_frame, text="ExamID")
        entry12 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry12.pack()

        label1 = tk.Label(scrollable_frame, text="Student")
        entry2 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry2.pack()

        label1 = tk.Label(scrollable_frame, text="Passed")
        entry3 = tk.Entry(scrollable_frame, bd =2, width=50)
        label1.pack()
        entry3.pack()

        def fetch():
            resexam = entry1.get()
            reexamid = int(entry12.get())
            resstudent = int(entry2.get())
            respassed = entry3.get()
            sql_insert = "INSERT INTO Results(Exam,ExamID,Student,Passed) values(%s,%s,%s,%s)"
            values = (resexam,reexamid,resstudent,respassed)
            mydb.execute(sql_insert,values)
            db_connection.commit()
            newwin.destroy()
            view("Results")

    addbut = tk.Button(newwin , text="Add" , command=lambda: fetch())
    addbut.pack(side="bottom")


def remove(table):
    popup = tk.Toplevel(window)
    popup.geometry("300x300")
    popup.title("Delete " + table + " from DB")
    popup.iconbitmap("inhLogo.ico")
    
    if table == "Students":
        labeldel1 = tk.Label(popup , text="StudentID")
        entrydel1 = tk.Entry(popup , bd=2 , width=20)
        labeldel1.pack()
        entrydel1.pack()
        
        def finalrem():
            values = int(entrydel1.get())
            sql_delete = "DELETE FROM Students WHERE StudentNumber = %s "
            mydb.execute(sql_delete , (values,))
            db_connection.commit()
            popup.destroy()
            view("Students")

        def asking():
            askwin = tk.Toplevel(popup)
            askwin.geometry("300x200")
            askwin.title("Attention")
            askwin.iconbitmap("inhLogo.ico")
            def destroyask():
                askwin.destroy()
            sqltext = "SELECT FirstName,LastName,StudentNumber FROM Students WHERE StudentNumber = %s"
            value = int(entrydel1.get())
            mydb.execute(sqltext , (value,))
            labeltext = mydb.fetchall()
            labelask = tk.Label(askwin , text="Are you sure you want to delete the entry: " + str(labeltext[0][0] ) + str(labeltext[0][1] ) + str(labeltext[0][2])  +" from the DB.")
            labelask.pack()
            yesbutton = tk.Button(askwin , text="Yes" , command = lambda: finalrem())
            nobutton = tk.Button(askwin , text="No" , command = lambda: destroyask())
            yesbutton.pack()
            nobutton.pack()

    if table == "Employees":
        labeldel1 = tk.Label(popup , text="EmployeeID")
        entrydel1 = tk.Entry(popup , bd=2 , width=20)
        labeldel1.pack()
        entrydel1.pack()

        def finalrem():
            values = int(entrydel1.get())
            sql_delete = "DELETE FROM Employees WHERE idEmployees = %s "
            mydb.execute(sql_delete , (values,))
            db_connection.commit()
            popup.destroy()
            view("Employees")

        def asking():
            askwin = tk.Toplevel(popup)
            askwin.geometry("500x200")
            askwin.title("Attention")
            askwin.iconbitmap("inhLogo.ico")
            def destroyask():
                askwin.destroy()
            sqltext = "SELECT FirstName,LastName,idEmployees FROM Employees WHERE idEmployees = %s"
            value = int(entrydel1.get())
            mydb.execute(sqltext , (value,))
            labeltext = mydb.fetchall()
            labelask = tk.Label(askwin , text="Are you sure you want to delete the entry: " + str(labeltext[0][0] ) + str(labeltext[0][1] ) + str(labeltext[0][2])  +" from the DB.")
            labelask.pack()
            yesbutton = tk.Button(askwin , text="Yes" , command = lambda: finalrem())
            nobutton = tk.Button(askwin , text="No" , command = lambda: destroyask())
            yesbutton.pack()
            nobutton.pack()

    if table == "Programmes":
        labeldel1 = tk.Label(popup , text="ProgrammeID")
        entrydel1 = tk.Entry(popup , bd=2 , width=20)
        labeldel1.pack()
        entrydel1.pack()

        def finalrem():
            values = int(entrydel1.get())
            sql_delete = "DELETE FROM Programmes WHERE idProgramme = %s "
            mydb.execute(sql_delete , (values,))
            db_connection.commit()
            popup.destroy()
            view("Programmes")

        def asking():
            askwin = tk.Toplevel(popup)
            askwin.geometry("500x200")
            askwin.title("Attention")
            askwin.iconbitmap("inhLogo.ico")
            def destroyask():
                askwin.destroy()
            sqltext = "SELECT ProgrammeName,idProgramme FROM Programmes WHERE idProgramme = %s"
            value = int(entrydel1.get())
            mydb.execute(sqltext , (value,))
            labeltext = mydb.fetchall()
            labelask = tk.Label(askwin , text="Are you sure you want to delete the entry: " + str(labeltext[0][0] ) + str(labeltext[0][1] ) +" from the DB.")
            labelask.pack()
            yesbutton = tk.Button(askwin , text="Yes" , command = lambda: finalrem())
            nobutton = tk.Button(askwin , text="No" , command = lambda: destroyask())
            yesbutton.pack()
            nobutton.pack()
        
    if table == "Courses":
        labeldel1 = tk.Label(popup , text="Course Name")
        entrydel1 = tk.Entry(popup , bd=2 , width=20)
        labeldel1.pack()
        entrydel1.pack()

        def finalrem():
            cnamedel1 = entrydel1.get()
            sql_delete = "DELETE FROM Courses WHERE CourseName = %s "
            mydb.execute(sql_delete, (cnamedel1,))
            db_connection.commit()
            popup.destroy()
            view("Courses")

        def asking():
            askwin = tk.Toplevel(popup)
            askwin.geometry("500x200")
            askwin.title("Attention")
            askwin.iconbitmap("inhLogo.ico")
            def destroyask():
                askwin.destroy()
            sqltext = "SELECT CourseName FROM Courses WHERE CourseName = %s"
            value = entrydel1.get()
            mydb.execute(sqltext , (value,))
            labeltext = mydb.fetchall()
            labelask = tk.Label(askwin , text="Are you sure you want to delete the entry: " + str(labeltext[0][0])  +" from the DB.")
            labelask.pack()
            yesbutton = tk.Button(askwin , text="Yes" , command = lambda: finalrem())
            nobutton = tk.Button(askwin , text="No" , command = lambda: destroyask())
            yesbutton.pack()
            nobutton.pack()

    if table == "Results":
        
        labeldel1 = tk.Label(popup , text="Exam Name")
        entrydel1 = tk.Entry(popup , bd=2 , width=20)
        labeldel1.pack()
        entrydel1.pack()

        labeldel2 = tk.Label(popup , text="StudentID")
        entrydel2 = tk.Entry(popup , bd=2 , width=20)
        labeldel2.pack()
        entrydel2.pack()

        def finalrem():
            cnamedel1 = entrydel1.get()
            cnamedel2 = int(entrydel2.get())
            sql_delete = "DELETE FROM Results WHERE Exam = %s and STUDENT = %s "
            mydb.execute(sql_delete, (cnamedel1,cnamedel2))
            db_connection.commit()
            popup.destroy()
            view("Results")

        def asking():
            askwin = tk.Toplevel(popup)
            askwin.geometry("500x200")
            askwin.title("Attention")
            askwin.iconbitmap("inhLogo.ico")
            def destroyask():
                askwin.destroy()
            sqltext = "SELECT Exam , STUDENT FROM Results WHERE Exam = %s and STUDENT = %s"
            cnamedel1 = entrydel1.get()
            cnamedel2 = int(entrydel2.get())
            mydb.execute(sqltext , (cnamedel1,cnamedel2))
            labeltext = mydb.fetchall()
            labelask = tk.Label(askwin , text="Are you sure you want to delete the entry: " + str(labeltext) +" from the DB.")
            labelask.pack()
            yesbutton = tk.Button(askwin , text="Yes" , command = lambda: finalrem())
            nobutton = tk.Button(askwin , text="No" , command = lambda: destroyask())
            yesbutton.pack()
            nobutton.pack()

    if table == "Exams":
        labeldel1 = tk.Label(popup , text="Course Name")
        entrydel1 = tk.Entry(popup , bd=2 , width=20)
        labeldel1.pack()
        entrydel1.pack()
        labeldel2 = tk.Label(popup , text="Date")
        entrydel2 = tk.Entry(popup , bd=2 , width=20)
        labeldel2.pack()
        entrydel2.pack()

        def finalrem():
            cnamedel1 = entrydel1.get()
            cnamedel2 = entrydel2.get()
            sql_delete = "DELETE FROM Exams WHERE Course = %s and Date = %s "
            mydb.execute(sql_delete, (cnamedel1,cnamedel2))
            db_connection.commit()
            popup.destroy()
            view("Exams")

        def asking():
            askwin = tk.Toplevel(popup)
            askwin.geometry("500x200")
            askwin.title("Attention")
            askwin.iconbitmap("inhLogo.ico")
            def destroyask():
                askwin.destroy()
            sqltext = "SELECT Course,Date FROM Exams WHERE Course=%s and Date=%s"
            cnamedel1 = entrydel1.get()
            cnamedel2 = (entrydel2.get())
            mydb.execute(sqltext , (cnamedel1,cnamedel2))
            labeltext = mydb.fetchall()
            labelask = tk.Label(askwin , text="Are you sure you want to delete the entry: " + str(labeltext) +" from the DB.")
            labelask.pack()
            yesbutton = tk.Button(askwin , text="Yes" , command = lambda: finalrem())
            nobutton = tk.Button(askwin , text="No" , command = lambda: destroyask())
            yesbutton.pack()
            nobutton.pack()


    buttondel = tk.Button(popup , text="Delete" , command=lambda: asking())
    buttondel.pack()


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
submenum.add_command(label="Students" , command= lambda: remove("Students"))
submenum.add_command(label="Teachers" , command= lambda: remove("Employees"))
submenum.add_command(label="Studies" , command= lambda: remove("Programmes"))
submenum.add_command(label="Courses" , command= lambda: remove("Courses"))
submenum.add_command(label="Exams" , command= lambda: remove("Exams"))
submenum.add_command(label="Results" , command= lambda: remove("Results"))
editmenu.add_cascade(label='Delete', menu=submenum, underline=0)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
helpmenu.add_command(label="Manual")
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

def search():
    searchwindow = tk.Toplevel(window)
    searchwindow.geometry("600x150")
    searchwindow.title("Search")
    tabparent = ttk.Notebook(searchwindow)
    tabstudents = ttk.Frame(tabparent)
    tabemployees = ttk.Frame(tabparent)
    tabcourses = ttk.Frame(tabparent)
    tabexams = ttk.Frame(tabparent)
    tabresults = ttk.Frame(tabparent)
    tabprogrammes = ttk.Frame(tabparent)
    tabparent.add(tabstudents,text="Students")
    tabparent.add(tabemployees,text="Employees")
    tabparent.add(tabcourses,text="Courses")
    tabparent.add(tabexams,text="Exams")
    tabparent.add(tabresults,text="Results")
    tabparent.add(tabprogrammes,text="Programmes")
    tabparent.pack(expand=True,fill="both")

    searchbarstu = tk.Entry(tabstudents)
    searchlabelstu = tk.Label(tabstudents,text="Firstname/Lastname or Programme:")
    searchlabelstu.pack()
    searchbarstu.pack()

    def studentsearch():
        global f
        f.destroy()
        f = tk.Frame(window)
        f.pack()
        tv = ttk.Treeview(f, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13 ,14,15) , show="headings" , height="50" )
        for i in range(15):
            tv.column(i , width=110 , anchor="center")
        tv.pack()
        count = 0
        for x in Students:
            count +=1
            tv.heading(count , text=x)
        searched = searchbarstu.get()
        searched = "'" + searched + "%'"
        sqlsearch = "SELECT * FROM Students WHERE FirstName LIKE " + searched + " OR LastName LIKE " + searched + " OR Programme LIKE " + searched
        mydb.execute(sqlsearch)
        output = mydb.fetchall()
        for x in output:
            tv.insert('', 'end', values=x)
    seabutstu = tk.Button(tabstudents,text="Search" , command=lambda:studentsearch())
    seabutstu.pack()

    searchbaremp = tk.Entry(tabemployees)
    searchlabelemp = tk.Label(tabemployees,text="Firstname or Lastname:")
    searchlabelemp.pack()
    searchbaremp.pack()
    def empsearch():
        global f
        f.destroy()
        f = tk.Frame(window)
        f.pack()
        tv = ttk.Treeview(f, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13 ,14,15) , show="headings" , height="50" )
        for i in range(15):
            tv.column(i , width=110 , anchor="center")
        tv.pack()
        count = 0
        for x in Employees:
            count +=1
            tv.heading(count , text=x)
        searched = searchbaremp.get()
        searched = "'" + searched + "%'"
        sqlsearch = "SELECT * FROM Employees WHERE FirstName LIKE " + searched + " OR LastName LIKE " + searched 
        mydb.execute(sqlsearch)
        output = mydb.fetchall()
        for x in output:
            tv.insert('', 'end', values=x)
    seabutemp = tk.Button(tabemployees,text="Search" , command=lambda:empsearch())
    seabutemp.pack()

    searchbarcou = tk.Entry(tabcourses)
    searchlabelcou = tk.Label(tabcourses,text="Course name:")
    searchlabelcou.pack()
    searchbarcou.pack()
    def coursesearch():
        global f
        f.destroy()
        f = tk.Frame(window)
        f.pack()
        tv = ttk.Treeview(f, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13 ,14,15) , show="headings" , height="50" )
        for i in range(15):
            tv.column(i , width=110 , anchor="center")
        tv.pack()
        count = 0
        for x in Courses:
            count +=1
            tv.heading(count , text=x)
        searched = searchbarcou.get()
        searched = "'" + searched + "%'"
        sqlsearch = "SELECT * FROM Courses WHERE CourseName LIKE " + searched
        mydb.execute(sqlsearch)
        output = mydb.fetchall()
        for x in output:
            tv.insert('', 'end', values=x)
    seabutcou = tk.Button(tabcourses,text="Search" , command=lambda:coursesearch())
    seabutcou.pack()

    searchbarex = tk.Entry(tabexams)
    searchlabelex = tk.Label(tabexams,text="Name of Exam::")
    searchlabelex.pack()
    searchbarex.pack()
    def examsearch():
        global f
        f.destroy()
        f = tk.Frame(window)
        f.pack()
        tv = ttk.Treeview(f, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13 ,14,15) , show="headings" , height="50" )
        for i in range(15):
            tv.column(i , width=110 , anchor="center")
        tv.pack()
        count = 0
        for x in Exams:
            count +=1
            tv.heading(count , text=x)
        searched = searchbarex.get()
        searched = "'" + searched + "%'"
        sqlsearch = "SELECT * FROM Exams WHERE Course LIKE " + searched
        mydb.execute(sqlsearch)
        output = mydb.fetchall()
        for x in output:
            tv.insert('', 'end', values=x)
    seabutex = tk.Button(tabexams,text="Search" , command=lambda:examsearch())
    seabutex.pack()

    searchbarprog = tk.Entry(tabprogrammes)
    searchlabelprog = tk.Label(tabprogrammes,text="Programme Name:")
    searchlabelprog.pack()
    searchbarprog.pack()
    def searchprog():
        global f
        f.destroy()
        f = tk.Frame(window)
        f.pack()
        tv = ttk.Treeview(f, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13 ,14,15) , show="headings" , height="50" )
        for i in range(15):
            tv.column(i , width=110 , anchor="center")
        tv.pack()
        count = 0
        for x in Programmes:
            count +=1
            tv.heading(count , text=x)
        searched = searchbarprog.get()
        searched = "'" + searched + "%'"
        sqlsearch = "SELECT * FROM Programmes WHERE ProgrammeName LIKE " + searched 
        mydb.execute(sqlsearch)
        output = mydb.fetchall()
        for x in output:
            tv.insert('', 'end', values=x)
    seabutprog = tk.Button(tabprogrammes,text="Search" , command=lambda:searchprog())
    seabutprog.pack()

    searchbarres = tk.Entry(tabresults)
    searchlabel = tk.Label(tabresults,text="Student Number:")
    searchlabel.pack()
    searchbarres.pack()
    def searchresults():
        global f
        f.destroy()
        f = tk.Frame(window)
        f.pack()
        tv = ttk.Treeview(f, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13 ,14,15) , show="headings" , height="50" )
        for i in range(15):
            tv.column(i , width=110 , anchor="center")
        tv.pack()
        count = 0
        for x in Results:
            count +=1
            tv.heading(count , text=x)
        searched = searchbarres.get()
        sqlsearch = "SELECT * FROM Results WHERE STUDENT = " + searched
        mydb.execute(sqlsearch)
        output = mydb.fetchall()
        for x in output:
            tv.insert('', 'end', values=x)
    seabutres = tk.Button(tabresults,text="Search" , command=lambda:searchresults())
    seabutres.pack()

def edit():
    editwindow = tk.Toplevel(window)
    editwindow.geometry("500x200")
    editwindow.title("Edit")
    mb = tk.Menubutton(editwindow, text="Group" , relief='raised')
    mb.grid()
    mb.menu = tk.Menu(mb, tearoff = 0 )
    mb["menu"] = mb.menu
    def editstudents():
        label = tk.Label(editwindow,text="Enter Student Number:")
        entry = tk.Entry(editwindow)
        label.pack()
        entry.pack()
        def get():
            stuno = entry.get()
            sqledit = "SELECT * FROM Students WHERE StudentNumber = " + stuno
            mydb.execute(sqledit)
            student = mydb.fetchall()
            studentinfo = tk.Toplevel(window)
            studentinfo.title("Student Info")
            studentinfo.geometry("600x800")

            label1 = tk.Label(studentinfo, text="Name")
            entry1 = tk.Entry(studentinfo, bd =2, width=50)
            entry1.insert(0,student[0][0])
            label1.pack()
            entry1.pack()

            label1 = tk.Label(studentinfo, text="Last Name")
            entry2 = tk.Entry(studentinfo, bd =2, width=50)
            entry2.insert(0,student[0][1])
            label1.pack()
            entry2.pack()

            label1 = tk.Label(studentinfo, text="StudentID")
            entry3 = tk.Entry(studentinfo, bd =2, width=50)
            entry3.insert(0,student[0][2])
            label1.pack()
            entry3.pack()

            label1 = tk.Label(studentinfo, text="Programme")
            entry4 = tk.Entry(studentinfo, bd =2, width=50)
            entry4.insert(0,student[0][3])
            label1.pack()
            entry4.pack()

            label1 = tk.Label(studentinfo, text="Address")
            entry5 = tk.Entry(studentinfo, bd =2, width=50)
            entry5.insert(0,student[0][4])
            label1.pack()
            entry5.pack()

            label1 = tk.Label(studentinfo, text="DOB")
            entry6 = tk.Entry(studentinfo, bd =2, width=50)
            entry6.insert(0,student[0][5])
            label1.pack()
            entry6.pack()

            label1 = tk.Label(studentinfo, text="ZIP")
            entry7 = tk.Entry(studentinfo, bd =2, width=50)
            entry7.insert(0,student[0][6])
            label1.pack()
            entry7.pack()

            label1 = tk.Label(studentinfo, text="City")
            entry8 = tk.Entry(studentinfo, bd =2, width=50)
            entry8.insert(0,student[0][7])
            label1.pack()
            entry8.pack()

            label1 = tk.Label(studentinfo, text="Email")
            entry9 = tk.Entry(studentinfo, bd =2, width=50)
            entry9.insert(0,student[0][8])
            label1.pack()
            entry9.pack()

            label1 = tk.Label(studentinfo, text="Start Year")
            entry11 = tk.Entry(studentinfo, bd =2, width=50)
            entry11.insert(0,student[0][10])
            label1.pack()
            entry11.pack()

            label1 = tk.Label(studentinfo, text="Gender")
            entry12 = tk.Entry(studentinfo, bd =2, width=50)
            entry12.insert(0,student[0][11])
            label1.pack()
            entry12.pack()

            label1 = tk.Label(studentinfo, text="ProgrammeID")
            entry13 = tk.Entry(studentinfo, bd =2, width=50)
            entry13.insert(0,student[0][12])
            label1.pack()
            entry13.pack()

            def editdata():
                db_connection.commit()
                studentname = entry1.get()
                studentlastname = entry2.get()
                studentid = int(entry3.get())
                studentprogramme = entry4.get()
                studentaddresss = entry5.get()
                studentdob = entry6.get()
                studentzip = entry7.get()
                studentcity = entry8.get()
                studentemail = entry9.get()
                studentcounselor = None
                studentstartyear = entry11.get()
                studentgender = entry12.get()
                studentprogid = entry13.get()

                sqlupdate = "UPDATE Students SET FirstName = %s ,LastName = %s , Programme = %s, Address = %s , DateOfBirth = %s, PostalCode = %s, City = %s, Email = %s, Counselor = %s, StartYear = %s, Gender = %s, ProgrammeID = %s WHERE StudentNumber = " + stuno
                values = (studentname,studentlastname , studentprogramme , studentaddresss , studentdob , studentzip , studentcity , studentemail , studentcounselor , studentstartyear , studentgender , studentprogid)
                mydb.execute(sqlupdate,values)
                db_connection.commit()
                studentinfo.destroy()
                view("Students")

            editstudentbut = tk.Button(studentinfo,text="Edit",command = lambda:editdata())
            editstudentbut.pack()

        button = tk.Button(editwindow,text="Edit" , command = lambda:get())
        button.pack()

    def editemployees():
        label = tk.Label(editwindow , text="Enter EmployeeID: ")
        entry = tk.Entry(editwindow)
        label.pack()
        entry.pack()
        def get():
            empno = entry.get()
            sqledit = "SELECT * FROM Employees WHERE idEmployees = " + empno
            mydb.execute(sqledit)
            employee = mydb.fetchall()
            employeeinfo = tk.Toplevel(editwindow)
            employeeinfo.title("Employee Info")
            employeeinfo.geometry("600x800")
            butframe = tk.Frame(employeeinfo)
            butframe.pack(side='top')

            label1 = tk.Label(employeeinfo, text="EmployeesID")
            entry1 = tk.Entry(employeeinfo, bd =2, width=50)
            entry1.insert(0,employee[0][0])
            label1.pack()
            entry1.pack()

            label1 = tk.Label(employeeinfo, text="Name")
            entry2 = tk.Entry(employeeinfo, bd =2, width=50)
            entry2.insert(0,employee[0][1])
            label1.pack()
            entry2.pack()

            label1 = tk.Label(employeeinfo, text="Last Name")
            entry3 = tk.Entry(employeeinfo, bd =2, width=50)
            entry3.insert(0,employee[0][2])
            label1.pack()
            entry3.pack()

            label1 = tk.Label(employeeinfo, text="Title")
            entry4 = tk.Entry(employeeinfo, bd =2, width=50)
            entry4.insert(0,employee[0][3])
            label1.pack()
            entry4.pack()

            label1 = tk.Label(employeeinfo, text="Department")
            entry5 = tk.Entry(employeeinfo, bd =2, width=50)
            entry5.insert(0,employee[0][4])
            label1.pack()
            entry5.pack()

            label1 = tk.Label(employeeinfo, text="Salary")
            entry6 = tk.Entry(employeeinfo, bd =2, width=50)
            entry6.insert(0,employee[0][5])
            label1.pack()
            entry6.pack()

            label1 = tk.Label(employeeinfo, text="From Date")
            entry7 = tk.Entry(employeeinfo, bd =2, width=50)
            entry7.insert(0,employee[0][6])
            label1.pack()
            entry7.pack()

            label1 = tk.Label(employeeinfo, text="To Date")
            entry8 = tk.Entry(employeeinfo, bd =2, width=50)
            entry8.insert(0,"")
            label1.pack()
            entry8.pack()

            label1 = tk.Label(employeeinfo, text="DOB")
            entry9 = tk.Entry(employeeinfo, bd =2, width=50)
            entry9.insert(0,employee[0][8])
            label1.pack()
            entry9.pack()

            label1 = tk.Label(employeeinfo, text="Adress")
            entry10 = tk.Entry(employeeinfo, bd =2, width=50)
            entry10.insert(0,employee[0][9])
            label1.pack()
            entry10.pack()

            label1 = tk.Label(employeeinfo, text="ZIP")
            entry11 = tk.Entry(employeeinfo, bd =2, width=50)
            entry11.insert(0,employee[0][10])
            label1.pack()
            entry11.pack()

            label1 = tk.Label(employeeinfo, text="City")
            entry12 = tk.Entry(employeeinfo, bd =2, width=50)
            entry12.insert(0,employee[0][11])
            label1.pack()
            entry12.pack()

            label1 = tk.Label(employeeinfo, text="Email")
            entry13 = tk.Entry(employeeinfo, bd =2, width=50)
            entry13.insert(0,employee[0][12])
            label1.pack()
            entry13.pack()

            label1 = tk.Label(employeeinfo, text="Gender")
            entry14 = tk.Entry(employeeinfo, bd =2, width=50)
            entry14.insert(0,employee[0][13])
            label1.pack()
            entry14.pack()

            def editdata():
                empid = int(entry1.get())
                empname = entry2.get()
                emplastname = entry3.get()
                emptitle = entry4.get()
                empdepartment = entry5.get()
                empsalary = int(entry6.get())
                empfromdate = entry7.get()
                emptodate = entry8.get()
                if emptodate == "":
                    emptodate = None
                empdob = entry9.get()
                empaddress = entry10.get()
                empzip = entry11.get()
                empcity = entry12.get()
                empemail = entry13.get()
                empgender = entry14.get()
                empcounselor = None
                sqlupdate= "UPDATE Employees SET FirstName = %s ,LastName = %s ,Title = %s ,Department = %s ,Salary = %s ,FromDate = %s ,ToDate = %s ,DateOfBirth = %s ,Address = %s ,PostalCode = %s ,City = %s ,Email = %s ,Gender = %s ,Counselor= %s WHERE idEmployees = " + empno
                values = ( empname,emplastname,emptitle , empdepartment , empsalary , empfromdate , emptodate , empdob , empaddress , empzip , empcity , empemail , empgender , empcounselor)
                mydb.execute(sqlupdate , values)
                db_connection.commit()
                employeeinfo.destroy()
                editwindow.destroy()
                view("Employees")

            editbutt = tk.Button(butframe , text ="Edit" , command=lambda:editdata())
            editbutt.pack()

        editemp = tk.Button(editwindow,text="Edit" , command=lambda:get())
        editemp.pack()






    mb.menu.add_checkbutton (label="Students" , command = lambda: editstudents())
    mb.menu.add_checkbutton (label="Teachers" , command = lambda: editemployees())
        

bottomframe = tk.Frame(window)
bottomframe.pack(side="bottom")
bottomframe.configure(background='white')

searchbutton = tk.Button(bottomframe,text="Search",command=lambda:search())
searchbutton.pack(side="right")


editbutton = tk.Button(bottomframe,text="Update" , command=lambda:edit())
editbutton.pack(side='left')

if adminlogon == True:
    window.mainloop()
if studentlogon == True:
    window.destroy()
    viewstudent()
