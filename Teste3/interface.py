from tkinter import *
from tkinter import messagebox

tela = Tk()
tela.title("Cadastro de Produtos")
# tela.geometry("1024x600")
tela.state("zoomed")  # janela maximizada
tela.resizable(False, False)
tela.iconbitmap("imagens/thefreeforty_register_icon-icons.com_66338.ico")

def inserir():
    messagebox.showinfo("Inserir", "Produto inserido com sucesso!")

def buscar():
    messagebox.showinfo("Buscar", "Busca realizada!")

def atualizar():
    messagebox.showinfo("Atualizar", "Produto atualizado!")

def excluir():
    messagebox.showinfo("Excluir", "Produto excluído!")

def novo():
    entry_codigo.delete(0, END)
    entry_descricao.delete(0, END)
    entry_fabricante.delete(0, END)
    entry_preco.delete(0, END)
    entry_quantidade.delete(0, END)

Label(tela, text="Código:").place(x=20, y=20)
Label(tela, text="Descrição:").place(x=20, y=60)
Label(tela, text="Fabricante:").place(x=20, y=100)
Label(tela, text="Preço:").place(x=20, y=140)
Label(tela, text="Quantidade:").place(x=20, y=180)

entry_codigo = Entry(tela, width=30)
entry_codigo.place(x=120, y=20)

entry_descricao = Entry(tela, width=30)
entry_descricao.place(x=120, y=60)

entry_fabricante = Entry(tela, width=30)
entry_fabricante.place(x=120, y=100)

entry_preco = Entry(tela, width=30)
entry_preco.place(x=120, y=140)

entry_quantidade = Entry(tela, width=30)
entry_quantidade.place(x=120, y=180)

Button(tela, text="Inserir", width=10, command=inserir).place(x=20, y=240)
Button(tela, text="Buscar", width=10, command=buscar).place(x=110, y=240)
Button(tela, text="Atualizar", width=10, command=atualizar).place(x=200, y=240)
Button(tela, text="Excluir", width=10, command=excluir).place(x=290, y=240)
Button(tela, text="Novo", width=10, command=novo).place(x=150, y=290)

tela.mainloop()
