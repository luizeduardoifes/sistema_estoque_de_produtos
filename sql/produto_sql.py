CREATE_TABLE_PRODUTO = """
CREATE TABLE IF NOT EXISTS Produto (
    estoque INTEGER NOT NULL,
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    codigo_produto INTEGER NOT NULL,
    descricao_produto TEXT NOT NULL  
);
"""

INSERT_PRODUTO = """
INSERT INTO Produto (estoque, nome_produto, codigo_produto, descricao_produto)
VALUES(?, ?, ?, ?)
"""