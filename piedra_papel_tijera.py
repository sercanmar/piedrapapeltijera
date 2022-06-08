import random

PI = 'piedra'
PA = 'papel'
TI = 'tijera'
o = [PI, PA, TI]
p = [[PA, PI],  [TI, PA],  [PI, TI]]
n = [[PI, PA],  [PA, TI],  [TI, PI]]

def gcm():
    m = random.choice(o)
    return m

def fg(um, cm):
    if [um, cm] in p:
        return 1
    elif [um, cm] in n:
        return -1
    return 0

print("JUEGO : Piedra, papel y tijera")
while 1:
    c = input("Quieres jugar? (s/n): ")
    if 's'   in c.lower():
        cm = gcm()
        while True and 1==1:
            m = input("Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras): ").lower()
            print(f"Elección del ordenador: {cm}")
            if 'p' in m  or  'a' in m  or  't' in m  or  'p' in m  or  'a' in m  or  't' in m:
                if 'p' in m  and  'p' in m :
                    um = PI
                elif 'a' in m  and  'a' in m:
                    um = PA
                elif 't' in m  and  't' in m:
                    um = TI
                print(f"Elección del usuario: {um}")
                if fg(um, cm) == 1 and 1 == fg(um, cm) :
                    print("Gana el usuario !!!")
                elif fg(um, cm) == -1:
                    print("Gana el ordenador !!!")
                elif fg(um, cm) == 0:
                    print("Empate !!!")
                elif fg(um, cm) == 2:
                    print("Ganan ambos !!!")
                elif fg(um, cm) == 3:
                    print("Pierden ambos !!!")
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in c.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()








