\#\# Projeto: Aplicação Flask com Chatbot Llama e Análise de Imagem

### Descrição

Este projeto consiste em uma aplicação web construída com Flask que integra um chatbot alimentado pelo modelo Llama (via `llama-cpp-python`) e funcionalidades básicas de análise de imagem. A aplicação permite aos usuários interagir com um chatbot programável e realizar análises simples em imagens enviadas, como o cálculo do valor médio dos pixels.

### Funcionalidades

  * **Chatbot Llama:**
      * Utiliza o modelo Llama para gerar respostas textuais com base em prompts do sistema e entradas do usuário.
      * Configurável com prompts de sistema para personalizar o comportamento do chatbot.
      * Implementado usando a biblioteca `llama-cpp-python` para inferência eficiente.
  * **Análise de Imagem:**
      * Permite o upload de imagens através de uma interface web.
      * Realiza uma análise básica da imagem, calculando o valor médio dos pixels como exemplo.
      * Utiliza as bibliotecas `Pillow (PIL)` e `NumPy` para manipulação e análise de imagens.
  * **Interface Web:**
      * Frontend simples ( `index2.html` - incluído neste repositório) para interagir com o chatbot e realizar uploads de imagem.
      * Rotas Flask para servir a interface web e lidar com requisições de chat e upload de imagens via API.
  * **Endpoints API:**
      * `/chat`: Endpoint para interagir com o chatbot via requisições POST no formato JSON.
      * `/upload_image`: Endpoint para upload de imagens via requisições POST com formulário de dados (`multipart/form-data`).
      * `/train`:  Endpoint (implementação básica) para simular a adição de dados de treinamento (funcionalidade não totalmente implementada).

### Tecnologias Utilizadas

  * **Python:** Linguagem de programação principal.
  * **Flask:** Framework web para construir a aplicação.
  * **llama-cpp-python:**  Biblioteca Python para utilizar modelos Llama.
  * **Pillow (PIL):** Biblioteca de processamento de imagens.
  * **NumPy:** Biblioteca para computação numérica, especialmente para manipulação de arrays de imagens.
  * **Werkzeug:** Biblioteca utilitária para aplicações web Flask ( `secure_filename`).
  * **OS:** Biblioteca padrão do Python para interações com o sistema operacional (criação de diretórios, manipulação de paths).

### Pré-requisitos

Antes de executar a aplicação, certifique-se de ter os seguintes pré-requisitos instalados:

1.  **Python 3.7+:** [Download Python](https://www.google.com/url?sa=E&source=gmail&q=https://www.python.org/downloads/)
2.  **pip:** Gerenciador de pacotes Python (geralmente incluído com a instalação do Python).

### Instalação e Configuração

1.  **Clone o repositório:**

    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DO_REPOSITORIO]
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

    Certifique-se de ter criado um arquivo `requirements.txt` com o seguinte conteúdo:

    ```
    Flask
    llama-cpp-python
    Werkzeug
    Pillow
    numpy
    ```

4.  **Baixe o modelo Llama:**

    O script está configurado para utilizar o modelo `Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf`. Você precisará baixar este modelo (ou outro modelo compatível com `llama-cpp-python`) e colocá-lo no diretório `qwen_model/`.

    Crie o diretório `qwen_model` na raiz do projeto, caso não exista:

    ```bash
    mkdir qwen_model
    ```

    E então, coloque o arquivo do modelo dentro deste diretório:

    ```
    qwen_model/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf  (Exemplo - o nome e a fonte do modelo podem variar)
    ```

    **Observação:** A localização do modelo é definida no script no seguinte trecho:

    ```python
    class LLMHandler:
        def __init__(self, model_path="qwen_model/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf"):
            # ...
    ```

    Você pode alterar o `model_path` se necessário.

5.  **Frontend:**

    Este repositório inclui o arquivo `index2.html`.
    
      * Formulários para inserir o prompt do sistema e a entrada do usuário para o chatbot.
      * Um campo para exibir a resposta do chatbot.
      * Um campo de upload de arquivo para imagens.
      * Um local para exibir o resultado da análise da imagem.

    Salve o arquivo `index2.html` no diretório `templates/` (crie o diretório `templates` se não existir).

### Executando a Aplicação

1.  **Execute o script Python:**

    ```bash
    python seu_script.py  # Substitua 'seu_script.py' pelo nome do seu arquivo Python (ex: app.py)
    ```

    A aplicação Flask será iniciada e estará acessível no endereço `http://0.0.0.0:5000/` (ou `http://localhost:5000/`).

### Utilização

1.  **Interface Web:**

      * Abra o navegador web e acesse `http://0.0.0.0:5000/`.
      * Utilize a interface em `index2.html` para:
          * Interagir com o chatbot inserindo prompts e mensagens.
          * Enviar imagens para análise.
          * Visualizar as respostas do chatbot e os resultados da análise de imagem.

2.  **Endpoints API (para uso programático):**

      * **Chatbot (`/chat`):**

          * Método: `POST`
          * Headers: `Content-Type: application/json`
          * Corpo (JSON):
            ```json
            {
              "system_prompt": "Você é um assistente especializado em...",
              "user_input": "Qual a sintaxe de um loop for em Python?"
            }
            ```
          * Resposta (JSON):
            ```json
            {
              "response": "Resposta do chatbot aqui..."
            }
            ```

      * **Upload de Imagem (`/upload_image`):**

          * Método: `POST`
          * Headers: `Content-Type: multipart/form-data`
          * Corpo: Formulário de dados com um campo chamado `image` contendo o arquivo de imagem.
          * Resposta (JSON):
            ```json
            {
              "message": "Imagem recebida com sucesso!",
              "analysis": "A média dos valores dos pixels da imagem é: XX.XX"
            }
            ```

      * **Treinamento (`/train`):**

          * Método: `POST`
          * Headers: `Content-Type: application/json`
          * Corpo (JSON):
            ```json
            {
              "training_data": "Dados de treinamento em formato JSON ou texto..."
            }
            ```
          * Resposta (JSON):
            ```json
            {
              "message": "Dados de treinamento adicionados com sucesso!"
            }
            ```
            **Observação:** A funcionalidade de treinamento está apenas parcialmente implementada e não irá efetivamente treinar o modelo Llama neste script.

### Considerações 

  * **Frontend:**Frontend `index2.html` mais completo e amigável para melhorar a experiência do usuário.
  * **Análise de Imagem:** Expandir as funcionalidades de análise de imagem para incluir tarefas mais complexas, como detecção de objetos, classificação de imagens, etc.
  * **Treinamento do Modelo:** Implementar uma lógica real de fine-tuning ou treinamento do modelo Llama com novos dados. Isso pode envolver a adaptação do script para lidar com o processo de treinamento e a integração de bibliotecas ou APIs apropriadas.
  * **Otimização e Escalabilidade:**  Para aplicações de maior escala, considerar otimizar o código para performance, especialmente a inferência do modelo Llama.


### Contribuição

Contribuições são bem-vindas\! Sinta-se à vontade para abrir Issues e Pull Requests para melhorias, correções de bugs e novas funcionalidades.

