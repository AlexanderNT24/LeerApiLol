class Jugador:

    def __init__(self,nombre,id,servidor,campeon,equipo):
        self.nombre=nombre
        self.id=id
        self.servidor=servidor
        self.campeon=campeon
        self.equipo=equipo
     
    def __str__(self):
        texto="\nNombre: {0}\nId: {1}\nServidor: {2}\nCampeon: {3}\nEquipo: {4}\n"
        return texto.format(self.nombre,self.id,self.servidor,self.campeon,self.equipo)
     
