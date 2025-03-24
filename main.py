import streamlit as st
import time
from models import verificar_login, validar_inputs, cadastrar_usuario


def iniciar_login():

    def alternar_form():
        if st.session_state.form == "login":
            st.session_state.form = "cadastro"
        else:
            st.session_state.form = "login"


    try: 
        if "form" not in st.session_state:
            st.session_state.form = "login"
        
        tab1, tab2 = st.tabs(['Entrar', 'Cadastrar'])

        with tab1.form("Realizar Login", enter_to_submit=True):
                st.title("Realizar :blue[Login] 🔒")
                st.markdown("Que bom em te ver novamente 🥰")
                st.divider()

                email = st.text_input("Email")
                senha = st.text_input("Senha", type="password")

                submitted = st.form_submit_button("Entrar")
                if submitted:
                    if verificar_login(email, senha):
                        st.success("Login bem-sucedido!")
                        # PAGINA DE ENTRADA (ACESSO CONFIRMADO)
                    else:
                        st.error("Email ou senha incorretos")
                        st.write("Não tem uma conta? Crie sua conta já!")
                        
        

        
        with tab2.form("Crie sua conta"):
                
                st.title(":blue[Cadastrar] conta! 📝")
                st.markdown("Otimo em ter você conosco.", )

                st.divider()

                nome = st.text_input("Nome")
                email = st.text_input("Email")
                col1, col2 = st.columns(2)
                senha = col1.text_input("Senha", type="password")
                confirmar_senha = col2.text_input("Confirme sua senha", type="password")

                submitted = st.form_submit_button("Criar conta")
                if submitted:
                    erros = validar_inputs(nome, email, senha, confirmar_senha)
                    if erros:
                        for erro in erros:
                            st.warning(erro)
                    else:
                        st.success("Cadastro realizado com sucesso!")
                        cadastrar_usuario(nome, email, senha)
                        time.sleep(2)
                        alternar_form() 
                        st.rerun()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    iniciar_login()
