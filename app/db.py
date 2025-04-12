import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Criando a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS transacoes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Mes TEXT,
    Valor REAL,
    Forma_de_pagamento TEXT,
    Categoria TEXT,
    Descricao TEXT
)
''')

# Salvando as alterações e fechando a conexão
conn.commit()
conn.close()