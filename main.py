import os
import sqlite3
import time
from models.produto import Produto
from repo.produto_repo import *

criar_tabela_produto()

def inserir_produto():
    while True:
        os.system("cls")
        estoque = input("insere estoque inicial: ")
        nome_produto = input("Insere o nome do produto: ")
        codigo_barra_produto = input("insere o código de barra do produto: ")
        descricao_produto = input("Insere a descrição do produto: ")
        
        if not estoque.strip() or not nome_produto.strip() or not codigo_barra_produto.strip() or not descricao_produto.strip():
            print("ERROR,campo vazio,não foi possível salvar os dados")
            time.sleep(3)
            continue
            
        
        try:
            int(estoque)
        except ValueError:
            return "ERROR! o estoque tem que ser número inteiro"
        try:
            int(codigo_barra_produto)
        except ValueError:
            return "ERROR! o código de barras do produto tem que ser número inteiro"
        
        else:    
            insert = Produto(estoque = estoque, id_produto = 0,nome_produto = nome_produto, codigo_barra_produto = codigo_barra_produto, descricao_produto = descricao_produto)
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
        
def delete_produto():
    while True:
        os.system("cls")
        conn = sqlite3.connect("produto.db")
        cursor = conn.cursor()
        codigo_barra = input("Digite o código de barra do produto: ")
        cursor.execute("SELECT * FROM produto WHERE codigo_barra_produto = ?", (codigo_barra,))
        resultado = cursor.fetchone()
        os.system("cls")
        
        if resultado:
            print(obter_produto_por_codigo(codigo_barra))
            print("deseja deletar este item?")
            opcao = input("").lower()
            if opcao == "sim":
                deletar_produto(codigo_barra)
                print("produto deletado com suceeso!!!,deseja fazer outro procedimento?")
                opcao2 = input().lower()
                if opcao2 == "sim":
                    continue
                elif opcao2 == "nao":
                    return
                else:
                    print("ERROR!!!,tem quer usar apenas o sim ou nao")
            
        
        else:
            print("Error, não existe esse produto no sistema!!!")
            print("aperte o enter para voltar no procedimento")
            input()
            continue
            
                
        try:
            int(codigo_barra)
        except ValueError:
            print("ERROR!!!, o código de barra tem que ser número inteiro,aperte enter e tente novamente")
            input()
            print("retornando ao procedimento...")
            time.sleep(3)
            continue
    
    
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
            
            case 2:
                delete_produto()
                
            


if __name__ == "__main__":
    main()