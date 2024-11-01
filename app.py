import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# URL e token de autorização fornecidos
ANYTHING_LLM_URL = "http://localhost:3001/api/v1/workspace/robot/chat"
AUTH_TOKEN = "Y0S7Z8X-5P84THA-G7EQBD1-ZTFN6CT"  # Token de autenticação fornecido

def get_response_from_anything_llm(prompt, session_id="identifier-to-partition-chats-by-external-id"):
    """
    Envia uma mensagem ao AnythingLLM e recebe uma resposta.
    """
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "message": prompt,
        "mode": "chat",
        "sessionId": session_id
    }

    try:
        response = requests.post(ANYTHING_LLM_URL, json=data, headers=headers)
        response.raise_for_status()  # Lança um erro para status HTTP ruins
        
        # Verifica e extrai o conteúdo da resposta dentro do JSON
        response_json = response.json()
        content = response_json.get("textResponse", "Nenhuma resposta encontrada.")
        return content
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao conectar ao AnythingLLM: {http_err}")
        return "Desculpe, ocorreu um erro ao tentar obter uma resposta."
    except Exception as err:
        print(f"Erro inesperado: {err}")
        return "Desculpe, ocorreu um erro ao tentar obter uma resposta."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    session_id = data.get("session_id", "identifier-to-partition-chats-by-external-id")

    # Obter resposta do AnythingLLM
    response = get_response_from_anything_llm(user_message, session_id)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
