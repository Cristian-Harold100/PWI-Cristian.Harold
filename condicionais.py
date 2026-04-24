# Estrutura condicional If,Elif e Else
#if - se a condição for verdadeira.
idade = 18
if idade >= 18:
    print("Você é maior de idade")

#-------------------------------------
#elif - outras condições se o if for falso.
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")

#-------------------------------------
# else - quando nenhuma das condições anteriores é verdadeira.
nota = 5 
if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")

#-------------------------------------
# verificar idade 
idade = 12
if idade <= 12:
    print("Criança ")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso") 
