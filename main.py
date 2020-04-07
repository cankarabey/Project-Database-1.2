import tkinter as tk
import mysql.connector


db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='2501',
    database='inh'
)
mydb = db_connection.cursor()
sql_statement= 'SELECT * FROM '

window = tk.Tk()
window.geometry("900x600")
window.title("INH Database")
from PIL import ImageTk, Image

window = tk.Tk()
window.title("INHOLLAND Database")
window.geometry("300x300")
window.configure(background='grey')

path = "Inholland.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

f = tk.Frame(window)
f.pack()

menubar = tk.Menu(window)
def view(table):
    global lb1, f
    f.destroy()
    f = tk.Frame(window)
    f.pack()
    lb1 = tk.Listbox(f, width=100 , height=100)
    mydb.execute(sql_statement + table)
    output = mydb.fetchall()
    count = 1
    for x in output:
        lb1.insert(count , x)
        count +=1 
    lb1.pack()

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
filemenu.add_command(label="Students",command=lambda: view("STUDENTS"))
filemenu.add_command(label="Teachers",command=lambda: view("EMPLOYEES"))
filemenu.add_command(label="Programmes" ,command=lambda: view("PROGRAMMES"))
filemenu.add_command(label="Courses" ,command=lambda: view("COURSES"))
filemenu.add_command(label="Exams" , command=lambda: view("EXAMS"))
filemenu.add_command(label="Results",command=lambda: view("RESULTS"))

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