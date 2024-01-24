# MB Fetch Coins

- [Instalação](#instalação)
  - [Usando Makefile and Docker](#usando-makefile-and-docker)
  - [Usando ambiente virtual](#usando-ambiente-virtual)
    - [Rodar Projeto](#rodar-projeto)
  - [Testes](#testes)
- [Documentação](#documentação)



## Instalação

### Clonar repositório
```
git clone https://github.com/wascellys/challege_mb.git
```

### Adicionar variáveis de ambiente

No diretório da aplicação, criar um arquivo .env e adicionar as seguintes variáveis:
```
DEBUG=True
BASE_URL_MB=https://store.mercadobitcoin.com.br/api/v1/marketplace/product/unlogged
BASE_URL_QUOTE=https://economia.awesomeapi.com.br/json/last/USD
```

## Usando Makefile and Docker
Na raiz do projeto, abra o terminal e execute o comando  
```
make api
```

## Usando ambiente virtual
#### Instalação do Python em terminal Linux
```
sudo apt install python3-pip python3-dev libpq-dev virtualenv
```
#### Criando virtualenv
```
virtualenv myenv --python=python3
```
#### Ativação da  virtualenv
```
source myenv/bin/activate
```
## Instalação das Dependências
```
pip install -r requirements.txt
```

## Rodar Projeto
No diretório raiz do projeto execute o comando:
```
python manage.py runserver
```

## Testes
No diretório do projeto execute o comando:
```
pytest -v
```

## Documentação
## Requisições HTTP
Toda requisição para a API são feitas por uma requisição HTTP usando para um dos seguintes métodos:

* `POST` Criar um recurso
* `PUT` Atualizar um recurso
* `GET` Buscar um ou uma lista de recursos
* `DELETE` Excluir um recurso

## Códigos de respostas HTTP
Cada resposta será retornada com um dos seguintes códigos de status HTTP:

* `201` `CREATED` A criação foi bem sucedida
* `200` `OK` A requisição foi bem sucedida
* `400` `Bad Request` Houve um problema com a solicitação (segurança, malformado, validação de dados, etc.)
* `401` `Unauthorized` As credenciais fornecidas à API são inválidas
* `403` `Forbidden` As credenciais fornecidas não têm permissão para acessar o recurso solicitado
* `404` `Not found` Foi feita uma tentativa de acessar um recurso que não existe
* `500` `Server Error` Ocorreu um erro no servidor


## Rotas
Os endpoints estão abertos, não precisam de autenticação

### Consultar valor de uma criptomoeda:

As informações das criptomeodas foram buscadas do seguinte endpoint do Mercado Bitcoin. 
```commandline
https://store.mercadobitcoin.com.br/api/v1/marketplace/product/unlogged
```
Endpoint de acesso as informações:

  - *Coin Infos: `POST` `/coin_infos/`*

Obs: deve ser passado a key _symbol_ no body.

Em caso de sucesso, o endpoint retornará:
ex: BTC

```commandline
{
	"coin_name": "Bitcoin",
	"symbol": "BTC",
	"coin_price": "198.489,34",
	"coin_price_dolar": "40.442,00",
	"date_consult": "2024-01-24 15:00:26"
}
```

Em caso de insucesso, o endpoint retorná uma mensagem de erro.
