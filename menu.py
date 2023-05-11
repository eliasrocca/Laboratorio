from parcial import *
menu = ["1.Mostrar nombre" , "2.Mostrar nombre y altura"]


while True:
    for opcion in menu:
        print(opcion)
    respuesta = int(input("Ingrese una opcion"))
    match respuesta:
        case 1:
            pprint(personaje_lista)

        case 2:
            mostrar_cantidad_por_raza(personaje_lista,'raza')