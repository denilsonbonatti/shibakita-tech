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

# 5. Loop Principal
janela.mainloop()