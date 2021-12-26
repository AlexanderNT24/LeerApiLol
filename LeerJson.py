import urllib.request
import json

urlApi="https://quiet-hollows-40476.herokuapp.com/lol/filter"

respuesta=urllib.request.urlopen(urlApi)

datos=json.loads(respuesta.read())

print(datos)

for partida in datos:
    print("Partida")
    print("ID")
    print(partida['id'])

    for jugadores in datos:
        #print(jugadores['players'])
        jugadoresPartida=jugadores['players']
        print("Datos Jugadores")
        for datosJugadores in jugadoresPartida:
            print("------------------")
            print(datosJugadores['name'])
            print(datosJugadores['id'])
            print(datosJugadores['server'])   
            print(datosJugadores['teamColor']) 
            print(datosJugadores['champ']) 

for fecha in datos:    
    print(fecha['date'])

for teamGanador in datos:
    print(teamGanador['winTeam'])



  