# aula16_bootcamp
# 📍 Consulta de CEP com Python

Projeto desenvolvido durante a **Jornada de Dados**, adaptado de um exercício que utilizava a API de Pokémon. A proposta foi aplicar os mesmos conceitos em um exemplo mais próximo de uma situação real: consultar um CEP, validar os dados e armazená-los em um banco de dados.

📌 Sobre a adaptação

O projeto foi desenvolvido a partir da estrutura apresentada na aula, originalmente utilizando a API de Pokémon. Como exercício de aprendizado, adaptei a aplicação para um contexto mais próximo de uma situação real, utilizando a API ViaCEP para consultar e armazenar informações de endereços.


## 🎯 Objetivo

A aplicação permite:

- Receber um CEP informado pelo usuário;
- Consultar os dados através da API ViaCEP;
- Validar e organizar os dados com Pydantic;
- Salvar as informações em um banco SQLite;
- Evitar o cadastro duplicado de um mesmo CEP.

## 🛠️ Tecnologias

- **Python**
- **Poetry** — gerenciamento do ambiente e dependências
- **Requests** — requisições à API
- **Pydantic** — validação dos dados
- **SQLAlchemy** — interação com o banco de dados
- **SQLite** — banco de dados
- **ViaCEP** — API de consulta de CEP

## 📂 Estrutura

```text
.
├── main.py
├── controller.py
├── schema.py
├── models.py
├── db.py
├── cep.db
├── pyproject.toml
└── poetry.lock
```

- **main.py** — controla o fluxo principal e a interação com o usuário.
- **controller.py** — consulta a API e salva os dados no banco.
- **schema.py** — define e valida a estrutura dos dados recebidos.
- **models.py** — define a estrutura da tabela no banco usando SQLAlchemy.
- **db.py** — configura a conexão e as sessões do banco.
- **cep.db** — banco de dados SQLite.

## 🔄 Fluxo da aplicação

```text
Usuário digita o CEP
        ↓
main.py
        ↓
Consulta à API ViaCEP
        ↓
Dados recebidos em JSON
        ↓
CepSchema (validação)
        ↓
Cep Model
        ↓
SQLAlchemy
        ↓
Banco SQLite (cep.db)
```

## 💡 Exemplo

Entrada:

```text
50710435
```

Saída:

```text
CEP encontrado: 50710-435
Logradouro: Rua José Bonifácio
Bairro: Madalena
Cidade: Recife
Estado: PE
```

## 📚 O que aprendi

- Consumo de APIs externas;
- Requisições HTTP com `requests`;
- Manipulação de dados JSON;
- Validação com Pydantic;
- Modelagem de dados com SQLAlchemy;
- Conexão com banco SQLite;
- Organização de um projeto Python;
- Separação de responsabilidades entre arquivos;
- Tratamento de registros duplicados.

## Sobre o projeto

Este projeto faz parte dos meus estudos em **Python aplicado a dados**. A adaptação do exercício original de Pokémon para um sistema de consulta de CEP foi feita como forma de compreender melhor a estrutura do projeto e aplicar os conceitos em um contexto diferente.
