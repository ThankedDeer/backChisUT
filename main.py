from flask import Flask, jsonify
from flask_cors import CORS
import os
import BackEnd.Functions.userFunctions as callMethodUser
import BackEnd.Functions.postFunctions as callMethodPost
import BackEnd.GlobalInfo.ResponseMessages as ResponseMessage

app = Flask(__name__)
CORS(app)


    
@app.route('/login', methods=['POST'])
def fnLogin():
    try:
        objResult = callMethodUser.login()
        return objResult
    except Exception as e:
        print("Error al hacer login:", e)
        return jsonify(ResponseMessage.message500)
    
@app.route('/chisme', methods=['GET'])
def fnGetChisme():
    try:
        objResult = callMethodPost.getChisme()
        return objResult
    except Exception as e:
        print("Error al buscar chisme:", e)
        return jsonify(ResponseMessage.message500)


@app.route('/newchisme', methods=['POST'])
def fnPostChisme():
    try:
        objResult = callMethodPost.postChisme()
        return objResult
    except Exception as e:
        print("Error al crear chisme:", e)
        return jsonify(ResponseMessage.message500)
    

@app.route('/newuser', methods=['POST'])
def fnPostUser():
    try:
        objResult = callMethodUser.postUsuario()
        return objResult
    except Exception as e:
        print("Error al crear Usuario:", e)
        return jsonify(ResponseMessage.message500)
    


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

    
