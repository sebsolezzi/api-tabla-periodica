from data.tablaperiodica import diccionario
""" no metales,metaloides ,gases nobles halogenos,metales del bloque p,metales de transicion,actinidos,actnidos,metales alcalinoterreos
,metales alcalinos,halogenos """

def obtener_no_metales()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'no metales':
            lista.append(item)
    return lista


def obtener_actinidos()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'actnidos':
            lista.append(item)
    return lista


def obtener_por_tipo(tipo:str)->list:
    lista = []
    for item in diccionario:
        if item['serie'] == tipo:
            lista.append(item)
    return lista


def obtener_por_electrones(electrones:int)->list:
    lista = []
    for item in diccionario:
        if item['electrones'] == electrones:
            lista.append(item)
            return lista
    if lista == []:
        return []

def obtener_por_simbolo(simbolo:str)->list:
    lista = []
    for item in diccionario:
        if item['simbolo'] == simbolo:
            lista.append(item)
            return lista
    if lista == []:
        return []

def obtener_todos()->list:
    return diccionario