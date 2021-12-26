import urllib.request
import json

import Partida
import Jugador
import Campeon
import Servidor
import Equipo

urlApi="https://quiet-hollows-40476.herokuapp.com/lol/filter"

respuesta=urllib.request.urlopen(urlApi)

datos=json.loads(respuesta.read())

for fecha in datos:    
    fechaPartida=fecha['date']

for teamGanador in datos:
    teamGanador=teamGanador['winTeam']

for partida in datos:
    idPartida=partida['id']
    
    objetoPartida=Partida.Partida(id=idPartida,fecha=fechaPartida,teamGanador=teamGanador)
    
    for jugadores in datos:
        jugadoresPartida=jugadores['players']
        for datosJugadores in jugadoresPartida:
            objetoServidor=Servidor.Servidor(ubicacion=datosJugadores['server'])
            objetoCampeon=Campeon.Campeon(nombre=datosJugadores['champ'])
            objetoEquipo=Equipo.Equipo(color=datosJugadores['teamColor'])
            objetoJugador=Jugador.Jugador(nombre=datosJugadores['name'],id=datosJugadores['id'],servidor=objetoServidor,campeon=objetoCampeon,equipo=objetoEquipo)
            objetoPartida.agregarJugadores(objetoJugador)


print(objetoPartida)