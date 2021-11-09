import time 
import json
from json import JSONEncoder

# ==========================================TRABALHO DO THIAGO==========================================
global estoque
global contador_sinal
global carregar_flag
estoque = []
lista_produtos = []
contador_sinal = 0
contador = 0
carregar_flag = 0


class ProductEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

class Produto:
    def __init__(self, codigo, nome, descricao, valor):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

def gravar():
    global contador_sinal
    print("="*50)
    print(" ","\nGravando Arquivo Externo dos Produtos...")
    with open('data.json', 'w') as fp:
        if len(lista_produtos) == 0:
            print("\n\033[31mNADA PARA SER SALVO!\033[0m\n")
            return menu()
        else:
            json.dump(lista_produtos, fp, indent=4, cls=ProductEncoder)
    time.sleep(1)
    print(" ")
    print("\033[32mARQUIVO SALVO COM SUCESSO!\033[0m\n")
    fp.close()

    contador_sinal = 1
    
    return menu()

def carregar():
    global carregar_flag
    global contador
    global estoque
    global data
    global objetos
    with open('data.json', 'r') as fp:
        data = fp.read()
        objetos = json.loads(data)
    
    for obj in objetos:
        codigo = obj['codigo']
        nome = obj['nome']
        descricao = obj['descricao']
        valor = obj['valor']
        produto = Produto(codigo, nome, descricao, valor)

        estoque.append(produto.codigo)
        estoque.append(produto.nome)
        estoque.append(produto.descricao)
        estoque.append(produto.valor)

        lista_produtos.append(produto.__dict__)

    contador = (obj['codigo'])  
     
    print("\n\033[32mARQUIVO CARREGADO COM SUCESSO!\033[0m\n")
    carregar_flag = 1

    return menu() 

def cadastrar():
    print("="*50, "\nInsira os Dados para o cadastro do produto\n")
    global contador
    global contador_sinal
    global produto
    global resp
    
    if contador_sinal == 1:
        contador += 1
    else:
        contador += 1

    codigo = contador
    nome = str(input(f"Insira o nome: "))
    descricao = str(input("Insira a descrição: "))
    valor = float(input("Insira o valor: R$"))
    produto = Produto(codigo, nome, descricao, valor)
    estoque.append(produto.codigo)
    estoque.append(produto.nome)
    estoque.append(produto.descricao)
    estoque.append(produto.valor)

    lista_produtos.append(produto)

    print("Deseja inserir outro item:", "\n 1- SIM            2- NÃO")
    resp = int(input(""))
    
def listar():
    global filtrados
    global resp
    filtrados = []
    print("="*50, "\nInsira os Valores para Filtrar")
    val_min = float(input("Insira o valor Mínimo: "))
    val_max = float(input("Insira o valor Máximo: "))

    if  carregar_flag == 1:
        for obj in objetos:
            if obj['valor'] <= val_max and obj['valor'] >= val_min:
                filtrados.append(obj)
                print(f"Código: {obj['codigo']} - Nome: {obj['nome']} - Descrição: {obj['descricao']} - Valor: {obj['valor']}")
    else:
        for produto in lista_produtos:
            if produto.valor <= val_max and produto.valor >= val_min:
                filtrados.append(produto)
                print(f"Código: {produto.codigo} - Nome: {produto.nome} - Descrição: {produto.descricao} - Valor: {produto.valor}")


    if len(filtrados) == 0:
        print("\n\033[31mNENHUM PRODUTO ENCONTRADO!\033[0m\n")   

    print("Deseja filtrar outros itens:", "\n 1- SIM            2- NÃO")
    resp = int(input(""))

def menu():
    global opt
    print ("="*20 + "Void Store" + "="*20,"""\n 1) Cadastrar Produto \n 2) Consultar Produtos por Faixa de Preço \n 3) Gravar Produtos em Arquivo \n 4) Carregar Produtos do Arquivo \n 5) Sair""")

    opt = int(input("Selecione a Opção Desejada: "))

    while opt > 5 or opt < 1:
        error = "OPÇÃO INVÁLIDA"
        print (f"\033[31m{error}\033[0m")
        opt = int(input("Selecione a Opção Desejada: "))

    if opt == 1:
        cadastrar()
        while resp == 1:
            cadastrar()
        if resp == 2:
           return menu()

    if opt == 2:
        listar()
        while resp == 1:
            listar()
        if resp == 2:
            return menu()

    if opt == 3:
        gravar()

    if opt == 4:
        carregar()

    if opt == 5:
        print("\n\033[36mATÉ LOGO!\033[0m\n")
        exit()
        
menu()



    
    
    