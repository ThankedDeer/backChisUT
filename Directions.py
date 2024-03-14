from flask import Flask, jsonify
from flask_cors import CORS
import BackEnd.Functions.userFunctions as callMethod
import BackEnd.GlobalInfo.ResponseMessages as ResponseMessage

app = Flask(__name__)
CORS(app)


    
@app.route('/login', methods=['POST'])
def fnLogin():
    try:
        objResult = callMethod.login()
        return objResult
    except Exception as e:
        print("Error al hacer login:", e)
        return jsonify(ResponseMessage.err500)
    


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000, debug=True)
    
