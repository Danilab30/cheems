from flask import Flask, request, jsonify, render_template
from entities.ciudad import Ciudad
from entities.envio import Envio
from entities.rastreo import Rastreo

app = Flask(__name__)

@app.route('/')
def index():
    ciudades_lista = Ciudad.get_all()
    return render_template('index.html', ciudades=ciudades_lista)

@app.route('/costos')
def costos():
    return render_template('costos.html')

@app.route('/rastreos')
def rastreos():
    guia = request.args.get('guia', '')
    rastreos = Rastreo.get_all(guia)
    return render_template('rastreos.html', guia=guia, rastreos=rastreos)

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

@app.route('/ciudad-eliminar/<int:id>', methods=['DELETE'])
def delete_ciudad(id):
    result = Ciudad.delete(id)
    if result == 0:
        return jsonify({'error': 'La ciudad no existe'}), 404
    return jsonify({'mensaje': 'Ciudad eliminada correctamente'}), 200

# METODOS ENVIOS

@app.route('/envios')
def envios():
    ciudades = Ciudad.get_all()  # Asegúrate de que esta función retorna las ciudades correctamente
    print(ciudades)  # Agrega esto para ver los resultados en la consola
    envios = Envio.get_all()  # Si estás mostrando los envíos también, asegúrate de obtenerlos
    return render_template('envios.html', envios=envios, ciudades=ciudades)



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
    envio = Envio(origen=data['origen'], destino=data['destino'], fecha_envio=None,
                  remitente=data['remitente'], destinatario=data['destinatario'], guia=data['guia'])
    id = Envio.save(envio)
    return jsonify({'id': id}), 201

@app.route('/envio/<int:id>', methods=['PUT'])
def update_envio(id):
    data = request.json
    envio = Envio(origen=data['origen'],  destino=data['destino'], fecha_envio= None,
                  remitente=data['remitente'], destinatario=data['destinatario'], guia=data['guia'])
    result = Envio.update(id, envio)
    if result ==0:
        return jsonify({'error':'El registro de envio no existe'}), 404
    return jsonify({'id':id},201)

@app.route('/envio-eliminar/<int:id>', methods=['DELETE'])
def delete_envio(id):
    result = Envio.delete(id)
    if result == 0:
        return jsonify({'error': 'El envio no existe'}), 404
    return jsonify({'mensaje': 'Envio eliminado correctamente'}), 200
    
if __name__ == '__main__':
    app.run()
