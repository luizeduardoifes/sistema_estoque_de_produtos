CREATE_TABLE_PRODUTO = """
CREATE TABLE IF NOT EXISTS Produto (
    estoque INTEGER NOT NULL,
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    codigo_barra_produto INTEGER NOT NULL,
    descricao_produto TEXT NOT NULL  
);
"""

INSERT_PRODUTO = """
INSERT INTO Produto (estoque, nome_produto, codigo_barra_produto, descricao_produto)
VALUES(?, ?, ?, ?)
"""

DELETE_PRODUTO_POR_CODIGO_BARRA = """
DELETE FROM Produto
WHERE codigo_barra_produto = ?;
"""

GET_PRODUTO_BY_CODIGO_BARRA = """
SELECT estoque, id_produto, nome_produto, codigo_barra_produto, descricao_produto
FROM Produto
WHERE codigo_barra_produto = ?;
"""