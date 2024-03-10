"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

def reader_data_csv():
    with open("data.csv", "r") as file:
        data = list(csv.reader(file, delimiter = "\t"))

    return data
#print(reader_data_csv())

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """    
def pregunta_01():
    data = reader_data_csv()
    suma = 0
    for row in data:
        suma += int(row[1])
    return suma



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.


    
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    """
    data = reader_data_csv()
    diccionario = {}
    for row in data:
        if row[0] in diccionario:
            diccionario[row[0]] += 1
        else:
            diccionario[row[0]] = 1
    lista = list(diccionario.items())
    lista.sort()
    return lista



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    data = reader_data_csv()
    diccionario = {}
    for row in data:
        if row[0] in diccionario:
            diccionario[row[0]] += int(row[1])
        else:
            diccionario[row[0]] = int(row[1])
    lista = list(diccionario.items())
    lista.sort()
    return lista


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """


    data = reader_data_csv()
    diccionario = {}
    for row in data:
        mes = row[2].split("-")[1]
        if mes in diccionario:
            diccionario[mes] += 1
        else:
            diccionario[mes] = 1
    lista = list(diccionario.items())
    lista.sort()
    return lista


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = reader_data_csv()
    word_value = {}

    for i in data:
        word = i[0]  # Obtener la letra de la columna 1
        value = int(i[1])  # Obtener el valor de la columna 2
        # Si la letra ya está en el diccionario, se agrega el valor a la lista existente
        if word in word_value:
            word_value[word].append(value)
        else:
            word_value[word] = [value]

    # Lista vacia para almacenar las tuplas de resultado
    result = []

    # Iterar sobre el diccionario y encontrar el valor máximo y mínimo por cada letra
    for words, values in word_value.items():
        value_max = max(values)
        value_min = min(values)
        result.append((words, value_max, value_min))
        sorted_result = sorted(list(result))
    return (sorted_result)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = reader_data_csv()
    diccionario = {}
    for row in data:
        dic = row[4].split(",")
        for i in dic:
            key, value = i.split(":")
            if key in diccionario:
                if int(value) > diccionario[key][1]:
                    diccionario[key] = (diccionario[key][0], int(value))
                if int(value) < diccionario[key][0]:
                    diccionario[key] = (int(value), diccionario[key][1])
            else:
                diccionario[key] = (int(value), int(value))
    lista = list(diccionario.items())
    lista.sort()
    return [(key, *value) for key, value in lista]


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = reader_data_csv()
    diccionario = {}

    for i in data:
        if int(i[1]) in diccionario.keys():
            diccionario[int(i[1])][0].append(i[0])
        else:
            diccionario[int(i[1])] = [[i[0]]]
    # Convertir el diccionario a una lista de tuplas
    resultado_tuplas = [(clave, valores[0]) for clave, valores in diccionario.items()]

    # Ordenar la lista de tuplas por clave
    result_sorted = sorted(resultado_tuplas)
    return result_sorted


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = reader_data_csv()
    diccionario = {}
    for i in data:
        valor_columna_2 = int(i[1])
        letra_columna_1 = i[0]
        if valor_columna_2 in diccionario:
            diccionario[valor_columna_2].add(letra_columna_1)
        else:
            diccionario[valor_columna_2] = {letra_columna_1}
    
    lista = sorted([(valor, sorted(list(letras))) for valor, letras in diccionario.items()])
    return lista
        


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = reader_data_csv()
    diccionario = {}
    for row in data:
        dic = row[4].split(",")
        for i in dic:
            key, value = i.split(":")
            if key in diccionario:
                diccionario[key] += 1
            else:
                diccionario[key] = 1
# ordenar el diccionario
    diccionario = dict(sorted(diccionario.items()))
    
    return diccionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = reader_data_csv()
    lista = [
        (row[0], len(row[3].split(",")), len(row[4].split(",")) if row[4] else 0)
        if len(row) >= 5
        else (row[0], len(row[3].split(",")), 0)
        for row in data
    ]  # agregar la cantidad de elementos de las columnas 4 y 5

    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = reader_data_csv()
    sum = {}    
    for row in data:
        for i in row[3].split(","):
            if i in sum:
                sum[i] += int(row[1])
            else:
                sum[i] = int(row[1])
    return dict(sorted(sum.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """


    data = reader_data_csv()
    letras = {}

    for row in data:
        values = row[4].split(",")
        dic_values = dict((rw.split(":")[0],int(rw.split(":")[1])) for rw in values)
        if row[0] in letras.keys():
            letras[row[0]] += sum(dic_values.values())
        else:
            letras[row[0]] = sum(dic_values.values())
    #0rdenar el diccionario
    letras = dict(sorted(letras.items()))
    return letras
