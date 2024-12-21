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
        
        btn_insertar = Button(frame, text='Insertar',command=self.insertar)
        btn_insertar.grid(row=3, columnspan=2, sticky=W+E)
        
        #grilla de alumnos
        self.tree = Treeview(self.app, columns=('DNI','Nombre'))
        self.tree.grid(row=4, column=0, columnspan=2,padx=10,pady=10)
        self.tree.heading('#0', text='id')
        self.tree.heading('DNI', text='DNI')
        self.tree.heading('Nombre', text='Nombre')
        
        self.cargar_alumnos()
        
    def cargar_alumnos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        self.cursor.execute("select id,nro_documento,nombre from alumno order by id")
        for row in self.cursor.fetchall():
            self.tree.insert('',0,text=row[0],values=(row[1],row[2]))
            
    def insertar(self):
        nuevo_alumno = (
            self.txt_dni.get(),
            self.txt_nombre.get()
        )
        
        query = "insert into alumno(nro_documento,nombre) values(%s,%s)"
        self.cursor.execute(query,nuevo_alumno)
        self.db.commit()
        self.cargar_alumnos()
        
        
app = Tk()
app_alumno = AlumnoTk(app)
app.mainloop()
        