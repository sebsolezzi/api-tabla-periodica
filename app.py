from flask import Flask
from routes.elementos import elementos

app = Flask('__name__')

app.register_blueprint(elementos)

@app.errorhandler(404)
def error(error):
    return 'seccion no encontrada',404  

if __name__ == '__main__':
    app.run(debug=False,port=5000)