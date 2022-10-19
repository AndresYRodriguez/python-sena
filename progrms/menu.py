from modulos.andres import resta
from modulos.felipe import multi
from modulos.ginna import suma
from modulos.sergio import facto


def mostrar_menu(opciones):
    print('Selection una opción: ')
    for num in sorted(opciones):
        print(f' {num}) {opciones[num][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def principal():
    opciones = {
        '1': ('Suma ', suma.operacion),
        '2': ('Resta', resta.resta),
        '3': ('Factorial', facto.factorial),
        '4': ('Multiplicacion', multi.multiplicar),
        '5': ('Salir', salir)
    }
    generar_menu(opciones, '5')


def salir():
    print('Saliendo')
