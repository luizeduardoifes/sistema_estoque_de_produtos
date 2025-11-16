from dataclasses import dataclass

@dataclass
class Produto:
    estoque: int 
    id_produto: int
    nome_produto: str
    codigo_produto: int
    descricao_produto: str