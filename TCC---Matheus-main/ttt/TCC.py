import PySimpleGUI as sg

import os
#caminhos das imagens tudo tem que ser .PNG
pasta=r'C:\Users\MatheusPereiraDaSilv\Desktop\ttt\logo.PNG'
pixe=r'C:\Users\MatheusPereiraDaSilv\Desktop\ttt\pix.PNG'
#formatação do numero de celular
padrao = r'^\+55\d{2}\d{9}$'
#pagina principal aonde fica a seleção de serviços
def principal():


    layout = [
        [sg.Image(filename=pasta,subsample=5)],  
        [sg.Text("Qual serviço você deseja contatar?",background_color='white',text_color='black'),
                sg.Combo(['Musculação','Aulas de Taekwondo','Aulas de Fit Dance', 'Pilates'],key='-COMBO-')],
                [sg.Button('Ok',button_color='black'), sg.Button('Cancelar',button_color='black')] 
                ]


    window = sg.Window('Academia GM FIT', layout,background_color='white')


    while True:
        event, values = window.read()
        ser=values['-COMBO-']
        if event=='Ok':
            #chmando a função de musculação
            if ser=='Musculação':
                window.close()
                musculação()
                
             #chamando a função de taekenwodo   
            if ser=='Aulas de Taekwondo':
                window.close()
                take()
            #chanmando a função de fitdance
            if ser=='Aulas de Fit Dance':
                window.close()
                dance()
            #chamando função de pilates
            if ser=='Pilates':
                window.close()
                pila()
        #fechando a janela 
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

    

    window.close()
#função local para mostrar as unidades da acadimia
def local():
    layout=[[sg.Image(filename=pasta,subsample=5)],
    [sg.Text('Secione Qual a Afilial Você Deseja Treinar!!!',background_color='white',text_color='Black'),sg.Combo(['GMFit-Praia Grande','GMFit-Barretos','GMFit-Poá','GMFit-Sorocaba'],key='al')],
    [sg.Button('Ok',button_color='black'),sg.Button('Cancelar',button_color='black')]]
    window = sg.Window('Planos de Musculação', layout,background_color='white')
    while True:
        event, values =window.read()
        #fechando a janela
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event=='Ok':
            af=values['al']
            #mostrando endeço da cada unidade
            if af=='GMFit-Praia Grande':
                sg.popup('Localização:Av. Marginal, 1150 - Canto Do Forte, Praia Grande - SP, 11700-970',background_color='white',text_color='Black',button_color='black')
                principal()
            if af=='GMFit-Poá':
                sg.popup('Localização:Av. Cap. Francisco Inácio, 144 - Centro, Poá - SP, 08551-150',background_color='white',text_color='Black',button_color='black')
                principal()
            if af=='GMFit-Barretos':

                sg.popup('Localização:Av. Vinte e Três, 1221 - América, Barretos - SP, 14780-320',background_color='white',text_color='Black',button_color='black')
                principal()
            if af=='GMFit-Sorocaba':
                sg.popup('Localização:R. Dr. Álvaro Soares, 46 - Centro, Sorocaba - SP, 18010-190',background_color='white',text_color='Black',button_color='black')
                principal()
            window.close()



#mostrando os planos de musculação 
def musculação():
    
    
    layout = [  
        [sg.Image(filename=pasta,subsample=5)],
        [sg.Text
         
         ('''PLANO MENSAL
VALOR: R$100,00
 O plano mensal de academia oferece flexibilidade e conveniência
 para quem busca atingir seus objetivos de saúde e bem-estar. 
Com acesso ilimitado a todos os equipamentos e áreas da academia, 
você pode treinar no seu ritmo e conforme sua disponibilidade.
                      ''',background_color='white',text_color='black')],

        [sg.Text('''PLANO TRIMESTRAL
VALOR:R$250,00
O plano trimestral é ideal para quem busca resultados consistentes em um período mais prolongado, 
com foco no acompanhamento contínuo e evolução visível. Com três meses de acesso ilimitado, 
você terá mais tempo para alcançar seus objetivos de maneira estruturada e eficiente.''',background_color='white',text_color='black')],

        [sg.Text('''PLANO ANUAL
VALOR:R$600,00
O plano anual é a melhor escolha para quem busca um compromisso de longo prazo
com a saúde e o bem-estar, proporcionando os melhores resultados ao longo do ano 
com uma rotina consistente e acompanhada. Com um ano de acesso ilimitado, este plano 
oferece o máximo de benefícios para que você atinja seus objetivos de forma sólida e duradoura.''',background_color='white',text_color='black'),
        sg.Combo(['Mensal','Trimestral','Anual'],key='plano')],

        [sg.Button('ok',button_color='black'),sg.Button('Cancelar',button_color='black')]]

        
       
                
                
   
    window = sg.Window('Planos de Musculação', layout,background_color='white')

    while True:
        event, values = window.read()


        # fechando
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event== 'ok':
            plano=values['plano']
            #mostando plano selecionado e chamando a função dindin
            if plano=='Mensal':
                dindin()
            if plano=='Trimestral':
                dindin()
            if plano=='Anual':
                dindin()

        if event==sg.WIN_CLOSED or event== 'Cancelar':
            principal()
            break



    window.close()


