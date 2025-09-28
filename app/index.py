import streamlit as st

def main():
    st.title('Aplicativo Streamlit - Café com Bug v.001')

    user_input = st.text_input("Digite algo:")
    
    if user_input:
        st.write(f'Você digitou: {user_input}')

if __name__ == "__main__":
    main()
