import random
import sys

piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'
lagarto = 'lagarto'
opciones = [piedra, papel, tijera, lagarto]
gana_usuario = [[papel, piedra], [tijera, papel], [piedra, tijera], [lagarto, papel], [piedra, lagarto],
                [tijera, lagarto]]
gana_ordenador = [[piedra, papel], [papel, tijera], [tijera, piedra], [papel, lagarto], [lagarto, piedra],
                  [lagarto, tijera]]
nombre = input("dime tu nombre")
rondas = int(input("dime el numero de rondas"))
empezar = input("Quieres jugar? (s/n): ")
if 'n' in empezar.lower():
    sys.exit()
intentos = 0
victorias_usuario = 0
victorias_ordenador = 0


def eleccionordenador():
    eleccion_ordenador = random.choice(opciones)
    return eleccion_ordenador


def ganador(eleccion, eleccion_ordenador):
    if [eleccion, eleccion_ordenador] in gana_usuario:
        return 1
    elif [eleccion, eleccion_ordenador] in gana_ordenador:
        return -1
    return 0


print("JUEGO : Piedra, papel, tijera y lagarto")
while 1:
        while True:
            eleccion_ordenador = eleccionordenador()
            if intentos == rondas:
                break
            eleccion_usuario = input(
                "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras / 'l' para lagarto): ").lower()
            print(f"Elección del ordenador: {eleccion_ordenador}")
            if eleccion_usuario == 'terminar':
                print("Tienes miedo?")
                sys.exit()
            if 'p' or 'a' or 't' or 'l' in eleccion_usuario:
                if 'p' in eleccion_usuario:
                    eleccion = piedra
                elif 'a' in eleccion_usuario:
                    eleccion = papel
                elif 't' in eleccion_usuario:
                    eleccion = tijera
                elif 'l' in eleccion_usuario:
                    eleccion = lagarto
                print(f"Elección del usuario: {eleccion}")
                if ganador(eleccion, eleccion_ordenador) == 1:
                    print(f"Gana {nombre} !!!")
                    victorias_usuario += 1
                    intentos += 1
                elif ganador(eleccion, eleccion_ordenador) == -1:
                    print(f"pierde {nombre} !!!")
                    victorias_ordenador += 1
                    intentos += 1
                elif ganador(eleccion, eleccion_ordenador) == 0:
                    print("Empate !!!")
                    intentos += 1

            else:
                print("Entrada incorrecta. Vuelve a intentar.")


        if intentos == rondas:
            if victorias_usuario > victorias_ordenador:
                print(f"el ganador final es {nombre} con {victorias_usuario} victorias")
                break
            if victorias_ordenador > victorias_usuario:
                print(f"el ganador final es ordenador con {victorias_ordenador} victorias")
                break
            if victorias_ordenador == victorias_usuario:
                print(f"Ha habido un empate con {victorias_usuario} victorias cada uno")
                break
        else:
            print('Entrada incorrecta. Vuelve a intentar.')
        print()
