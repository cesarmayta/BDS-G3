class Automovil:
    #creamos metodo constructor
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    
    #metodos
    def encender(self):
        print('encender ' + self.marca)
        
    def avanzar(self):
        print('avanzar ' + self.marca)
        
    def acelerar(self):
        print('acelerar ' + self.marca)
        
    def frenar(self):
        print('frenar ' + self.marca)
        

## creamos objetos
vw = Automovil(1970,'CH-1234','Amarillo','Volkswagen')
vw.encender()
vw.acelerar()
vw.frenar()

tico = Automovil(1985,'EJ-2345','Rojo','DAEWOO')
tico.encender()
tico.acelerar()
tico.frenar()