#função que cobra o cliente 
def dindin():
    layout=[
        [sg.Image(filename=pasta,subsample=5)],  
        [sg.Text("Forma de Pagamento",background_color='white',text_color='black'),
                sg.Combo(['Pix','Cartão de Credito','Cartão Debito'],key='pag')],
                [sg.Text("Digite a sua senha",background_color='white',text_color='black')],
                [sg.InputText()],
                [sg.Button('Ok',button_color='black'), sg.Button('Cancelar',button_color='black')] 
                ]
    window = sg.Window('Academia GM FIT', layout ,background_color='white',size=(600,600))
    while True:
        event,values=window.read()
        if event=='Ok':
            #chamando a função pix
            paga=values['pag']
            if paga=='Pix':
               Pix()
            if paga=='Cartão de Credito':
                Card()
            if paga=='Cartão Debito':
                Card()
                
        if event==sg.WIN_CLOSED=='Cancelar':
            principal()
            break
def Pix():
    layout=[
        [sg.Image(filename=pasta,subsample=5)],
    [sg.Push(background_color='white'),sg.Text('PIX',background_color='white',text_color='black'),sg.Push(background_color='white')],
    [sg.Push(background_color='white'),sg.Image(filename=pixe,subsample=2),sg.Push(background_color='white')],
     [sg.Push(background_color='white'),sg.Text(''' Copia e Cola
    00020126360014BR.GOV.BCB.PIX0114+55119478295455204000053039865406230.
 x   005802BR5901N6001C62090505gmfit63048577''',background_color='white',text_color='black'),sg.Push(background_color='white')],
    [sg.Button('Pago',button_color='black'),sg.Button('Cacelar',button_color='black')]]
    window = sg.Window('Academia GM FIT', layout ,background_color='white',size=(600,600))
    while True:
        event,values=window.read()
        if event=='Cacelar':
            window.close()
            principal()
            break

        if event=='Pago':
            sg.popup('Agrdecemos a Preferencia, Em breve eviaremos um E-mail de Confirmação de Pagamento ',background_color='white',text_color="black",button_color='black')
            break
def Card():
    
    layout = [
        [sg.Image(filename=pasta, subsample=5)],
        [sg.Text('Qual é a bandeira do seu cartão',background_color='white',text_color='black')],
        [sg.Combo(['Mastercard', 'Visa','American Express', 'Hipercard'], key='Bandeira',background_color='white',text_color='black')],
        [sg.Text('Digite o Número do Cartão',background_color='white',text_color='black')],
        [sg.Input(key='NC',background_color='white',text_color='black')],
        [sg.Button('Enviar'), sg.Button('Fechar')]
    ]
    
    
    window = sg.Window('Academia GM FIT', layout, background_color='black', size=(600, 300))
    
    while True:
        
        event, values = window.read()
        

        if event in (sg.WIN_CLOSED, 'Fechar'):
            principal()
            break
        
        
        if event == 'Enviar':
            bandeira = values['Bandeira']
            nc = values['NC']
            w=bool
            
            if bandeira=='Mastercard':
                if nc.startswith('5') or nc.startswith('2'):
                    [sg.popup('Bandeira esta certa!!!',background_color='white',text_color='black',button_color='black')]
                    w=True
                else:
                    [sg.popup('Bandeira esta errada!!!',background_color='white',text_color='black',button_color='black')] 
                    w=False  
            elif bandeira=='Visa':
                if nc.startswith('4'):
                    [sg.popup('Bandeira esta certa!!!',background_color='white',text_color='black',button_color='black')]
                    w=True
                else:
                    [sg.popup('Bandeira esta errada!!!',background_color='white',text_color='black',button_color='black')]
                    w=False  
            elif bandeira=='American Express':
                if nc.startswith('34') or nc.startswith('37'):
                    [sg.popup('Bandeira esta certa!!!',background_color='white',text_color='black',button_color='black')]
                    w=True
                else:
                    [sg.popup('Bandeira esta errada!!!',background_color='white',text_color='black',button_color='black')] 
                    w=False 
            elif bandeira=='Hipercard':
                if nc.startswith('38') or nc.startswith('60'):
                    [sg.popup('Bandeira esta certa!!!',background_color='white',text_color='black',button_color='black')]
                    w=True
                else:
                    [sg.popup('Bandeira esta errada!!!',background_color='white',text_color='black',button_color='black')]
                    w=False 
            else:
                [sg.popup('Bandeira esta errada!!!',background_color='white',text_color='black',button_color='black')]
            if w==True:
                nc=nc[::-1]
                total=0
                for i, digit in enumerate(nc):
                    n = int(digit)
                    if i % 2 == 1:
                        n *= 2
                        if n > 9:
                            n -= 9
                            ww=True
                    total += n
                    
                if ww==True:
                    [sg.popup('cartão valido',background_color='white',text_color='black',button_color='black')]
            
    window.close()
