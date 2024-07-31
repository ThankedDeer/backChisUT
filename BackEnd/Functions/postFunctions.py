from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import BackEnd.GlobalInfo.Keys as PracticaKeys
import BackEnd.GlobalInfo.ResponseMessages as ResponseMessages

app = Flask(__name__)
CORS(app)

# Conexión a MongoDB
if PracticaKeys.dbconn is None:
    mongoConnect = MongoClient(PracticaKeys.strConnection)
    PracticaKeys.dbconn = mongoConnect[PracticaKeys.strDBConnection]

dbConnPost = PracticaKeys.dbconn["clChisme"]

@app.route('/getchismes', methods=['GET'])
def getChisme():
    try:
        objFindColab = dbConnPost.find()
        listColab = list(objFindColab)
        
        for colab in listColab:
            # Convertir ObjectId a string
            colab['_id'] = str(colab['_id'])
        
        response_data = {'Response': listColab}
        return jsonify(response_data)
    except Exception as e:
        print("Error al obtener chismes:", e)
        return jsonify(ResponseMessages.message500), 500

@app.route('/newchisme', methods=['POST'])
def postChisme():
    try:
        # Obtener datos del formulario
        titulo = request.form.get('strTitulo')
        chisme = request.form.get('strChisme')
        usuario = request.form.get('strUsuario')
        categoria = request.form.get('strCategoria')
        
        # Verificar que los datos se reciban correctamente
        print(f"Datos recibidos: Titulo={titulo}, Chisme={chisme}, Usuario={usuario}, Categoria={categoria}")

        # Obtener el archivo si está presente
        image = request.files.get('image')

        # Crear el nuevo chisme
        nuevo_chisme = {
            'strTitulo': titulo,
            'strChisme': chisme,
            'strUsuario': usuario,
            'strCategoria': categoria
        }
        
        # Si se recibió una imagen, agregarla al diccionario
        if image:
            # Guarda el archivo en una ubicación específica o solo guarda el nombre
            nuevo_chisme['image'] = image.filename  # Puedes guardar el archivo si lo necesitas
            # Ejemplo: image.save(os.path.join('/path/to/save', image.filename))
            print(f"Imagen recibida: {image.filename}")

        # Insertar el nuevo chisme en la base de datos
        resultado = dbConnPost.insert_one(nuevo_chisme)
        
        if resultado.inserted_id:
            nuevo_chisme['_id'] = str(resultado.inserted_id)
            return jsonify(nuevo_chisme), 200
        else:
            return jsonify({"message": "Error al agregar chisme"}), 500
    except Exception as e:
        print('Error al agregar chisme:', e)
        return jsonify({"message": "Error interno del servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)
