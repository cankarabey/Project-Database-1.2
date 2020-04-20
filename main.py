import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image


db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2508',
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
print(studentids)

loginscreen = tk.Tk()
loginscreen.geometry("500x150")
loginscreen.title("Login")
loginscreen.iconbitmap("inhLogo.ico")
labelusername = tk.Label(loginscreen, text="Admin name/ Student name")
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
window.geometry("1200x600")
window.title("INHOLLAND Database")
window.iconbitmap("inhLogo.ico")

window.configure(background='grey')

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

def search(person):
    root = tk.Tk()
    root.title("Inholland Academy")
    root.iconbitmap("inhLogo.ico")
    #root.geometry("200*200")
    label = tk.Label(root, text=person+"'s name")
    e = tk.Entry(root, width=40)

    label.pack()
    e.pack()


    def personsearch():
        global firstLetter
        firstLetter = e.get()
        if person.lower() == "student":
            aboutstudent = tk.Tk()
            aboutstudent.title("Student Info")
            aboutstudent.iconbitmap("inhLogo.ico")
            Columns = ["FirstName", "Last Name", "StudentID", "Programme", "Address", "DateOfBirth", "ZIP", "City",
                        "Email", "Counselor", "Start Year", "Gender", "ProgrammeID"]
            sgrades = ttk.Treeview(aboutstudent, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13), show="headings", height="50")
            for i in range(14):
                sgrades.column(i, width=110, anchor="center")
            sgrades.pack()
            count = 0
            for x in Columns:
                count += 1
                sgrades.heading(count, text=x)
            mydb.execute(
                "SELECT * from students where firstname like '{}%'".format(str(firstLetter)))
            gradesfst = mydb.fetchall()
            for x in gradesfst:
                sgrades.insert('', 'end', values=x)
            aboutstudent.mainloop()

        if person.lower() == "teacher":
            aboutteacher = Tk()
            aboutteacher.title("Teacher Info")
            aboutteacher.iconbitmap("inhLogo.ico")
            Columns = ["EmployeesID", "FirstName", "Last Name", "Title", "Department", "Salary", "FromDate", "ToDate",
                         "DOB", "Address", "ZIP", "City", "Email", "Gender", "Counselor"]
            sgrades = ttk.Treeview(aboutteacher, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15), show="headings", height="50")
            for i in range(16):
                sgrades.column(i, width=110, anchor="center")
            sgrades.pack()
            count = 0
            for x in Columns:
                count += 1
                sgrades.heading(count, text=x)
            mydb.execute(
                "SELECT * from employees where firstname like '{}%'".format(str(firstLetter)))
            gradesfst = mydb.fetchall()
            for x in gradesfst:
                sgrades.insert('', 'end', values=x)
            aboutteacher.mainloop()

    mybutton = tk.Button(root, text="Search", command=personsearch, fg="white", bg="blue")
    mybutton.pack()

    root.mainloop()


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

searchmenu = tk.Menu(menubar, tearoff=0)
searchmenu.add_command(label="Student",command=lambda: search("Student"))
searchmenu.add_command(label="Teacher",command=lambda: search("Teacher"))

menubar.add_cascade(label="Search", menu=searchmenu)

window.config(menu=menubar)


if adminlogon == True:
    window.mainloop()
if studentlogon == True:
    window.destroy()
    viewstudent()