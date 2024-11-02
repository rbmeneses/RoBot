# RoBot
ChatBot com inteligencia artificial treinada localmente
Estrutura do Projeto
O projeto será estruturado da seguinte maneira:

├── app.py              # Backend Flask para lidar com as requisições
├── templates/
│   └── index.html      # Frontend HTML e JavaScript
└── static/
    └── style.css       # Estilos CSS para o frontend (opcional)
1. Instale o Flask
Primeiro, instale o Flask:
pip install flask
pip install requests

Executar o Projeto
No terminal, dentro da pasta do projeto, execute o servidor Flask:
python app.py
Acesse http://127.0.0.1:5000 no navegador para abrir o frontend.

Requisitos.
Lm Studio instalado e servidor ativo
AnythingLLm instalado e configurado
Obs: Alterar o nome de seu workspace dentro da URL de comunicação e sua chave de API.
Ex. "http://seu_servidor:3001/api/v1/workspace/seu_workspace/chat"  ----   AUTH_TOKEN = "Y0S7Z8X-5P84THA-G7EQBD1-ZTFN6CT"
Obs2: Estruturar o projeto dentro das pastas correspondentes.
