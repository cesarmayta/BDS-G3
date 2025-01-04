from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import mysql.connector

class Empresa:
    
    def __init__(self,app):
        self.app = app
        self.app.title("Gestión de Empresas")
        self.app.geometry("640x380")
        
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="db_proyecto")
        
        self.cursor = self.db.cursor()
        
        self.empresa_id = 0
        
        frame = LabelFrame(self.app, text="Registro de Empresas")
        frame.grid(row=0, column=0, columnspan=2, pady=10,padx=10)
        
        lb_ruc = Label(frame, text="RUC")
        lb_ruc.grid(row=0, column=0)
        
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=0, column=1)
        
        lb_razon_social = Label(frame, text="Razón Social")
        lb_razon_social.grid(row=0, column=2)
        
        self.txt_razon_social = Entry(frame)
        self.txt_razon_social.grid(row=0, column=3)
        
        self.btn_insertar = Button(frame,text="Insertar Nueva Empresa", command=self.insertar)
        self.btn_insertar.grid(row=0, column=4)
        
        self.btn_editar = Button(self.app,text="Editar Empresa",command=self.editar)
        self.btn_editar.grid(row=3, column=0)
        
        self.btn_eliminar = Button(self.app,text="Eliminar Empresa",command=self.eliminar)
        self.btn_eliminar.grid(row=3, column=1)
        
        self.tree = Treeview(self.app, columns=("RUC","Razón Social"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("RUC", text="RUC")   
        self.tree.heading("Razón Social", text="Razón Social")
        
        self.tree.grid(row=1, column=0,padx=20,pady=10,columnspan=2)
        
        self.cargar_empresas()
        
    def cargar_empresas(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        self.cursor.execute("select id,ruc,razon_social from empresa")
        for row in self.cursor.fetchall():
            self.tree.insert("",0,text=row[0],values=(row[1],row[2]))
        
    def insertar(self):
        if self.empresa_id > 0:
            self.actualizar()
            return
        
        
        if not self.txt_ruc.get() or not self.txt_razon_social.get():
            messagebox.showwarning("Atención","Complete los campos")
            return
        
        nueva_empresa = (self.txt_ruc.get(),self.txt_razon_social.get())
        
        query = "insert into empresa(ruc,razon_social) values(%s,%s)"
        self.cursor.execute(query,nueva_empresa)
        self.db.commit()
        self.cargar_empresas()
        
    def editar(self):
        selected_row = self.tree.selection()
        if not selected_row:
            messagebox.showwarning("Atención","Seleccione una Empresa")
            return
        
        self.empresa_id = self.tree.item(selected_row[0])["text"]
        print("empresa a editar : ",self.empresa_id)
        self.txt_ruc.delete(0,END)
        self.txt_ruc.insert(0,self.tree.item(selected_row[0])["values"][0])
        self.txt_razon_social.delete(0,END)
        self.txt_razon_social.insert(0,self.tree.item(selected_row[0])["values"][1])
        self.btn_insertar.config(text="Actualizar Empresa")
        
    def actualizar(self):
        nuevo_ruc = self.txt_ruc.get()
        nueva_razon_social = self.txt_razon_social.get()
        
        empresa_actualizar = (nuevo_ruc,nueva_razon_social,self.empresa_id)
        
        if not nuevo_ruc or not nueva_razon_social:
            messagebox.showwarning("Atención","Complete los campos")
            return
        
        query = "update empresa set ruc=%s, razon_social=%s where id=%s"
        self.cursor.execute(query,empresa_actualizar)
        self.db.commit()
        self.cargar_empresas()
        self.limpiar_datos()
        
    def limpiar_datos(self):
        self.txt_ruc.delete(0,END)
        self.txt_razon_social.delete(0,END)
        self.empresa_id = 0
        self.btn_insertar.config(text="Insertar Nueva Empresa")
        
    def eliminar(self):
        selected_row = self.tree.selection()
        if not selected_row:
            messagebox.showwarning("Atención","Seleccione una Empresa")
            return
        
        empresa_id = self.tree.item(selected_row[0])["text"]
        
        respuesta = messagebox.askyesno("Confirmación","¿Esta seguro que desea eliminar la Empresa?")
        
        if respuesta:
            empresa_eliminar = (empresa_id,)
            query = "delete from empresa where id=%s"
            self.cursor.execute(query,empresa_eliminar)
            self.db.commit()
            self.cargar_empresas()
            self.limpiar_datos()
    
        
        
        