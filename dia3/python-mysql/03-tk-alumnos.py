from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import mysql.connector

class AlumnoTk:
    
    def __init__(self,app):
        self.app = app
        self.app.title('Alumnos')
        self.app.geometry('640x480')
        
        self.db = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='datag3')
        
        self.cursor = self.db.cursor()
        
        frame = LabelFrame(self.app, text='Registrar nuevo alumno')
        frame.grid(row=0, column=0, columnspan=2, pady=10,padx=50)
        
        lb_dni = Label(frame, text='DNI')
        lb_dni.grid(row=1, column=0)
        self.txt_dni = Entry(frame)
        self.txt_dni.grid(row=1, column=1)
        
        lb_nombre = Label(frame, text='Nombre')
        lb_nombre.grid(row=2, column=0)
        self.txt_nombre = Entry(frame)
        self.txt_nombre.grid(row=2, column=1)
        
        btn_insertar = Button(frame, text='Insertar')
        btn_insertar.grid(row=3, columnspan=2, sticky=W+E)
        
        
app = Tk()
app_alumno = AlumnoTk(app)
app.mainloop()
        