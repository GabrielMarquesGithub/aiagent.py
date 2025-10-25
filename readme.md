# AiAgent uma api Gemini

Um script de linha de comando em Python que utiliza a API do Google Gemini para responder ou executar ações em arquivos via prompts do usuário. É possível saber a versão da api no arquivos /dir

## 1. Requisitos

Para executar este projeto, você precisará ter o seguinte:

- Python: O projeto é construído com o Python.
- Chave de API do Google Gemini: Você precisará de uma chave de API válida obtida através do [Google AI Studio](https://aistudio.google.com/) na opção [Get API Key](https://aistudio.google.com/api-keys).
- Acesso à internet ao executar o script (para chamar a API)

## 2. Instalação e Configuração

Siga estes passos para configurar seu ambiente de desenvolvimento.

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/GabrielMarquesGithub/aiagent.py.git
cd aiagent.py
```

### Passo 2: Adicionar a chave da API (GEMINI_API_KEY)

2. No diretório do projeto existe um arquivo de exemplo `.env.example`. Crie o arquivo `.env` a partir dele
3. Edite o `.env` e adicione a variável `GEMINI_API_KEY` a sua chave da API do Google Gemini

### Passo 3: Instalação das dependências

3.1. (opcional, recomendado) Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

3.2. Instale dependências:

```bash
pip install -r requirements.txt
```

O arquivo requirements.txt incluído neste repositório contém as seguintes libs:

- google-genai
- python-dotenv

## Como rodar

Uso básico:

```bash
python main.py "<user_prompt>"
```

Com flag de verbose (imprime tokens, interações e logs extras):

```bash
python main.py "<user_prompt>" --verbose
```
