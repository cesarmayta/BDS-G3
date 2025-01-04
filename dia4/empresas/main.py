from tkinter import *
from libempresas import Empresa

app = Tk()

if __name__ == '__main__':
    empresa = Empresa(app)
    app.mainloop()