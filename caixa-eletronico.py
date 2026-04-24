print("Bem-vindo ao Caixa Eletrônico ")

agencia_correta = "1234"
senha_correta = "0000"
saldo = 1000

agencia = input("Digite sua agência: ")
senha = input("Digite sua senha: ")

if agencia == agencia_correta and senha == senha_correta:
    print("Login realizado com sucesso!")

    while True:
        print("\nMenu:")
        print("1 - Ver saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Seu saldo é: R${saldo}")

        elif opcao == "2":
            try:
                valor = float(input("Digite o valor do saque: "))
                if valor <= saldo:
                    saldo -= valor
                    print("Saque realizado!")
                else:
                    print("Saldo insuficiente!")
            except:
                print("Valor inválido!")

        elif opcao == "3":
            try:
                valor = float(input("Digite o valor do depósito: "))
                saldo += valor
                print("Depósito realizado!")
            except:
                print("Valor inválido!")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

else:
    print("Agência ou senha incorretas.")