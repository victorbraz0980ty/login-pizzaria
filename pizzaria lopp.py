import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.title("login dos usuários")
root.geometry("500x300")

def abrir_login():
    root.withdraw() 

    janela_de_inicio = customtkinter.CTkToplevel(root)    

    janela_de_inicio.geometry("500x300")  

    janela_de_inicio.title("Cadastro")    

    janela_de_inicio.attributes("-topmost", True)     
        
    texto_cadastro = customtkinter.CTkLabel(janela_de_inicio, text="Tela de inicío")
    texto_cadastro.pack(pady=20)   
    
'''Janela de cadastro e Posições'''  
def abrir_cadastro():   
    root.withdraw()    
        
    janela_de_cadastro = customtkinter.CTkToplevel(root)    

    janela_de_cadastro.geometry("500x300")  

    janela_de_cadastro.title("Cadastro")    

    janela_de_cadastro.attributes("-topmost", True)     
        
    texto_cadastro = customtkinter.CTkLabel(janela_de_cadastro, text="Página de Cadastro")
    texto_cadastro.pack(pady=20)


texto = customtkinter.CTkLabel(root, text= "Seja bem - vindo a pizza loop, faça o seu login:", font=("Arial",14,"bold"))
texto.pack(padx=10, pady=10)

numero = customtkinter.CTkEntry(root, placeholder_text="Digite seu nome:")
numero.pack(padx=10, pady=10)
'''Senha e posiçao'''
senha = customtkinter.CTkEntry(root, placeholder_text="Digite sua senha:", show="*")
senha.pack(padx=10, pady=10)
'''Lembrar login e posicao'''
checkbox = customtkinter.CTkCheckBox(root, text="Lembrar login")
checkbox.place(relx=0.15, rely=0.65)    
'''Cadastro e posicao'''    
cadrasto = customtkinter.CTkButton(root, text="Criar conta",command=abrir_cadastro,fg_color="transparent",text_color="white",bg_color="darkblue")
cadrasto.place(relx=0.6, rely=0.65)
'''Botão de Login e Posição'''
botao_de_login= customtkinter.CTkButton(root, text="Login", command=abrir_login)
botao_de_login.pack(padx=10,pady=10)

root.mainloop()