def take():
    layout=[[sg.Image(filename=pasta,subsample=5)],
            [sg.Text('''O Taekwondo é uma arte marcial
de origem coreana, conhecida por sua ênfase em
chutes altos e técnicas rápidas. Surgiu após a 
Segunda Guerra Mundial, combinando antigas práticas 
marciais coreanas com influências do karatê japonês. 
Além de ser um esporte olímpico, o Taekwondo 
promove a disciplina, o respeito e o autocontrole. 
Ele se divide em competições de luta, 
formas (poomsae) e defesa pessoal, sendo praticado 
tanto por crianças quanto por adultos''',background_color='white',text_color='black')],
[sg.Text('Escolha Seu Sensei, R$90,00 Ao Mês',background_color='white',text_color='black')],
[sg.Combo(['Vitoria Andrade','Murilo Horvat','Vitor Hugo','Vinicuis Olivera'],key='sen',background_color='white',text_color='black')],
[sg.Text('Escolha um Turno',background_color='white',text_color='black')],
[sg.Combo(['Manha','Tarde','Noite'],key='tur',background_color='white',text_color='black')],
[sg.Button('Eviar'),sg.Button('Cacelar')]]


    window = sg.Window('Academia GM FIT', layout,background_color='white')


    while True:
        event, values = window.read()
        if event=='Eviar':
            sensei= values['sen']
            turno= values['tur']
            [sg.popup(f'Sensei{sensei} Turno{turno},Aluno...')]
            dindin()

        if event=='Cacelar':
            window.close()
            break
def login():
    layout=[[sg.Image(filename=pasta,subsample=5)],
            [sg.Text('Nome de Usuario',background_color='white',text_color='black')],
    [sg.InputText(key='-us-',background_color='white',text_color='black')],
    [sg.Text('Digite sua Senha',background_color='white',text_color='black')],
    [sg.InputText(key='senha', password_char='*',background_color='white',text_color='black')],
    [sg.Button('Entrar',button_color='black'),sg.Button('Sair',button_color='black'),sg.Button('Cadastrar',button_color='black')]]
    window = sg.Window('Academia GM FIT', layout,background_color='white')
    while True:
        event, values = window.read()
        if event == 'Entrar':
                user = values['-us-']
                senha = values['senha']
                
                if user.isdigit():
                    sg.popup('O nome de usuário não pode ser numérico.',background_color='white')
                    continue
                
                if len(user) < 3:
                    if user == '':
                        sg.popup('As informações estão em branco.',background_color='white')
                    else:
                        sg.popup('O nome de usuário deve ter pelo menos 3 caracteres.',background_color='white')
                    continue
                
                user_found = False
                with open('dados_de_login.txt', 'r') as file:
                    for line in file:
                        file_user, file_senha = line.strip().split(',')
                        if file_user == user and file_senha == senha:
                            sg.popup('Login aceito!',background_color='white',text_color='black',button_color='black')
                            window.close
                            local()
                            user_found = True
                            break
                
                if not user_found:
                    sg.popup('Esse usuário não existe ou a senha está incorreta. Por favor, verifique novamente ou faça a inscrição.')
        if event=='Cadastrar':
            window.close()
            cad()
        if event in (sg.WIN_CLOSED, 'Sair'):
                window.close()
                return
                
def pila():
    layout=[[sg.Image(filename=pasta,subsample=5)],
            [sg.Text('''O Pilates é um método de exercício físico criado por Joseph Pilates no início do século XX. 
Ele foca no fortalecimento dos músculos profundos do corpo, responsável pela 
postura e estabilidade, principalmente o core (abdômen, pelve e região lombar). 
As aulas de Pilates podem ser realizadas individualmente ou com 
o uso de equipamentos específicos, combinando movimentos suaves e 
controlados com a respiração. Além de melhorar a flexibilidade, 
a força e o equilíbrio, o Pilates é amplamente utilizado na reabilitação física 
e no intervalo de dores musculares''',background_color='white',text_color='black')],
[sg.Text('Escolha Seu Instrutor, R$500,00 Ao Mês',background_color='white',text_color='black')],
[sg.Combo(['Artur Medeiros','Leonardo Lopez','Rebeca Takahashi','Heloisa Pereira'],key='ins',background_color='white',text_color='black')],
[sg.Text('Escolha um Turno',background_color='white',text_color='black')],
[sg.Combo(['Manha','Tarde','Noite'],key='tur',background_color='white',text_color='black')],
[sg.Button('Eviar',button_text='black'),sg.Button('Cacelar',button_text='black')]]


    window = sg.Window('Academia GM FIT', layout,background_color='white')


    while True:
        event, values = window.read()
        if event=='Eviar':
            instru= values['ins']
            turno= values['tur']
            [sg.popup(f'Instrutor{instru} Turno{turno}', background_color='white',text_color='black',button_color='black')]
            dindin()

        if event in (sg.WIN_CLOSED,'Cacelar'):
            principal()
            window.close()
            break
