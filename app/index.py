import streamlit as st

def main():
    st.title('Aplicativo Simples com ajuda do canal Café com Bug')

    user_input = st.text_input("Digite algo:")
    
    if user_input:
        st.write(f'Você digitou: {user_input}')

if __name__ == "__main__":
    main()
