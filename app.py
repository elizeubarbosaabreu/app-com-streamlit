import streamlit as st
import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    response = requests.get(url)

    if response.status_code == 200: 
        data = response.json()
        return data
    
    else:
        return None

st.title("Buscador de CEP")
st.write('---')

cep_input = st.text_input("Digite o CEP desejado:")

try:
    if st.button("Buscar"):
        if cep_input:
            endereco = buscar_cep(cep_input)
            if endereco:
                st.write(f"CEP: {endereco['cep']}")
                st.write(f"LOGRADOURO: {endereco['logradouro']}")
                st.write(f"COMPLEMENTO: {endereco['complemento']}")
                st.write(f"BAIRO: {endereco['bairro']}")
                st.write(f"CIDADE: {endereco['localidade']}")
                st.write(f"ESTADO: {endereco['uf']}")
            else:
                st.write('Verifique o CEP digitado...')
        else:
            st.write('Verifique o CEP digitado ou sua conexão à internet...')
except:
    st.write('Putz! Parece que esse CEP não existe...')

st.write('''
        ---
         Exemplo de CEP: 76916-000

         Aplicação desenvolvida por [Elizeu Barbosa Abreu](https://github.com/elizeubarbosaabreu)''')
        
