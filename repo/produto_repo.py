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
                   (produto.estoque, produto.nome_produto, produto.codigo_barra_produto, produto.descricao_produto))
    produto.id_produto = cursor.lastrowid
    conexao.commit()
    conexao.close()
    
def deletar_produto(codigo_barra: int) -> bool:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(DELETE_PRODUTO_POR_CODIGO_BARRA, (codigo_barra,))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)
    
    
def obter_produto_por_codigo(codigo_barra: int) -> Produto:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_PRODUTO_BY_CODIGO_BARRA, (codigo_barra,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return Produto(
            estoque=resultado[0],
            id_produto=resultado[1],
            nome_produto=resultado[2],
            codigo_barra_produto=resultado[3],
            descricao_produto=resultado[4]
        )    
    return None