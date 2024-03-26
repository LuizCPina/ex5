import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['biblioteca']
collection = db['livros']

def inserir_livro():
    livro = {
        "_id": input("ID do livro: "),
        "titulo": input("Título: "),
        "autor": input("Autor: "),
        "ano": int(input("Ano: ")),
        "preco": float(input("Preço: "))
    }
    collection.insert_one(livro)
    print("Livro inserido!")

def listar_livros():
    for livro in collection.find():
        print(livro)

def atualizar_livro():
    livro_id = input("ID do livro a ser atualizado: ")
    novo_valor = {"$set": {
        "titulo": input("Novo Título: "),
        "autor": input("Novo Autor: "),
        "ano": int(input("Novo Ano: ")),
        "preco": float(input("Novo Preço: "))
    }}
    collection.update_one({"_id": livro_id}, novo_valor)
    print("Livro atualizado!")

def remover_livro():
    livro_id = input("ID do livro a ser removido: ")
    collection.delete_one({"_id": livro_id})
    print("Livro removido!")

def menu():
    while True:
        print("\nMenu CRUD - livros")
        print("1 - Inserir Livro")
        print("2 - Atualizar Livro")
        print("3 - Remover Livro")
        print("4 - Listar Livros")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        def switch_case(opcao):
            return {
                '1': inserir_livro,
                '2': atualizar_livro,
                '3': remover_livro,
                '4': listar_livros,
                '5': print("Saindo..."),
            }.get(opcao, print("Opção inválida. Por favor, escolha uma opção válida."))()

        switch_case(opcao)

if 'name' == "_main_":
    menu()