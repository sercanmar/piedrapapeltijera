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
    empezar = input("Quieres jugar? (s/n): ")
    if 's' in empezar.lower():
        eleccion_ordenador = eleccionordenador()
        while True:
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
                    print("Gana el usuario !!!")
                elif ganador(eleccion, eleccion_ordenador) == -1:
                    print("Gana el ordenador !!!")
                elif ganador(eleccion, eleccion_ordenador) == 0:
                    print("Empate !!!")
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in empezar.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()
