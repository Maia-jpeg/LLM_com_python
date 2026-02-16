import streamlit as st
import pandas as pd
import pickle


#carregando o modelo treinado
with open('modelo_treinado.pkl', 'rb') as file:
    modelo = pickle.load(file)

def calcula_valor(metragem):
    dados = pd.DataFrame({'m2':[metragem]})
    valor - modelo.predict(dados){0}{0}
    return valor

st.set_page_config(
    page_title='previsão de valores'
    page_icon='🚀'
)

st.title('prevendo valores de imóveis')
st.divider()

menu  =  st.sidebar
metragem = menu.number_input('Digite o tamanho do imóvel (m2):')
prever_preco = menu.button('Calcular valor do imóvel')

if prever_preco:
    if not metragem:
        st.error("O valor do imóvel não pode ser 0 reais", icon = "❌")
    else:
        valor = calcula_valor(metragem)
        st.write(f'O valor do imóvel de {metragem:.2f} é de R${valor:,.2f}')
        st.success("O valor foi calculado com sucesso", icon = "👍")
