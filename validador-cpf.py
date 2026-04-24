cpf = input("Digite seu CPF: ")

cpf = cpf.replace(".", "").replace("-", "")

if len(cpf) != 11:
    print("CPF inválido")

elif cpf == cpf[0] * 11:
    print("CPF inválido")

else:
    # PRIMEIRO DÍGITO
    soma = 0
    for contador in range(9):  
        soma = soma + int(cpf[contador]) * (10 - contador)

    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    
    if digito1 != int(cpf[9]):
        print("CPF inválido")
        exit()
    
    # SEGUNDO DÍGITO
    soma = 0
    for contador in range(10):
        soma = soma + int(cpf[contador]) * (11 - contador)

    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    
    if digito2 != int(cpf[10]):
        print("CPF inválido")
        exit()

    print("CPF válido")