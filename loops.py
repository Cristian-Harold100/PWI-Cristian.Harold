# Estrutura FOR / FOR EACH / WHILE

# EXEMPLO 1 - FOR (bônus)
lista_vendas = [1000, 500, 800, 600]
meta = 1200
percentual_bonus = 0.1

for venda in lista_vendas:
    if venda >= meta:
        bonus = percentual_bonus * venda
    else:
        bonus = 0

    print(f"Bonus: {bonus}")

# -------------------------------------

# EXEMPLO 2 - FOR + CONTINUE (pares)
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for numero in numeros:
    if numero % 2 != 0:
        continue
    print(f"O número par é {numero}")

# -------------------------------------

# EXEMPLO 3 - FOR + RANGE (soma)
soma = 0

for n in range(1, 11):
    soma += n

print(f"Soma é igual a {soma}")

# -------------------------------------

# EXEMPLO 4 - LISTA + FOR
frutas = ["maçã", "banana", "laranja", "melancia"]

for fruta in frutas:
    print(fruta)

for i in range(5):
    print(i)

# break (para no 5)
for i in range(10):
    if i == 5:
        break
    print(i)

# continue (pula o 2)
for i in range(5):
    if i == 2:
        continue
    print(i)

# -------------------------------------

# WHILE básico
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# WHILE com break
contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break

# WHILE até 10
contador = 0

while contador <= 10:
    print(f"O contador é {contador}")
    contador += 1

# WHILE com entrada do usuário
while True:
    numero = int(input("Digite um número par: "))

    if numero % 2 == 0:
        print("Você digitou um número par")
        break
    else:
        print("Você digitou um número ímpar")

print("Fim do programa")

# -------------------------------------

# DICIONÁRIO
dados = {
    "nome": "lan code",
    "inscritos": 5000,
    "categoria": "programação"
}

for chave in dados:
    print(chave)

for valor in dados.values():
    print(valor)

for chave, valor in dados.items():
    print(f"{chave}: {valor}")