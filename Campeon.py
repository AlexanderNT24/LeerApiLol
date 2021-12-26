class Campeon:

    def __init__(self,nombre):
        self.nombre=nombre

    def __str__(self):
        texto="{0}"
        return texto.format(self.nombre)