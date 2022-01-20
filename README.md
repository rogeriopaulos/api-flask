# Count Vowels
API em Flask que retorna a contagem de vogais a partir de uma lista de strings.

## Instalação

### Pré-requisitos

**Obrigatório**:
- Python 3.8+

**Opcionais**:
- Docker
- docker-compose

### Instalando localmente no modo de desenvolvimento

Para rodar a aplicação localmente (no modo de desenvolvimento), siga os seguintes passos:

1. Crie um ambiente virtual do Python.

Para maiores informações sobre como criar, acesse esse (link)[https://docs.python.org/pt-br/3/tutorial/venv.html].

_Ps: Ative o ambiente virtual antes de executar os próximos passos._

2. Instale as dependências da aplicação.

Na raiz do projeto, execute:
```
pip install -r requirements/local.txt
```

3. Configure as variavéis de ambiente abaixo.

- FLASK_APP=app:create_app
- FLASK_ENV=development

Por exemplo, no linux execute os seguintes comandos:

```
export FLASK_APP=app:create_app
export FLASK_ENV=development
```

4. Rodando o servidor web.

Na raiz do projeto, execute:

```
flask run
```

### Instalando com Docker (ambiente de produção)

(...)


## Documentação
(...)

## Testes

Para rodar os testes unitários da aplicação, execute:

```
pytest test_views.py -v
```

## Demo
(...)
