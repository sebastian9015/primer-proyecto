class Saludo:

    def __init__(self,mensaje):
        self.mensaje=mensaje

    def mostrarmensaje (self):
        print(self.mensaje)

saludo =Saludo("hola mundo")
saludo.mostrarmensaje()



