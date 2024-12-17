class Persona:
    def __init__(self,dni,nom,ema):
        self.nombre = nom
        self.dni = dni
        self.email = ema
        
    def mostrar(self):
        print("*"*50)
        print(f"DNI : {self.dni}")
        print(f"NOMBRE : {self.nombre}")
        print(f"EMAIL : {self.email}")
    
class Alumno(Persona):
    def __init__(self,dni,nom,ema,nota):
        super().__init__(dni,nom,ema)
        self.nota = nota
        
    def mostrar(self):
        super().mostrar()
        print(f'NOTA : {self.nota}')
    
class Profesor(Persona):
    def __init__(self,dni,nom,ema,esp):
        super().__init__(dni,nom,ema)
        self.especialidad = esp
        
    def mostrar(self):
        super().mostrar()
        print(f"ESPECIALIDAD : {self.especialidad}")
        
class Empleado(Persona):
    pass
        
        
        
alumno1 = Alumno('100','JORGE','JORGE@GMAIL.COM',20)
alumno1.mostrar()

profesor1 = Profesor('200','LUIS','LUIS@GMAIL.COM','MACHINE LEARNING')
profesor1.mostrar()

empleado1 = Empleado('300','HEBERT','HEBERT@GMAIL.COM')
empleado1.mostrar()