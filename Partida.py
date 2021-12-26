class Partida:

    def __init__(self,id,fecha,teamGanador):       
        self.id=id
        self.fecha=fecha
        self.teamGanador=teamGanador
        self.jugadores=[]

    def __str__(self):
       texto="Partida: \nId: {0}\nFecha: {1}\nTeam Ganador: {2}\n\nJugadores: {3}"
       datosJugadores=""
       for jugador in self.jugadores:
            datosJugadores=datosJugadores+str(jugador)
       return texto.format(self.id,self.fecha,self.teamGanador,datosJugadores)

    def agregarJugadores(self,jugador):
        self.jugadores.append(jugador)

            