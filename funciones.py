from data.tablaperiodica import diccionario
busqueda = ""

def obtener_no_metales()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'no metales':
            lista.append(item)
    return lista

def obtener_metaloides()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'metaloides':
            lista.append(item)
    return lista


def obtener_gases_nobles()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'gases nobles':
            lista.append(item)
    return lista


def obtener_halogenos()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'halogenos':
            lista.append(item)
    return lista

def obtener_metales_bloque_p()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'metales del bloque p':
            lista.append(item)
    return lista


def obtener_metales_alcalinos()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'metales alcalinos':
            lista.append(item)
    return lista

def obtener_metales_de_transicion()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'metales de transicion':
            lista.append(item)
    return lista


def obtener_metales_alcalinoterreos()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'metales alcalinoterreos':
            lista.append(item)
    return lista


def obtener_actinidos()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'actnidos':
            lista.append(item)
    return lista
    
def obtener_lantanidos()->list:
    lista = []
    for item in diccionario:
        if item['serie'] == 'lantanidos':
            lista.append(item)
    return lista


def obtener_por_electrones(electrones:int)->list:
    lista = []
    for item in diccionario:
        if item['electrones'] == electrones:
            lista.append(item)
            return lista
    if lista == []:
        return lista

def obtener_por_simbolo(simbolo:str)->list:
    lista = []
    criterio = "nada"
    for item in diccionario:
        if item['simbolo'] == simbolo:
            lista.append(item)
            return lista
    if lista == []:
        return []

def obtener_por_serie(serie:str)->list:
    lista = []
    if serie == 'nometales':
        busqueda = 'no metales'
    elif serie == 'halogenos':
        busqueda = 'halogenos'
    elif serie == 'actinidos':
        busqueda = 'actinidos'
    elif serie == 'lantanidos':
        busqueda = 'lantanidos'
    elif serie == 'metalesbloquep':
        busqueda = 'metales del bloque p'
    elif serie == 'metaloides':
        busqueda = 'metaloides'
    elif serie == 'metalesalcalinoterreos':
        busqueda = 'metales alcalinoterreos'
    elif serie == 'metalesdetransicion':
        busqueda = 'metales de transicion'
    elif serie == 'gasesnobles':
        busqueda = 'gases nobles'
    elif serie == 'metalesalcalinos':
        busqueda = 'metales alcalinos'
    else:
        return lista
    
    for item in diccionario:
        if item['serie'] == busqueda:
            lista.append(item)
    return lista
    

def obtener_todos()->list:
    return diccionario