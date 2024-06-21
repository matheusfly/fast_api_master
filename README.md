# 📋 Gerenciador de Tarefas com FastAPI

Bem-vindo ao projeto **Gerenciador de Tarefas com FastAPI**! Este repositório é parte da minha trilha de aprendizado em backend Python, onde iremos iniciar nossos conhecimentos em transmissão de dados pela web utilizando o FastAPI.

## 📚 Sobre o Projeto

O objetivo deste projeto é facilitar o aprendizado no desenvolvimento de APIs com FastAPI. Vamos explorar como integrar bancos de dados, criar testes e implementar um sistema básico de autenticação. Este curso prático fornecerá uma base sólida para quem deseja trabalhar com essa tecnologia.

### 📌 Objetivos

- **Integrar Bancos de Dados**: Utilizando Pydantic e SQLAlchemy.
- **Criar Testes**: Com pytest e coverage.
- **Sistema de Autenticação**: Para proteger nossas rotas.
- **Deploy da Aplicação**: Utilizando Docker e Fly.io.

## 🚀 Tecnologias Utilizadas

Para a construção do projeto, utilizaremos as versões mais recentes das ferramentas disponíveis em 2024:

- **FastAPI** 0.100
- **Pydantic** 2.0
- **SQLAlchemy ORM** 2.0
- **Python** 3.11
- **Alembic** (Gerenciamento de Migrações)
- **pytest** (Testes)
- **Docker** (Containerização)
- **Fly.io** (Deploy)

## 🛠️ Configuração do Ambiente de Desenvolvimento

### 1. Clonando o Repositório

```bash
git clone https://github.com/matheusfly/fast_api_master
cd fast_api
```
### 2. Ativando pyenv

´´´bash
pyenv global 3.12.4
´´´

### 3. Instalando e Ativando o Poetry

Certifique-se de ter o [Poetry](https://python-poetry.org/docs/#installation) instalado em seu sistema. Então, instale as dependências:

```bash
poetry install
```

### 4. Ativando o Ambiente Virtual do Poetry

```bash
poetry shell
```

### 4. Iniciando o Servidor de Desenvolvimento

Utilize o comando `fastapi dev` para iniciar o servidor de desenvolvimento:

```bash
fastapi dev api_master/main.py
```

## 🏗️ Estrutura do Projeto

### 1. Primeiros Passos com FastAPI e TDD

Após configurar o ambiente, mergulharemos na estrutura básica de um projeto FastAPI e faremos uma introdução detalhada ao Test Driven Development (TDD).

### 2. Modelagem de Dados com Pydantic e SQLAlchemy

Aprenderemos a criar e manipular modelos de dados utilizando Pydantic e SQLAlchemy, dois recursos que levam a eficiência do FastAPI a outro nível.

### 3. Autenticação e Autorização em FastAPI

Construiremos um sistema de autenticação completo para proteger nossas rotas e garantir que apenas usuários autenticados tenham acesso a certos dados.

### 4. Testando sua Aplicação FastAPI

Faremos uma introdução detalhada aos testes de aplicação FastAPI, utilizando as bibliotecas pytest e coverage.

### 5. Dockerizando e Fazendo Deploy de sua Aplicação FastAPI

Aprenderemos como "dockerizar" nossa aplicação FastAPI e fazer seu deploy utilizando Fly.io.

## 📂 Estrutura de Diretórios

```plaintext
gerenciador-de-tarefas-fastapi/
├── api_master/
│   ├── __init__.py
│   ├── main.py
│   ├── .coverage
├── tests/
│   ├── __init__.py
│   ├── test_main.py
├── .gitignore
├── .pytest_cache/
├── .ruff_cache/
├── poetry.lock
├── pyproject.toml
└── README.md
```

## 👥 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## 📧 Contato

Se você tiver alguma dúvida ou sugestão, entre em contato pelo email: [seu-email@exemplo.com](mailto:seu-email@exemplo.com).

---

**Estudos e Codificação!** 🚀