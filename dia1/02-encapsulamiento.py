class Usuario:
    __email = 'cesar@gmail.com'
    __password = 'qwerty123'
    
    def __init__(self):
        pass
    
    def set_password(self,password):
        self.__password = password
    
    def login(self,email,password):
        if(self.__email == email and self.__password == password):
            print(f'Bienvenido {self.__email}')
        else:
            print('datos incorrectos')
            
print('LOGIN DE USUARIOS')
email = input('Ingrese Email :')
password = input('Ingrese Password : ')

usuario = Usuario()
usuario.set_password(password)
usuario.login(email,password)