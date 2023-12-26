# CRUD FastAPI

Este repositório contém uma aplicação FastAPI que oferece operações CRUD (Create, Read, Update, Delete) para filmes e gêneros (n:n). Utiliza o SQLAlchemy para gerenciamento de banco de dados e o Pydantic para validação de entradas.

## Instalação

1. Clone o repositório:

```
git clone https://github.com/caiython/crud-fastapi.git
```

2. Acesse o diretório do projeto:

```
cd crud-fastapi
```

3. Crie um ambiente virtual:

```
python -m venv venv
```

4. Ative o ambiente virtual:

- Windows
```
venv\Scripts\activate
```

- Unix ou MacOS
```
source venv/bin/activate
```

5. Instale as dependências:

```
pip install -r requirements.txt
```

## Uso

1. Execute a aplicação FastAPI:

```
uvicorn main:app --reload
```

Obs: A opção --reload permite o recarregamento automático do servidor em alterações de código durante o desenvolvimento.

2. Abra o seu navegador e acesse http://127.0.0.1:8000/docs para acessar a documentação Swagger da API.

3. Utilize a documentação Swagger fornecida para testar e interagir com as operações CRUD.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- 📂 app: Contém os arquivos principais do projeto.
    - 🐍 main: Define as rotas e endpoints da API.
    - 🐍 crud: Implementa as operações CRUD usando o SQLAlchemy.
    - 🐍 database: Contém código relacionado ao banco de dados.
    - 🐍 models: Define os modelos do SQLAlchemy.
    - 🐍 schemas: Define modelos Pydantic para validação de entradas.
- 📜 .gitignore: Arquivos que devem ser ignorados pelo git.
- 📄 README.md: Documentação do projeto.
- 📋 requirements.txt: Bibliotecas que são requisito para o uso do projeto.

## Tecnologias Utilizadas

- FastAPI: Um framework web moderno e rápido para construção de APIs com Python.
- SQLAlchemy: Um kit de ferramentas SQL e uma biblioteca de Mapeamento Objeto-Relacional (ORM).
- Pydantic: Uma biblioteca de validação de dados e gerenciamento de configurações.

## Contribuições

Sinta-se à vontade para contribuir com este projeto abrindo problemas (issues) ou requisições de pull (pull requests). Suas contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a Licença Pública Geral GNU (GNU GPL) - consulte o arquivo LICENSE para mais detalhes.