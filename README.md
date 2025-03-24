
# Sistema de Autenticação - Streamlit

Este projeto é um sistema de autenticação simples desenvolvido em **Python** e **Streamlit**, com integração ao banco de dados **PostgreSQL**. Ele permite o cadastro e login de usuários, utilizando hashing de senha para maior segurança.

## 📋 Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente:

- **Python**  
- **PostgreSQL** 
- **Streamlit**  

## 🛠️ Instalação

### 1. Clonar o Repositório

Clone este repositório em sua máquina local:

```bash
git clone https://github.com/maxforcedev/login-register-streamlit
cd login-register-streamlit
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Banco de Dados PostgreSQL

1. **Criar Banco de Dados:**
   - Acesse o PostgreSQL:
     ```bash
     psql -U postgres
     ```
   - Execute o comando SQL para criar o banco de dados:
     ```sql
     CREATE DATABASE auth_system;
     ```

2. **Criar Tabela de Usuários:**
   - Acesse o banco de dados:
     ```bash
     \c auth_system
     ```
   - Crie a tabela `users`:
     ```sql
     CREATE TABLE users (
         user_id VARCHAR(255) PRIMARY KEY,
         password VARCHAR(255) NOT NULL
     );
     ```

### 5. Configurar Conexão com o Banco

Abra o arquivo `db.py` e ajuste as credenciais de acesso ao PostgreSQL:

```python
conn = psycopg2.connect(
    host="localhost",
    database="auth_system",
    user="postgres",
    password="SUA_SENHA_AQUI"
)
```

### 6. Executar o Projeto

Para rodar a aplicação, execute o seguinte comando:

```bash
streamlit run main.py
```

Agora, acesse a aplicação em seu navegador pelo endereço `http://localhost:8501`.

## 🚀 Funcionalidades

- **Cadastro de Usuários:**  
  Salva os usuários no banco de dados com senhas criptografadas.
  
- **Login Seguro:**  
  Verificação de credenciais e controle de sessão.

## 🔧 Tecnologias Utilizadas

- **Python**  
- **Streamlit**  
- **PostgreSQL**  
- **Psycopg2**  

---

Este projeto faz parte de um aprendizado contínuo com Python e banco de dados. Contribuições e melhorias são bem-vindas! 🎯
