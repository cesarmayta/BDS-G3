from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox

class Empresa:
    
    def __init__(self,app):
        self.app = app
        self.app.title("Gestión de Empresas")
        self.app.geometry("640x480")
        
        frame = LabelFrame(self.app, text="Registro de Empresas")
        frame.grid(row=0, column=0, columnspan=2, pady=10,padx=10)
        
        lb_razon_social = Label(frame, text="Razón Social")
        lb_razon_social.grid(row=0, column=0)
        
        self.txt_razon_social = Entry(frame)
        self.txt_razon_social.grid(row=0, column=1)