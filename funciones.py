from data.tablaperiodica import diccionario
busqueda = ""

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