import customtkinter as ctk
from tkinter import messagebox


# 1. Configurações Iniciais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# 2. Instanciação da Janela
janela = ctk.CTk()
janela.title("Shibakita Eletro - Login")
janela.geometry("400x600")
janela.resizable(False, False)

# 3. Container (Frame) para centralizar os elementos
frame = ctk.CTkFrame(master=janela, corner_radius=15)
frame.pack(pady=40, padx=40, fill="both", expand=True)

# 4. Widgets

label_titulo = ctk.CTkLabel(master=frame, text="Shibakita Eletro", font=("Roboto", 24, "bold"))
label_titulo.pack(pady=20)

ent_usuario = ctk.CTkEntry(master=frame, placeholder_text="Usuário", height=45)
ent_usuario.pack(pady=12, padx=30, fill="x")

ent_senha = ctk.CTkEntry(master=frame, placeholder_text="Senha", show="*", height=45)
ent_senha.pack(pady=12, padx=30, fill="x")

btn_entrar = ctk.CTkButton(master=frame, text="Entrar", height=45)
btn_entrar.pack(pady=25, padx=30, fill="x")

# 5. Loop Principal
janela.mainloop()