# -*- coding: utf-8 -*-
#Programa que encuentra la lista más larga posible de palabras en el fichero pokemon.txt
#Autores: Kevin Jesus Valle Gomez
#         Adrian Bazan Muñoz

#Funcion que calcula la lista más larga de palabras encadenadas empezando por
#una palabra dada (su índice)
def lista_larga(indice, lista):
    listAux = [lista[indice]]
    i = 0
    
    while i < len(lista):
        if lista[i] not in listAux and lista[indice].endswith(lista[i][0]):
            listAux += [lista[i]]
            indice = i
            i = 0
        else:
            i += 1
    
    return listAux

#Abrimos el fichero e insertamos su contenido en un array, quedando cada linea como un
#elemento del mismo
fichero = open('pokemon.txt', 'r')
contenido = fichero.read()

#Eliminamos los saltos de linea y convertimos cada palabra en un elemento del array
contenido = contenido.replace('\n', ' ')
contenido = contenido.split(' ')

listaFinal = list()

#Se comprueba la lista para cada palabra del array, almacenandose siempre la
#lista más larga de todas.
i = 0
while i < len(contenido):
    lista = lista_larga(i, contenido)

    if len(lista) > len(listaFinal):
        listaFinal = lista
    i += 1

print "La lista de palabras es: ", listaFinal, "\nSu tamaño es: ", len(listaFinal)