numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))

print("Escolha a operação da calculadora: +, -, * ou /")
operacao = input("Digite a operação: ").strip()

match operacao:
        case "+":
             resultado = numero1 + numero2 
             print (f"Resultado da soma: {resultado}")
        case "-":
             resultado = numero1 - numero2 
             print (f"Resultado da subtracao: {resultado}")
        case "*":
             resultado = numero1 * numero2 
             print (f"Resultado da multiplicação: {resultado}")
        case "/":
          if numero2 != 0:
             resultado = numero1 / numero2 
             print (f"Resultado da divisão: {resultado}")
          else:
             print ("Não é possivel dividir por 0") 
        case _ :
             print ("digito invalido")