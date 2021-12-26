class Equipo:

    def __init__(self,color):
        self.color=color

    def __str__(self):
        texto="{0}"
        return texto.format(self.color)
