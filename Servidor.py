class Servidor:

    def __init__(self,ubicacion):
        self.ubicacion=ubicacion

    def __str__(self):
        texto="{0}"
        return texto.format(self.ubicacion)
