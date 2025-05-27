
userCpf =''
userNome=''
userSenha=''
userSaldo = 0.0
extrato = [] 

while True:
    print('--- Bem-vindo à Agência XPTO --- ')
    print('\n')

    print("1 - Criar conta")
    print ("2 - Fazer login")
    print ("3 - Sair")
    print("\n")

    escolha = int(input("> Escolha: "))
    print('\n')

    if escolha == 1:
        if userNome =='' and userCpf =='' and userSenha =='':
            userNome = str(input('Digite seu nome: '))
            userCpf = str(input('Digite seu CPF: '))
            userSenha = str(input('Crie uma senha: '))
            print('Conta criada com sucesso!')
            print('\n')
        else:
            print("Voce ja tem uma conta")
            print("\n")

    elif escolha == 2:
        
        if userNome =='' and userCpf =='' and userSenha =='':
            print("Voce não possui uma conta, porfavor crie uma conta")
            print('\n')
        else:
            print('------------- FAÇA SEU LOGIN-----------------')
            cpf = str(input("CPF : "))
            senha = str(input("Senha : "))
            print("\n")
            if cpf == userCpf and senha == userSenha:
                print("Login bem-sucedido!")
                print("\n")



                
                

                while True:
                    print("-------------- MENU --------------------")
                    print('1 - Ver saldo')
                    print('2 - Depositar')
                    print('3 - Sacar')
                    print('4 - Transferir')
                    print('5 - Ver extrato')
                    print('6 - Sair')

                    escolhaMenu = int(input("> Escolha : "))
                    print("\n")

                    if escolhaMenu == 1:
                        print('Seu saldo: R$ ', userSaldo)

                    elif escolhaMenu == 2:
                        valorDeposito = float(input('Digite valor para depósito: '))
                        print("\n")
                        if valorDeposito > 0 :
                            userSaldo = userSaldo + valorDeposito
                            extrato.append(f'depoito de R$ {valorDeposito:.2f}')
                        else:
                            print("esse valor e invalido tente novamente")
                            print('\n')

                    elif escolhaMenu == 3:
                        valorSacar = float(input('Digite valor para o saque :'))
                        if valorSacar > 0: 
                            if userSaldo > valorSacar:
                                userSaldo = userSaldo - valorSacar
                                extrato.append(f'Seque realizado no valor de {valorSacar:.2f}')
                            else:
                                print("Você não possui essa quantia para sacar ")
                                print("\n")
                        else:
                            print("esse valor e invalido")
                            print("\n")
                    elif escolhaMenu == 4:
                        print("transferir")
                        recebedor = int(input('Qual o CPF do recebedor?'))
                        valorTransferencia = float(input('digite o valor que deseja tranferir:'))
                        if valorTransferencia > userSaldo: 
                            print('transferencia não realizada por falta de saldo.')
                        else:
                            userSaldo = userSaldo - valorTransferencia
                            print('transferencia realizada com  sucesso!.')
                            extrato.append(f'transferencia realizada no valor de {valorTransferencia:.2f}')



                    elif escolhaMenu == 5:
                        if extrato:
                            print('últimas ações feitas:')
                            for acao in extrato[-1]:
                                print(acao)
                        else:
                         print('Nenhuma ação  foi  executada.')        

                    elif escolhaMenu == 6:
                        print(" Você saiu do Menu ")
                        break
                    else:
                        print(" essa opção não existe tente novamanete")
                        print("\n")






    
                
            else:
                print("senha ou cpf incorretos")
                print("\n")
            
        
    elif escolha == 3: 
        print("Você saiu. até aproxima")
        break
    else:
        print(" Essa opção não existe tente novamente")
        print("\n")



