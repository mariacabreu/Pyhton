#Função
def adicionar_item():
    codigo = input ("Código: ")
    descricao = input ("Descrição: ")
    fabricante = input ("Fabricante: ")
    preco = input ("Preço: ")

    with open ("estoque.txt", "a") as arquivo:
        arquivo.write (f"{codigo}, {descricao}, {fabricante}, {preco}\n")   
    print( "Item adicionado com sucesso!")

def listar_estoque():
    with open ("estoque.txt", "r") as arquivo:
        print ("--- ESTOQUE ---")
        for linha in arquivo:
            codigo, descricao, fabricante, preco = linha.strip().split(", ")
            print (f"Código: {codigo} | Descrição: {descricao} | Fabricante: {fabricante} | Preço: {preco}")

def menu():
    while True:
        print ("--- MENU ESTOQUE ---")
        print ("1. Adicionar item")
        print ("2. Sair")
        opcao = input ("Escolha uma opção: ")
        if opcao == "1":
            adicionar_item()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente")
    menu()