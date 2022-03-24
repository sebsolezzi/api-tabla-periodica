from flask import Blueprint,render_template,jsonify
from funciones import obtener_por_electrones, obtener_por_serie, obtener_por_simbolo, obtener_todos
from flask_cors import CORS,cross_origin

elementos = Blueprint('elementos',__name__)

CORS(elementos)

@elementos.route('/')
@cross_origin()
def render_index():
    return render_template('index.html')

#regrese un json con todos los elementos de tabla periodica
@elementos.route('/api/todos')
@cross_origin()
def return_elements():
    lista = obtener_todos()
    return jsonify(lista),200

#regresa un json con elemento de tabla que sean de esa serie
@elementos.route('/api/serie/<nombreserie>')
@cross_origin()
def return_por_Serie(nombreserie):
    if nombreserie == '':
        return jsonify('sin nombre serie'),404
    lista = obtener_por_serie(nombreserie)
    if lista != []:
        return jsonify(lista),200
    else:
        return jsonify(lista),204

#regresa un json con elemento de tabla que tenga esa cantidad de electrones
@elementos.route('/api/electrones/<int:electrones>')
@cross_origin()
def return_por_electrones(electrones):
    lista = obtener_por_electrones(electrones)
    if len(lista) >= 1:
        return jsonify(lista),200
    else:
        return jsonify(lista),204


#regresa un json con el elemento de la tabla que tenga ese simbolo
@elementos.route('/api/simbolo/<simbol>')
@cross_origin()
def return_por_simbolo(simbol):
    lista = obtener_por_simbolo(simbol)
    if len(lista) >= 1:
        return jsonify(lista),200
    else:
        return jsonify(lista),204