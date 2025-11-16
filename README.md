# Sistema de Controle de Estoque de Produtos

## 📋 Descrição

Sistema em Python para gerenciar estoque de produtos com funcionalidades de cadastro, consulta, alteração e exclusão. O sistema utiliza código de barras como identificador único dos produtos e armazena os dados em um banco de dados SQLite.

## 🎯 Funcionalidades Principais

### 1. **Cadastrar Produto**
- Insere novos produtos no estoque
- Coleta as seguintes informações:
  - **Estoque Inicial**: quantidade de produtos em estoque (número inteiro)
  - **Nome do Produto**: denominação do produto
  - **Código de Barras**: identificador único do produto (número inteiro)
  - **Descrição**: detalhes sobre o produto
- Validação de campos vazios
- Validação de tipos numéricos

### 2. **Consultar Produtos**
- Lista todos os produtos cadastrados no estoque
- Exibe: código de barras, nome, descrição e quantidade em estoque
- Busca por código de barras específico

### 3. **Alterar Produto**
- Permite modificar informações de um produto existente
- Busca pelo código de barras
- Atualiza dados como: estoque, nome, descrição

### 4. **Deletar Produto**
- Remove produtos do estoque
- Busca pelo código de barras do produto a deletar

## 🏗️ Estrutura do Projeto

```
sistema de controle de estoque/
│
├── main.py                 # Arquivo principal com menu
├── README.md              # Este arquivo
│
├── models/
│   └── produto.py         # Modelo/classe Produto
│
├── repo/
│   └── produto_repo.py    # Operações com banco de dados
│
├── sql/
│   └── produto_sql.py     # Queries SQL
│
└── data/
    └── database.py        # Conexão com banco de dados
```

## 💾 Fluxo de Funcionamento

1. **Inicialização**: Cria tabela de produtos no banco de dados
2. **Menu Principal**: Apresenta 4 opções ao usuário
3. **Operações**: 
   - Opção 1: Entra em loop de cadastro
   - Opção 2: Deleta produtos
   - Opção 3: Lista produtos
   - Opção 4: Altera dados de produtos
4. **Persistência**: Todos os dados são salvos no banco de dados

## 🔑 Componentes Principais

### [models/produto.py](models/produto.py)
Classe `Produto` com atributos:
- `id_produto`: ID único no banco
- `nome_produto`: Nome do produto
- `codigo_produto`: Código de barras (identificador único)
- `estoque`: Quantidade disponível
- `descricao_produto`: Descrição detalhada

### [repo/produto_repo.py](repo/produto_repo.py)
Funções de operação:
- `criar_tabela_produto()`: Cria tabela no banco
- `inserir_dados_produto()`: Insere novo produto
- `listar_produtos()`: Lista todos
- `deletar_produto()`: Remove produto
- `alterar_produto()`: Atualiza produto

### [sql/produto_sql.py](sql/produto_sql.py)
Queries SQL para operações CRUD

### [data/database.py](data/database.py)
Gerencia conexão com SQLite

## ⚙️ Como Usar

1. Execute o programa:
   ```bash
   python main.py
   ```

2. Escolha uma opção no menu (1-4)

3. **Para cadastrar (opção 1)**:
   - Digite a quantidade de estoque
   - Digite o nome do produto
   - Digite o código de barras
   - Digite a descrição
   - Confirme se deseja continuar

4. **Para consultar (opção 3)**:
   - Visualize todos os produtos
   - Identifique pelo código de barras

5. **Para alterar (opção 4)**:
   - Informe o código de barras do produto
   - Atualize os dados desejados

6. **Para deletar (opção 2)**:
   - Informe o código de barras
   - Confirme exclusão

## ✅ Validações

- ✓ Campos não podem ser vazios
- ✓ Estoque deve ser número inteiro
- ✓ Código de barras deve ser número inteiro
- ✓ Menu rejeita entradas inválidas

## 🗄️ Banco de Dados

- **Sistema**: SQLite
- **Arquivo**: Criado automaticamente
- **Tabela**: produtos
- **Chave Primária**: código de barras (único)

## 🚀 Próximas Melhorias Sugeridas

- [ ] Busca por código de barras com autocomplete
- [ ] Relatórios de estoque baixo
- [ ] Histórico de movimentações
- [ ] Interface gráfica (tkinter ou PySimpleGUI)
- [ ] Sistema de permissões/usuários
- [ ] Exportar dados (PDF, Excel)

## 📝 Requisitos

- Python 3.6+
- SQLite3 (incluído no Python)

## 📧 Autor

Sistema desenvolvido para controle eficiente de estoque.