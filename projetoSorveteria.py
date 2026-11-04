import tkinter as tk
from tkinter import messagebox, ttk

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Sorveteria - Sistema de Pedidos")
janela.geometry("440x520")
janela.config(bg="#E3F2FD") # Azul claro de fundo



itens_comprados = []

frame_pagina1 = tk.Frame(janela, bg="#E3F2FD")
frame_pagina2 = tk.Frame(janela, bg="#E3F2FD")

def aviso():

    tamanho = combo_tamanho.get()
    sabor = combo_sabor.get()
    cobertura = combo_cobertura.get()
    adicionais = combo_adicionais.get()

    if not tamanho or not sabor:
        messagebox.showinfo("Aviso", "Você precisa selecionar pelo menos o tamanho e o sabor do sorvete.")
        return
    else:
        messagebox.showinfo("sucesso", "Sorvete adicionado ao pedido com sucesso!")

    descricao = f" {tamanho} - Sabor: {sabor} - Cobertura: {cobertura} - Adicionais: {adicionais}"
    itens_comprados.append(descricao)


    combo_tamanho.set('')
    combo_sabor.set('')
    combo_cobertura.set('')
    combo_adicionais.set('')


def atualizar_resumo():

    if itens_comprados:
        texto = "\n".join(itens_comprados)
    else:
        texto = "Seu carrinho está vazio..."


    lbl_itens_resumo.config(text=texto)

def mudar_pagina(pagina):
    frame_pagina1.pack_forget()
    frame_pagina2.pack_forget()
    pagina.pack(fill="both", expand=True, padx=20, pady=20)

    if pagina == frame_pagina2:
        atualizar_resumo()

def limpar_carrinho():
    itens_comprados.clear()
    atualizar_resumo()
    

tk.Label(frame_pagina1, text=" 🍦 Monte o seu Sorvete", font=("Arial", 16, "bold"), bg="#E3F2FD", fg="#D81B60").pack(pady=20)


frame_pagina1 = tk.Frame(janela, bg="#E3F2FD")
frame_pagina1.pack(fill="both", expand=True, padx=20, pady=20)
frame_pagina2 = tk.Frame(janela, bg="#E3F2FD")

# Card Branco para os menus
card_branco = tk.Frame(frame_pagina1, bg="#FFFFFF", padx=20, pady=20)
card_branco.pack(fill="both", expand=True, pady=5)

tk.Label(card_branco, text="Escolha o Tamanho:", font=("Arial", 12, "bold"), bg="#FFFFFF").pack(anchor="w", pady=5)
combo_tamanho = ttk.Combobox(card_branco, values=["Copinho", "Cascão", "Cascinha", "Pote 1kg"], state="readonly", font=("Arial", 8))
combo_tamanho.pack(fill="x", pady=(5, 20))

tk.Label(card_branco, text="Escolha o Sabor:", font=("Arial", 12, "bold"), bg="#FFFFFF").pack(anchor="w", pady=5)
combo_sabor = ttk.Combobox(card_branco, values=["Chocolate", "Morango", "Creme", "Flocos"], state="readonly", font=("Arial", 8))
combo_sabor.pack(fill="x", pady=(5, 20))

tk.Label(card_branco, text="Escolha a cobertura:", font=("Arial", 12, "bold"), bg="#FFFFFF").pack(anchor="w", pady=5)
combo_cobertura = ttk.Combobox(card_branco, values=["Nenhuma", "Chocolate", "Morango", "Creme"], state="readonly", font=("Arial", 8))
combo_cobertura.pack(fill="x", pady=(5, 20))


tk.Label(card_branco, text="Escolha os adicionais:", font=("Arial", 12, "bold"), bg="#FFFFFF").pack(anchor="w", pady=5)
combo_adicionais = ttk.Combobox(card_branco, values=["Nenhum", "paçoca", "morango", "banana", "Uva", "mel", "leite em pó", "granola", "leite condensado"], state="readonly", font=("Arial", 8))
combo_adicionais.pack(fill="x", pady=(5, 20))

tk.Button(card_branco, text="Adicionar ao Pedido", font=("Arial", 12, "bold"), bg="#D81B60", fg="white", command=lambda: aviso()).pack(pady=10)

tk.Button(card_branco, text="Ver Meu Pedido ➔", font=("Arial", 12, "bold"), bg="blue", fg="white", command=lambda: mudar_pagina(frame_pagina2)).pack(pady=10)


##PAGINA 2 - RESUMO DO PEDIDO


tk.Label(frame_pagina2, text="📋 Resumo do Pedido", font=("Arial", 16, "bold"), bg="#E3F2FD", fg="#D81B60").pack(pady=20)

card_resumo = tk.Frame(frame_pagina2, bg="#FFFFFF", padx=20, pady=20)
card_resumo.pack(fill="both", expand=True, pady=5)

lbl_itens_resumo = tk.Label(card_resumo, text="", font=("Arial", 11), bg="#FFFFFF", fg="#333333", justify="left", anchor="nw", height=10)
lbl_itens_resumo.pack(fill="both", expand=True, pady=5)

frame_botoes = tk.Frame(frame_pagina2, bg="#FFFFFF")
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="voltar", font=("Arial", 12, "bold"), bg="#D81B60", fg="white", command=lambda: mudar_pagina(frame_pagina1)).pack(side="left", padx=5)
tk.Button(frame_botoes, text="Finalizar Pedido", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=lambda: messagebox.showinfo("Sucesso", "Pedido finalizado com sucesso!")).pack(side="left", padx=5)
tk.Button(frame_botoes, text="Limpar Carrinho", font=("Arial", 12, "bold"), bg="#D81B60", fg="white", command=lambda: [itens_comprados.clear(), atualizar_resumo()]).pack(side="left", padx=5)


janela.mainloop()