import tkinter as tk
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

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Students")
filemenu.add_command(label="Teachers")
filemenu.add_command(label="Studies")
filemenu.add_command(label="Courses")
filemenu.add_command(label="Exams")
filemenu.add_command(label="Results")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="View", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)

submenu2 = tk.Menu(window)
submenu2.add_command(label="Students")
submenu2.add_command(label="Teachers")
submenu2.add_command(label="Studies")
submenu2.add_command(label="Courses")
submenu2.add_command(label="Exams")
submenu2.add_command(label="Results")
editmenu.add_cascade(label='Add', menu=submenu2, underline=0)


editmenu.add_separator()

submenu1 = tk.Menu(window)
submenu1.add_command(label="Students")
submenu1.add_command(label="Teachers")
submenu1.add_command(label="Studies")
submenu1.add_command(label="Courses")
submenu1.add_command(label="Exams")
submenu1.add_command(label="Results")
editmenu.add_cascade(label='Delete', menu=submenu1, underline=0)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
helpmenu.add_command(label="Manual")
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
window.mainloop()