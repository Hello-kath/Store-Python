from flask import Flask, render_template
from flask_pymongo import PyMongo
from config import Config

# Crear la aplicación
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la conexión a MongoDB
mongo = PyMongo(app)

@app.route('/')
def index():
    # Ejemplo de uso de la base de datos
    collection = mongo.db['nombre_coleccion']
    datos = collection.find()
    return str(list(datos))  # Muestra los documentos como texto

if __name__ == '__main__':
    app.run(debug=True)
