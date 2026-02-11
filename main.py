import customtkinter as ctk
from tkinter import messagebox
from database import realizar_login
import os
from PIL import Image

def acao_login():
    usuario = ent_usuario.get()
    senha = ent_senha.get()
    
    perfil = realizar_login(usuario, senha)
    
    if perfil:
        messagebox.showinfo("Login", f"Bem-vindo! Perfil: {perfil}")
        #janela.destroy() 
        #abrir_menu(perfil)
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

# 1. Configurações Iniciais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Definir o caminho da imagem
caminho_logo = os.path.join(os.path.dirname(__file__), "logo_shibakita.png")

# Criar o objeto da imagem
imagem_logo = ctk.CTkImage(
    light_image=Image.open(caminho_logo),
    dark_image=Image.open(caminho_logo),
    size=(120, 120) # Ajuste o tamanho conforme necessário
)

# 2. Instanciação da Janela
janela = ctk.CTk()
janela.title("Shibakita Eletro - Login")
janela.geometry("400x600")
janela.resizable(False, False)

# 3. Container (Frame) para centralizar os elementos
frame = ctk.CTkFrame(master=janela, corner_radius=15)
frame.pack(pady=40, padx=40, fill="both", expand=True)


# 4. Widgets

# Inserir o logotipo no topo do frame
label_imagem = ctk.CTkLabel(master=frame, image=imagem_logo, text="") # text="" remove o texto padrão
label_imagem.pack(pady=(20, 10)) # Espaçamento superior e inferior

label_titulo = ctk.CTkLabel(master=frame, text="Shibakita Eletro", font=("Roboto", 24, "bold"))
label_titulo.pack(pady=20)

ent_usuario = ctk.CTkEntry(master=frame, placeholder_text="Usuário", height=45)
ent_usuario.pack(pady=12, padx=30, fill="x")

ent_senha = ctk.CTkEntry(master=frame, placeholder_text="Senha", show="*", height=45)
ent_senha.pack(pady=12, padx=30, fill="x")

btn_entrar = ctk.CTkButton(master=frame, text="Entrar", height=45, command=acao_login)
btn_entrar.pack(pady=25, padx=30, fill="x")


# 5. Loop Principal
janela.mainloop()