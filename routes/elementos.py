from flask import Blueprint,render_template,jsonify
from funciones import obtener_actinidos, obtener_por_electrones, obtener_no_metales, obtener_por_simbolo, obtener_todos

elementos = Blueprint('elementos',__name__)

@elementos.route('/')
def render_index():
    return render_template('index.html')

#regrese un json con todos los elementos de tabla periodica
@elementos.route('/todos')
def return_elements():
    lista = obtener_todos()
    return jsonify(lista),200

#regresa un json con los elementos de la tabla que sean tipo nometales
@elementos.route('/serie/nometales')
def return_nometales():
    lista = obtener_no_metales()
    return jsonify(lista),200

#regresa un json con los elementos de la tabla que sean tipo actinidos
@elementos.route('/serie/actinidos')
def return_actinidos():
    lista = obtener_actinidos()
    return jsonify(lista),200

#regresa un json con elemento de tabla que tenga esa cantidad de electrones
@elementos.route('/electrones/<int:electrones>')
def return_por_electrones(electrones):
    lista = obtener_por_electrones(electrones)
    if lista != []:
        return jsonify(lista),200
    else:
        return jsonify(lista),204

#regresa un json con el elemento de la tabla que tenga ese simbolo
@elementos.route('/simbolo/<simbol>')
def return_por_simbolo(simbol):
    lista = obtener_por_simbolo(simbol)
    if lista != []:
        return jsonify(lista),200
    else:
        return jsonify(lista),204