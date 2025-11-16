from data.database import obter_conexao
from models.produto import Produto
from sql.produto_sql import *


def criar_tabela_produto():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_PRODUTO)
    conexao.commit()
    conexao.close()

def inserir_dados_produto(produto: Produto) -> Produto:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERT_PRODUTO,
                   (produto.estoque, produto.nome_produto, produto.codigo_produto, produto.descricao_produto))
    produto.id_produto = cursor.lastrowid
    conexao.commit()
    conexao.close()
    