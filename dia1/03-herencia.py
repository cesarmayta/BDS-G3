class Persona:
    def __init__(self,dni,nom,ema):
        self.nombre = nom
        self.dni = dni
        self.email = ema
        
    def mostrar(self):
        print(f"DNI : {self.dni}")
        print(f"NOMBRE : {self.nombre}")
        print(f"EMAIL : {self.email}")
    
class Alumno(Persona):
    pass
    
class Profesor(Persona):
    def __init__(self,dni,nom,ema,esp):
        super().__init__(dni,nom,ema)
        self.especialidad = esp
        
    def mostrar(self):
        print(f"DNI : {self.dni}")
        print(f"NOMBRE : {self.nombre}")
        print(f"EMAIL : {self.email}")
        print(f"ESPECIALIDAD : {self.especialidad}")
        
        
        
alumno1 = Alumno('100','JORGE','JORGE@GMAIL.COM')
alumno1.mostrar()

profesor1 = Profesor('200','LUIS','LUIS@GMAIL.COM','MACHINE LEARNING')
profesor1.mostrar()