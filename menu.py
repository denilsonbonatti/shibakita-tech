import customtkinter as ctk
from tkinter import messagebox
import os
from PIL import Image

def abrir_menu(perfil):
    """Função que constrói e exibe a janela do Menu Principal."""
    
    # 1. Configurações da Janela
    menu_app = ctk.CTk()
    menu_app.title(f"Shibakita Tech - Sistema de Gestão [{perfil}]")
    menu_app.geometry("1000x600")
    menu_app.resizable(True, True)

    # 2. Carregamento de Ícone/Logo para o Menu
    caminho_logo = os.path.join(os.path.dirname(__file__), "logo_shibakita.png")
    img_logo = ctk.CTkImage(Image.open(caminho_logo), size=(60, 60))

    # --- FUNÇÕES DE NAVEGAÇÃO ---
    def abrir_clientes():
        messagebox.showinfo("Navegação", "Abrindo módulo de Clientes...")

    def abrir_produtos():
        messagebox.showinfo("Navegação", "Abrindo módulo de Produtos...")

    def abrir_vendas():
        messagebox.showinfo("Navegação", "Abrindo módulo de Vendas...")

    def fazer_logout():
        if messagebox.askyesno("Sair", "Deseja realmente encerrar a sessão?"):
            menu_app.destroy()
            # Aqui poderíamos chamar o login novamente se desejado

    # --- LAYOUT: BARRA LATERAL (SIDEBAR) ---
    sidebar = ctk.CTkFrame(menu_app, width=200, corner_radius=0)
    sidebar.pack(side="left", fill="y")

    # Logo e Título na Sidebar
    lbl_logo_menu = ctk.CTkLabel(sidebar, image=img_logo, text="")
    lbl_logo_menu.pack(pady=(20, 10))
    
    lbl_titulo_side = ctk.CTkLabel(sidebar, text="Shibakita\nTech", font=("Roboto", 18, "bold"))
    lbl_titulo_side.pack(pady=10)

    # Botões da Sidebar
    btn_clientes = ctk.CTkButton(sidebar, text="Clientes", command=abrir_clientes, fg_color="transparent", hover_color="#334155")
    btn_clientes.pack(pady=5, padx=20, fill="x")

    btn_produtos = ctk.CTkButton(sidebar, text="Produtos", command=abrir_produtos, fg_color="transparent", hover_color="#334155")
    btn_produtos.pack(pady=5, padx=20, fill="x")

    btn_vendas = ctk.CTkButton(sidebar, text="Vendas", command=abrir_vendas, fg_color="transparent", hover_color="#334155")
    btn_vendas.pack(pady=5, padx=20, fill="x")

    # Botão Sair (embaixo)
    btn_sair = ctk.CTkButton(sidebar, text="Sair do Sistema", command=fazer_logout, fg_color="#ef4444", hover_color="#b91c1c")
    btn_sair.pack(side="bottom", pady=20, padx=20, fill="x")

    # --- LAYOUT: ÁREA CENTRAL ---
    conteudo = ctk.CTkFrame(menu_app, corner_radius=15)
    conteudo.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    lbl_boas_vindas = ctk.CTkLabel(conteudo, text=f"Bem-vindo(a), {perfil}!", font=("Roboto", 28, "bold"))
    lbl_boas_vindas.pack(pady=(50, 10))

    lbl_info = ctk.CTkLabel(conteudo, text="Selecione uma opção no menu lateral para começar.", font=("Roboto", 14))
    lbl_info.pack(pady=10)

    # Dashboard Simples (Cards informativos)
    cards_frame = ctk.CTkFrame(conteudo, fg_color="transparent")
    cards_frame.pack(pady=30, padx=20, fill="x")

    # Exemplo de um "Card" de resumo
    card1 = ctk.CTkFrame(cards_frame, width=200, height=100, corner_radius=10)
    card1.pack(side="left", padx=10, expand=True)
    ctk.CTkLabel(card1, text="Vendas Hoje", font=("Roboto", 12)).pack(pady=10)
    ctk.CTkLabel(card1, text="R$ 1.250,00", font=("Roboto", 18, "bold")).pack(pady=5)

    menu_app.mainloop()