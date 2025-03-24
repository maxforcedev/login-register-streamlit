import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
import bcrypt

load_dotenv()

def conectar():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")

        )

        return conn
    except psycopg2.OperationalError as e:
        print(f"Erro operacional ao conectar: {e}")
    except psycopg2.ProgrammingError as e:
        print(f"Erro de programação ao conectar: {e}")
    except Exception as e:
        print(f"Erro inesperado ao conectar: {e}")
    return None


def verificar_login(email, senha):
    try:
        
        conn = conectar()
        cur = conn.cursor()

        cur.execute("SELECT senha FROM usuarios WHERE email = %s", (email,))
        resultado = cur.fetchone()

        conn.close()
        cur.close()
        if resultado:
            if bcrypt.checkpw(senha.encode('utf-8'), resultado[0].encode('utf-8')):
                return True
            else:
                return False
        else:
            return False

    except Exception as e:
        print(f"OCORREU UM ERRO: {e}" )


def validar_inputs(nome, email, senha, confirmar_senha):
    erros = []
    conn = conectar()
    cur = conn.cursor()

    if nome == "":
        erros.append("O campo 'Nome' deve ser preenchido.")
    
    elif email == "" or '@' not in email or '.com' not in email:
        erros.append("Email invalido.")

    elif senha != confirmar_senha:
        erros.append("As senhas nao se conferem.")

    elif email:
        email = cur.execute("SELECT email FROM usuarios WHERE email = %s", (email,))
        email = cur.fetchone()
        if email and email != None:
            erros.append("Esse email ja existe.")
            conn.close()    
            cur.close()
    
    return erros


def cadastrar_usuario(nome, email, senha):
    conn = conectar()
    cur = conn.cursor()
    senha = (bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())).decode('utf-8')

    cur.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))

    conn.commit()
    conn.close()    
    cur.close()


