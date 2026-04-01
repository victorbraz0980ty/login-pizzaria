'''import tkinter 
root = tkinter.Tk()
root.title("Seja bem - vindo a pizza loop")
root.geometry("500x300")

def clique():
    print("Fazer login")
texto= tkinter.Label(root, text="Fazer login")
texto.grid(padx=10, pady=10)

botao= tkinter.Button(root, text= "Seja bem - vindo a pizza loop", command=clique)
botao.grid(padx=10, pady=10)

root.mainloop()'''

import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.title("login dos usuários")
root.geometry("500x300")
def clique():

    print("Seja bem - vindo a pizza loop, faça o seu login")
texto = customtkinter.CTkLabel(root, text= "Seja bem - vindo a pizza loop, faça o seu login:", font=("Arial",14,"bold"))
texto.pack(padx=10, pady=10)

numero = customtkinter.CTkEntry(root, placeholder_text="Digite seu nome:")
numero.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(root, placeholder_text="Digite sua senha:", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(root, text="Lembrar login")
checkbox.pack(padx=10, pady=10)

botao= customtkinter.CTkButton(root, text="Login", command=clique)
botao.pack(padx=10,pady=10)

root.mainloop()

