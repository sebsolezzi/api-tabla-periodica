from pickle import TRUE
from flask import Flask
from routes.elementos import elementos
from flask_cors import CORS,cross_origin

app = Flask('__name__')

app.register_blueprint(elementos)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.errorhandler(404)
def error(error):
    return 'seccion no encontrada',404  

if __name__ == '__main__':
    app.run(debug=False,port=5000)