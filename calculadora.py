numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))

print ("Escolha a operação: ")
print ("1 - Soma")
print ("2 - Subtração")
print ("3 - Multiplicação")
print ("4 - Divisão")

operacao = input("digite o número da operação desejada: ").strip()
if operacao == "1": 
   resultado = numero1 + numero2 
   print (f"Resultado da soma: {resultado}")
elif operacao == "2":
   resultado = numero1 - numero2
   print (f"Resultado da subtração é: {resultado} ")
elif operacao == "3":
   resultado = numero1 * numero2
   print (f"Resultado da Multiplicação: {resultado}")
elif operacao == "4":
   if numero2 != 0:
      resultado = numero1 / numero2
      print (f"Resultado da divisão é: {resultado}")
   else:
      print (f"Não é possivel dividir por 0")
else:
   print ("Digito inválido")




