import streamlit as st
import sqlite3

st.set_page_config(layout="wide")

# Função para inserir os dados no banco de dados
def inserir_dados(mes, valor, forma_pagamento, categoria, descricao):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO transacoes (Mes, Valor, Forma_de_pagamento, Categoria, Descricao)
    VALUES (?, ?, ?, ?, ?)
    ''', (mes, valor, forma_pagamento, categoria, descricao))
    conn.commit()
    conn.close()

# Título do Dashboard
st.title("Adicionar gastos")

# Criando o formulário para adicionar gastos
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes = st.selectbox("Mês", meses)
valor = st.number_input("Valor")
forma_pagamento = st.selectbox("Forma de pagamento", ["Cartão de crédito", "Pix", "Débito", "Boleto", "Recebimento"])
categoria = st.selectbox("Categoria", ["Receitas", "Habitação", "Automóvel", "Lazer", "Saúde", "Educação", "Assinaturas"])
descricao = st.text_area("Descrição")

# Botão para adicionar o gasto
if st.button("Adicionar gasto"):
    inserir_dados(mes, valor, forma_pagamento, categoria, descricao)
    st.write("Gasto adicionado com sucesso!")