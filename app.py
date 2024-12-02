from flask import Flask, request, jsonify, render_template
from entities.ciudad import Ciudad
from entities.envio import Envio

app = Flask(__name__)

@app.route('/')
def index():
    ciudades_lista = Ciudad.get_all()
    return render_template('index.html', ciudades=ciudades_lista)

@app.route('/ciudades')
def ciudades():
    ciudades = Ciudad.get_all()
    return render_template('ciudades.html', ciudades=ciudades)

@app.route('/ciudad', methods=['GET'])
def get_ciudades():
    ciudades = Ciudad.get_all()
    return jsonify(ciudades), 200

@app.route('/ciudad-registro', methods=['GET'])
def ciudad_registro():
    return render_template('ciudad.html')

@app.route('/ciudad', methods=['POST'])
def save_ciudad():
    data = request.json
    ciudad = Ciudad(nombre=data['nombre'], codigo=data['codigo'])
    id = Ciudad.save(ciudad)
    return jsonify({'id': id}), 201

@app.route('/ciudad/<int:id>', methods=['PUT'])
def update_ciudad(id):
    data = request.json
    ciudad = Ciudad(nombre=data['nombre'], codigo=data['codigo'])
    result = Ciudad.update(id, ciudad)
    if result == 0:
        return jsonify({'error': 'El registro de ciudad no existe'}), 404
    return jsonify({'id': id}), 201

@app.route('/envios')
def envios():
    envios = Envio.get_all()
    return render_template('envios.html', envios=envios)

@app.route('/envio', methods=['GET'])
def get_envios():
    envios = Envio.get_all()
    return jsonify(envios), 200

@app.route('/envio-registro', methods=['GET'])
def envio_registro():
    return render_template('envio.html')

@app.route('/envio', methods=['POST'])
def save_envio():
    data = request.json
    envio = Envio(origen=data['origen'], destino=data['destino'], fecha_envio=data['fecha_envio'],
                  remitente=data['remitente'], destinatario=data['destinatario'], guia=data['guia'])
    id = Envio.save(envio)
    return jsonify({'id': id}), 201

@app.route('/envio/<int:id>', methods=['PUT'])
def update_envio(id):
    data = request.json
    envio = Envio(origen=data['origen'], destino=data['destino'], fecha_envio=data['fecha_envio'],
                  remitente=data['remitente'], destinatario=data['destinatario'], guia=data['guia'])
    result = Envio.update(id, envio)
    if result == 0:
        return jsonify({'error': 'El registro de envío no existe'}), 404
    return jsonify({'id': id}), 201

if __name__ == '__main__':
    app.run()
