import os
import time
from models.produto import Produto
from repo.produto_repo import *

criar_tabela_produto()

def inserir_produto():
    while True:
        os.system("cls")
        estoque = input("insere estoque inicial: ")
        nome_produto = input("Insere o nome do produto: ")
        codigo_produto = input("insere o código de barra do produto: ")
        descricao_produto = input("Insere a descrição do produto: ")
        
        if not estoque.strip() or not nome_produto.strip() or not codigo_produto.strip() or not descricao_produto.strip():
            print("ERROR,campo vazio,não foi possível salvar os dados")
            time.sleep(3)
            continue
            
        
        try:
            int(estoque)
        except ValueError:
            return "ERROR! o estoque tem que ser número inteiro"
        try:
            int(codigo_produto)
        except ValueError:
            return "ERROR! o código de barras do produto tem que ser número inteiro"
        
        else:    
            insert = Produto(estoque = estoque, id_produto = 0,nome_produto = nome_produto, codigo_produto = codigo_produto, descricao_produto = descricao_produto)
            inserir_dados_produto(insert)
            print("dados inseridos com sucesso!!!")
        
        time.sleep(2)
        print("deseja continuar fazendo operação?")
        print("apenas responde com 'S' ou 'N': ")
        
        opcao = input("").lower()
        
        if opcao == "s":
            print("voltando ao operação...")
            time.sleep(3)
            continue
        
        elif opcao == "n":
            print("voltando ao menu principal...")
            time.sleep(3)
            return
        
            

def main():
    while True:
        os.system("cls")
        
        print(f"{"-"*10} CONTROLE DE ESTOQUE DE PRODUTO {"-"*10}")
        print("1: inserir produtos novos\n2: excluir produto do estoque\n3: listar todos os produtos do estoque\n4: alterar produto")
        opcao = input("seleciona o numero:")
        
        if not opcao.strip():
            os.system("cls")  
            print("Tem que escolher uma opção")
            time.sleep(3)
            continue 

        
        try:
            opcao = int(opcao)
        except ValueError:
            os.system("cls")  
            print("ERROR, não pode ser letra")
            time.sleep(3)
            continue
            
        match opcao:
            case 1:
                inserir_produto()
                
            


if __name__ == "__main__":
    main()