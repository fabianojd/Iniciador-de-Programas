import tkinter as tk
import subprocess

def abrir_chrome():
    subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])

def abrir_vscode():
    subprocess.Popen(["C:\\Users\\seu_usuario\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])

def sair():
    janela.destroy()

janela = tk.Tk()
janela.title("Apps")
janela.configure(bg="#add8e6")

# Tamanho e posição
largura = 220
altura = 280
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = largura_tela - largura - 10
pos_y = altura_tela - altura - 80
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Estilo base dos botões
estilo_botao = {
    "bg": "white",
    "fg": "black",
    "font": ("Arial", 12, "bold"),
    "relief": "groove",
    "bd": 2,
    "width": 20,
    "height": 2
}

tk.Label(janela, text="Meus Apps", bg="#add8e6", fg="black", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(janela, text="Chrome", command=abrir_chrome, **estilo_botao).pack(pady=5)
tk.Button(janela, text="VS Code", command=abrir_vscode, **estilo_botao).pack(pady=5)
tk.Button(janela, text="Sair", command=sair, bg="#ff4d4d", fg="white", font=("Arial", 12, "bold"), width=20, height=2).pack(pady=20)

janela.mainloop()
