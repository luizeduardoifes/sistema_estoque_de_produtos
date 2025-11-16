import sqlite3

def obter_conexao():
    conexao = sqlite3.connect("produto.db")
    return conexao