import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.set_page_config(layout="wide")
st.title("Tela de")
#Interface de Login

def main():

    ####Desabilitar tela de login
    #st.session_state['logged_in'] = True
    ####
    
    # Verificar se o usuário está logado
    if not is_user_logged_in():
        show_login_page()
    else:
        run_main_program()

def is_user_logged_in():
    # Verificar se o usuário está logado
    return st.session_state.get('logged_in', False)

def show_login_page():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == "admin" and password == "admin":
            st.session_state['logged_in'] = True
            st.experimental_rerun()  # Re-executar o aplicativo para atualizar a tela
        else:
            st.error("Invalid username or password")

def run_main_program():
    st.title("Logado") 
    st.write("Texto")

    #Checkbox
    texto= st.checkbox('Apresentar Texto')
    if texto:
        st.write("Texto")
    
    #Menu Lateral
    with st.sidebar:
        st.write("Texto")
        st.write("Maneiro")
    
    #Barras de arrastar
    linhas = st.slider("Quantidade de linhas", 1, 20)
    st.write(linhas)
    
    #Botões
    a = "Palmeiras não tem"
    button = st.button("botão")
    if button:
    	a= "Mundial"
    st.write(a)
    
    #Caixa de entrada
    num1= st.text_input("número")
    st.write(num1)
    
    #Multpiplas páginas - bootstrap-icons
    def pag1():
    	st.title("Página 1")
    def pag2():
    	st.title("Página 2")
    def pag3():
    	st.title("Página 3")
    
    with st.sidebar:
                selecao = option_menu(
                    "Menu",
                    ["Página 1", "Página 2", "Página 3"],
                    icons=['1-circle', '2-circle', '3-circle'],
                    menu_icon="cast",
                    default_index=0,
                )
    if selecao == 'Página 1':
        pag1()
    elif selecao == 'Página 2':
        pag2()
    elif selecao == 'Página 3':
        pag3()
    
    #Importar dados do excel
    file_path = r"Downloads\dados.xlsx"
    df = pd.read_excel(file_path)
    
    #Utilizando a barra de arrastar + Posicionando na tela
    with st.sidebar:
    	linhas = st.slider("Quantidade de linhas", 1, 20)
    col1, col2 = st.columns(2)
    with col1:
        st.write(df)        
    with col2:
        st.write(df.head(linhas))


if __name__ == "__main__":
    main()



