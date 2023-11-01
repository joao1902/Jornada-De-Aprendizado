import tkinter as tk #importando biblioteca para interfaces gráficas, o as cria um apelido
# no caso a biblioteka tkinter é apelidada de tk
janela_boas_vindas = tk.Tk()
janela_boas_vindas.configure(bg="#add8e6")
janela_boas_vindas.title("CAshAPP")
janela_boas_vindas.geometry("250x300")

canvas = tk.Canvas(janela_boas_vindas, width=250, height=300, bg="#000080")
canvas.pack()
rotulo_boas_vindas = tk.Label(janela_boas_vindas, text ="Bem Vindo ao CashApp", font=("Helvetica",   16))   
rotulo_boas_vindas.pack(pady=20)

janela_boas_vindas.mainloop()



'''def solucionar_funcao():
    if funcao == "Vendedor": 
        janela_boas_vindas.destroy() #fecha a tela boas vindas
        abrir_tela_loguin_vendedor()
    elif funcao == "Adiministrador":
        janela_boas_vindas.destroy()
        abrir_tela_loguin_adiministrador()


def abrir_tela_loguin_vendedor(): #função para abrir a tela vendedor
    pass #deixando em branco temporariamente

def abrir_tela_loguin_adiministrador(): #funcao para abrir a tela administrador
    pass #deixando em branco temporariamente


#criar tela de boas vindas
janela_boas_vindas = tk.Tk()
janela_boas_vindas.title("CAshAPP")

#rotulo de boas vindas

#text seria o texto que o programador quer inserir
#font seria a font desejada "Helvetica e 16 o tamanho da letra"
rotulo_boas_vindas = tk.Label(janela_boas_vindas, text ="Bem Vindo ao CashApp",font=("Helvetica",   16))   
rotulo_boas_vindas.pack(pady=20) #o pady basicamente define o espaço vertical que vc quer

#botões para a seleção da função
#tk.label cria um ojeto de rotulo usando a classe lambda do modulo para, assim lambda retorna a funççao que recebeu
botao_vendedor = tk.Button(janela_boas_vindas, text= "Entrar como Vendedor", command= lambda:solucionar_funcao("Vendedor"))
botao_administrador = tk.Button(janela_boas_vindas, text= "Entrar como Administrador", command = lambda:solucionar_funcao("Admistrador"))
botao_vendedor.pack() # o .pack faz com que o botão vendedor já criado anteriormente 
botao_administrador.pack() # receba a posição do gerenciador de layout "pack"

#Inicia a interface gráfica e a tela de  boas vindas
janela_boas_vindas.mainloop()

#                         =-=-=-=-=-=-=-=-=-=-=-
#                        Tela de loguin de ambos
# função para tratar o loguin administrador 
def loguin_administrador():
    if email == "admin@gmail.com" and senha == "senha_admin":
        abrir_tela_acompanhamento_admin()
    else:#label é onde guardamos um rotulo da interface grafica
       #.config é onde vc pode alterar as configuraçoes do rótulo
       #text moatr o que vai aparecer caso de erro
       label_erro.config(text= "Loguin falhou . Verifique suas credenciais.")

# função para abrir a tela acompanhamento de vendas para o administrador
# a função.destry faz com que a ultima janela se encerre
def abri_tela_acompanhamento_admin():
    janela_loguin_admin.destroy()
    
#criando a janela loguin administrador
janela_loguin_admin = tk.Tk()
janela_loguin_admin.title("Cash APP - Loguin Administrador")

#Rotulo do titulo
rotulo_titulo = tk.Label(janela_loguin_admin, text = "Loguin Administrador", font = ("Helvetica", 16))
rotulo_titulo.pack(pady =20 )

#Campo de entarda para o email do administrador 
# show="*" para ocultar a senha e width=30 para defini a largura do campo de entrada dos caracteres
# tk.Entry serve como um imput para deixar que o usuário digite suas informações
entrada_email = tk.Entry(janela_loguin_admin, width=30) 
entrada_email.pack()

#Campo de entrada para a senha do administrador
entrada_senha = tk.Entry(janela_loguin_admin, show="*",width=30 )
entrada_senha.pack()

#botão de loguin
#.get() obtem o valor inserido pelo usuário
botao_loguin = tk.Button(janela_loguin_admin, text= "Loguin (ex:botãoazul)", command = lambda:loguin_administrador(entrada_email.get(), entrada_senha.get()))
botao_loguin.pack()

#Rotulo para exibir mensagens de erro
label_erro = tk.Label(janela_loguin_admin, text="", fg= "red")
label_erro.pack()

#inicia a interface grafica da tela de loguin do administrador
janela_loguin_admin.mainloop()
#                      =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#                      Tela acompanhamento admin

def abrir_tela_acompanhamento_admin():
    janela_loguin_admin.destroy()

janela_acompanhamento_admin = tk.Tk()
janela_acompanhamento_admin.title("Acompanhamento Vendas  - Administrador")
# Adicionar aqui um grafico de exemplo para o almento de vendas 
janela_acompanhamento_admin.mainloop

#                      =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#                              Tela de loguin vendedor
    
def abrir_tela_loguin_vendedor():
    #Fecha a tela de boas vindas
    janela_boas_vindas.destroy()
def abrir_tela_acompanhamento_vendedor():
    pass

    #Criando a tela de loguin vendedor
janela_loguin_vendedor = tk.Tk()
janela_loguin_vendedor.title("CashAPP - Loguin vendedor")

    #Rotulo de boas vindas
    #tk.Label(Label é usar para criar rotulos ou melhor, passar uma informação)
rotulo_loguin_vendedor = tk.Label(janela_loguin_vendedor, text= "Faça seu loguin",font= ("Helvetica", 16))
rotulo_loguin_vendedor.pack(pady= 20)

    #Capo de entrada para o email do vandedor
    # width controla a largura do campo e show = "*" oculta uma informação que o usuário colocar 
entrada_email_vendedor = tk.Entry(janela_loguin_vendedor, width= 30)
entrada_email_vendedor.pack()

    #Campo de entrada para a senha do vendedor
entrada_senha_vendedor = tk.Entry(janela_loguin_vendedor, show= "*", width= 30)
entrada_senha_vendedor.pack()

    #Botão para fazer loguin como vendedor
botao_loguin_vendedor = tk.Button(janela_loguin_vendedor, text= "Loguin", command= loguin_vendedor(entrada_email.get(), entrada_senha.get()))
botao_loguin_vendedor.pack()

    #Botão para cadastro vendedor
botao_cadastro_vendedor = tk.Button(janela_loguin_vendedor,text= "Cadastro (exbotão azul)" )
botao_cadastro_vendedor.pack()
janela_loguin_vendedor.mainloop'''






