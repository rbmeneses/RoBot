from flask import Flask, request, jsonify, render_template
from llama_cpp import Llama
import os
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np

# Configuração do Flask
app = Flask(__name__)

# Configuração do diretório de uploads
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Inicialização do modelo Llama
class LLMHandler:
    def __init__(self, model_path="qwen_model/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf"):
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,          # Tamanho do contexto
            n_threads=4,         # Número de threads (CPU)
            n_gpu_layers=20      # Camadas para GPU (use 0 para CPU apenas)
        )

    def generate_response(self, system_prompt, user_input):
        prompt = f"""<|im_start|>system
        {system_prompt}<|im_end|>
        <|im_start|>user
        {user_input}<|im_end|>
        <|im_start|>assistant
        """

        output = self.llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
            temperature=0.2,  # Mais determinístico
            stop=["<|im_end|>"]
        )
        return output['choices'][0]['message']['content']

# Criando instância do modelo
llm = LLMHandler()

# Rota para servir o frontend
@app.route('/')
def index():
    return render_template('index2.html')

# Rota para o chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    system_prompt = data.get("system_prompt", "Você é um assistente de programação especializado em Python.")
    user_input = data.get("user_input", "")
    
    response = llm.generate_response(system_prompt, user_input)
    return jsonify({"response": response})

# Função para analisar a imagem
def analyze_image(image_path):
    try:
        # Abre a imagem
        image = Image.open(image_path)
        
        # Converte a imagem para um array numpy
        img_array = np.array(image)
        
        # Exemplo de análise: calcula a média dos valores dos pixels
        mean_value = np.mean(img_array)
        
        # Retorna uma análise simples
        return f"A média dos valores dos pixels da imagem é: {mean_value:.2f}"
    except Exception as e:
        return f"Erro ao analisar a imagem: {str(e)}"

# Rota para upload de imagem
@app.route("/upload_image", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "Nenhuma imagem enviada"}), 400
    
    image = request.files["image"]
    filename = secure_filename(image.filename)
    image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    image.save(image_path)

    # Analisa a imagem
    analysis_result = analyze_image(image_path)

    return jsonify({"message": "Imagem recebida com sucesso!", "analysis": analysis_result})

# Rota para inserir dados de treinamento
@app.route("/train", methods=["POST"])
def train():
    data = request.json
    new_training_data = data.get("training_data", "")

    if not new_training_data:
        return jsonify({"error": "Nenhum dado fornecido"}), 400

    # Aqui pode ser adicionada a lógica para treinar o modelo com os novos dados
    return jsonify({"message": "Dados de treinamento adicionados com sucesso!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)