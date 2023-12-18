# BUSCADOR DE CEP

## BUSCADOR DE  CEP USANDO API E STREAMLIT

Este é um app web que utiliza o sistema API do via cep e o streamlit para, através de um CEP válido,  determinar o destino: logradouro, cidade, UF, etc...

### INSTALAÇÃO E EXECUÇÃO
1. Primeiro baixe esse repositório com o comando
~~~python
git clone https://github.com/elizeubarbosaabreu/app-com-streamlit.git
~~~

2. Crie uma máquina virtual e instale as dependências com os comandos:
~~~python
cd app-com-streamlit/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~
 **Obs: dependendo a versão ou seu sistema operacional o trecho 'python3' pode variar para 'python', 'python2', etc...**

3. Para rodar a aplicação, basta digitar o código abaixo:

~~~python
streamlit run app.py
~~~

Obrigado por usar o sistema. Sinta-se á vontade para modificá-lo e adaptá-lo à sua realidade...