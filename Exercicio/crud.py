#gravar um arquivo
arquivo = open ("numero.txt", "w")

for linha in range (1,100):
    arquivo.write (f"{linha}\n")
arquivo.close()

#ler um arquivo
arquivo = open ("numero.txt", "r")
for linha in arquivo.readlines():
    print (linha)
arquivo.close()

#CRUD
#Criar
with open ("dados.txt", "w") as arquivo:
    arquivo.write ("Texto escrito como teste")

#Ler
with open ("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print (linha.stip())

#Alterar arquivo
#Lê arquivo
with open ("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

#Modifica 
with open ("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() == "Maria Clara":
            arquivo.write("Maria\n")
        else:
            arquivo.write(linha)

#Deletar
with open ("daddos.txt", "r") as arquivo:
    linhas = arquivo.readline()

#Escreve todos os dados diferentes de
with open ("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() != "Maria":
            arquivo.write(linha)
