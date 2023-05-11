import csv
import re
from pprint import pprint

ruta = "C:\\Users\\Elias\\Desktop\\Phyton\\Parcial_1\\DBZ.csv"



# 1. Traer datos desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
# cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
# un personaje puede tener más de una raza y más de una habilidad.
# lista_personajes = []
#1

with open(ruta,'r+', encoding='utf-8') as archivo:
    personaje_lista = []
    
    for personaje in archivo:
        # print(personaje, end="")
        nuevo_personaje = {}
        
        register = re.split(",|\n",personaje)
        # print(register)
        # if len(register) > 5:
        nuevo_personaje['id'] = int(register[0].strip())
        nuevo_personaje['nombre'] = register[1].strip()
        nuevo_personaje['raza'] = register[2].strip()
        nuevo_personaje['poder de pelea'] = int(register[3].strip())
        nuevo_personaje['poder de ataque'] = int(register[4].strip())
        nuevo_personaje['habilidades'] = re.split("\|\$\%",register[5].strip())

        for i in range(len(nuevo_personaje['habilidades'])):
            nuevo_personaje['habilidades'][i] = nuevo_personaje['habilidades'][i].strip()

        if nuevo_personaje['raza']== 'Three-Eyed People' or nuevo_personaje['raza'] == 'Shin-jin':
            nuevo_personaje['raza'] = [nuevo_personaje['raza']]
        else:
            nuevo_personaje['raza'] = re.split('-',nuevo_personaje['raza'])
        
        personaje_lista.append(nuevo_personaje)
            

# for elemento in personaje_lista:
#     print(elemento)
        

        

        # Id, Nombre, Raza, Poder de pelea, Poder de ataque, Habilidades
def categorizar_luchadores(lista_heroes, clave):
    luchadores_categorizados = {}

    for luchador in lista_heroes:
        if type(luchador[clave]) == list:
            for categoria in luchador[clave]:


        lista_heroes.append(luchadores_categorizados)




    


    
#2
def mostrar_cantidad_por_raza(lista_heroes, clave):
    
    diccionario_razas = {}

    for heroe in lista_heroes:
        for raza in heroe[clave]:

            elemento = raza
            if elemento == "":
                elemento = "No tiene"
            if elemento in diccionario_razas:
                diccionario_razas[elemento]+=1
            else:
                diccionario_razas[elemento]=1

    

    for clave,valor in diccionario_razas.items():

        print(str(clave)+': '+str(valor))


# #3
# # 3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
# # personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
# # repetirse en los distintos listados.
def mostrar_raza_nombre_attackpower(heroe,clave):
    lista_raza_poder = []
    diccionario_caracteristicas = {}
    for heroe in lista_raza_poder:


        return f"Nombre: {heroe['nombre']}|| {clave}: {heroe[clave]}"
    



# 4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
# deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.
def listar_personajes_habilidad(lista):
    dato_solicitado = input("Ingrese el dato")
    for dato in personaje_lista:
        if dato_solicitado['habilidades']:
            pass

        
        


