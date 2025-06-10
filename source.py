import sqlite3

def adicionar_autor():
    nome = input("Nome do autor: ")
    nacionalidade = input("Nacionalidade: ")
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
    conn = sqlite3.connect("bibliodb.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO autor (nome, nacionalidade, data_nascimento) VALUES (?, ?, ?)",
        (nome, nacionalidade, data_nascimento)
    )
    conn.commit()
    conn.close()
    print("Autor adicionado com sucesso!")

def adicionar_livro():
    nome = input("Nome do livro: ")
    ano_lanc = input("Ano de lançamento: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")
    isbn = input("ISBN: ")
    status = input("Status: ")
    favoritado = input("Favoritado (S/N): ")
    editora = input("Editora: ")
    data_cadastro = input("Data de cadastro (AAAA-MM-DD): ")
    conn = sqlite3.connect("bibliodb.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO livros (nome, ano_lanc, autor, genero, isbn, status, favoritado, editora, data_cadastro) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (nome, ano_lanc, autor, genero, isbn, status, favoritado, editora, data_cadastro)
    )
    conn.commit()
    conn.close()
    print("Livro adicionado com sucesso!")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar autor")
        print("2 - Adicionar livro")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_autor()
        elif opcao == "2":
            adicionar_livro()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()