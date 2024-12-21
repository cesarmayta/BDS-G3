from tkinter import *
from tkinter import messagebox

def saludar():
    messagebox.showinfo('Saludo', f'Hola {txt_nombre.get()}')

app = Tk()
app.title("Mi app")
app.geometry("300x200")

#frame
frame = LabelFrame(app,text='Nueva Ventana',padx=50,pady=50)
frame.grid(row=0,column=0,padx=10,pady=10)

#label
lb_nombre = Label(frame,text='Nombre:')
lb_nombre.grid(row=1,column=0)

#text
txt_nombre = Entry(frame)
txt_nombre.grid(row=1,column=1)

#button
btn_saludo = Button(frame,text='Saludar',command=saludar)
btn_saludo.grid(row=1,column=2)

app.mainloop()