def dance():
    layout=[[sg.Image(filename=pasta,subsample=5)],
            [sg.Text('''O Fit Dance é uma modalidade de dança fitness que combina movimentos 
coreografados com ritmos populares, como funk, reggaeton, axé e pop. Criada no Brasil, 
ela busca aliar diversão e exercício físico, proporcionando uma forma dinâmica e envolvente 
de queima térmica. As aulas são estruturadas de forma simples para que pessoas de todos 
os níveis de habilidade possam acompanhar as coreografias, tornando-se uma maneira 
descontraída de melhorar o condicionamento físico, a progressão motora e liberar o estresse. 
O Fit Dance é popular em academias e eventos, sendo uma atividade social e energética''')],
[sg.Text('Escolha Seu instrutor, R$120,00 Ao Mês',background_color='white',text_color='black')],
[sg.Combo(['Alex Santos','Bruna Suarez','Julia Matos','Rafaela Grove'],key='da',background_color='white',text_color='black')],
[sg.Text('Escolha um Turno',background_color='white',text_color='black')],
[sg.Combo(['Manha','Tarde','Noite'],key='tur',background_color='white',text_color='black')],
[sg.Button('Eviar',button_color='black'),sg.Button('Cacelar',button_color='black')]]


    window = sg.Window('Academia GM FIT', layout,background_color='white')


    while True:
        event, values = window.read()
        if event=='Eviar':
            dan= values['da']
            turno= values['tur']
            [sg.popup(f'Sensei{dan} Turno{turno}',background_color='white',text_color='black')]
            dindin()

        if event in (sg.WIN_CLOSED,'Cacelar'):
            window.close()
            break
def cad():
    layout=[#[sg.Image(filename=pasta,subsample=5)],
        [sg.Text('Nome',background_color='white',text_color='black')],
            [sg.InputText(key='user',background_color='white',text_color='black')],
            [sg.Text('Digite um E-mail',background_color='white',text_color='black')],
            [sg.InputText(key='email',background_color='white',text_color='black')],
            [sg.Text('Digite o seu CPF',background_color='white',text_color='black')],
            [sg.InputText(key='cpf',background_color='white',text_color='black')],
            [sg.Text('Numero De Telefone',background_color='white',text_color='black')],
            [sg.InputText(key='ddd',background_color='white',text_color='black')],
            [sg.Text('Digite a senha ',background_color='white',text_color='black')],
            [sg.InputText(key='senha',background_color='white',text_color='black', password_char='*')],
            [sg.Button('Finalizar',button_color='black'),sg.Button('Voltar',button_color='black')]
            ]
    window = sg.Window('Academia GM FIT', layout,background_color='white')
    while True:
        event, values = window.read()
        if event =='Finalizar':
            nome=values['user']
            email=values['email']
            cpf=values['cpf']
            numero=values['ddd']
            senha=values['senha']
            if nome.isalpha()==False:
                [sg.popup('Escreva apenas letras')]
            if len(nome)<3:
                [sg.popup('Nome deve conter mais de 3 carcteres')]
            if '@'not in email:
                [sg.popup('Digite um Email valido')]
            cpf = cpf.replace(".", "").replace("-", "")
            if len(cpf) != 11:
                [sg.popup(f'O CPF precisa de 11 Numeros, Você Digitou apenas {len(cpf)} numeros')]
            if cpf == cpf[0] * 11:
                [sg.popup('Esse CPF tem mutos numeros repitidos')]
            soma = 0
            for i in range(9):
                soma += int(cpf[i]) * (10 - i)
            digito1 = 11 - (soma % 11)
            if digito1 > 9:
                digito1 = 0
            soma = 0
            for i in range(10):
                soma += int(cpf[i]) * (11 - i)
            digito2 = 11 - (soma % 11)
            if digito2 > 9:
                digito2 = 0
            if cpf[-2:] != f"{digito1}{digito2}":
              [sg.popup('digite um CPF valido')]  
            with open('dados_de_login.txt', 'a') as file:
                file.write(f"{nome},{senha}\n")
            login()
        if event in (sg.WIN_CLOSED,'Voltar'):
            window.close()
            login()
            break
login()