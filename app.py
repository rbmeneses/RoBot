import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# URL do backend e token
ANYTHING_LLM_URL = "http://127.0.0.1:3001/api/v1/workspace/robot/chat"
AUTH_TOKEN = "Y0S7Z8X-5P84THA-G7EQBD1-ZTFN6CT"  # Token de autenticação fornecido

def get_response_from_anything_llm(prompt, session_id="default-session-id"):
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
        # Envia a requisição ao endpoint do AnythingLLM
        response = requests.post(ANYTHING_LLM_URL, json=data, headers=headers)
        response.raise_for_status()  # Lança erro para status HTTP inadequados
        
        # Extrai o conteúdo da resposta JSON
        response_json = response.json()
        content = response_json.get("textResponse", "Nenhuma resposta encontrada.")
        return content
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao conectar ao AnythingLLM: {http_err}")
        return "Erro ao obter resposta do servidor."
    except Exception as err:
        print(f"Erro inesperado: {err}")
        return "Erro inesperado ao obter resposta."

@app.route("/")
def index():
    # Renderiza o arquivo HTML da interface (index.html) 
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    session_id = data.get("session_id", "default-session-id")  # Identificador único para sessões de usuário

    # Obter resposta do AnythingLLM
    response = get_response_from_anything_llm(user_message, session_id)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Permite acesso externo
