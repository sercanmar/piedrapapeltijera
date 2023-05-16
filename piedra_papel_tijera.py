import random

piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'
opciones = [piedra, papel, tijera]
gana_usuario = [[papel, piedra], [tijera, papel], [piedra, tijera]]
gana_ordenador = [[piedra, papel], [papel, tijera], [tijera, piedra]]


def eleccionordenador():
    eleccion_ordenador = random.choice(opciones)
    return eleccion_ordenador


def ganador(eleccion, eleccion_ordenador):
    if [eleccion, eleccion_ordenador] in gana_usuario:
        return 1
    elif [eleccion, eleccion_ordenador] in gana_ordenador:
        return -1
    return 0


print("JUEGO : Piedra, papel y tijera")
while 1:
    empezar = input("Quieres jugar? (s/n): ")
    if 's' in empezar.lower():
        eleccion_ordenador = eleccionordenador()
        while True and 1 == 1:
            eleccion_usuario = input(
                "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras): ").lower()
            print(f"Elección del ordenador: {eleccion_ordenador}")
            if 'p' or 'a' or 't' or 'p' or 'a' or 't' in eleccion_usuario:
                if 'p' in eleccion_usuario:
                    eleccion = piedra
                elif 'a' in eleccion_usuario:
                    eleccion = papel
                elif 't' in eleccion_usuario:
                    eleccion = tijera
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
