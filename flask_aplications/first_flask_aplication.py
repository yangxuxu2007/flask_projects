from flask import Flask, request

app = Flask(__name__)

@app.route("/soma", methods=["POST"])
def metodo_post():
    dados_recebidos = request.get_json()
    numero1 = dados_recebidos['numero1']
    numero2 = dados_recebidos['numero2']
    resultado = numero1 + numero2
    return{'resultado': resultado}

#python -m flask --app first_flask_aplication run