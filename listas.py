#Array
frutas = ["maçã", "banana", "laranja"]

print(frutas[0])  # maçã
print(frutas[1])  # banana
print(frutas[2])  # laranja

print(frutas)

#mudar o nome pela posição que o clente quer
frutas = ["maçã", "banana", "laranja"]
frutas[2] = "uva"
print[frutas]


#insert
frutas = ["maçã", "laranja"]
frutas.insert(1, "banana")
print[frutas]



#remover da lista
frutas = ["maçã", "banana", "laranja"]
frutas.remove("banana")
print(frutas)




temperatura_media = []
temperatura_media.append(31.9)
temperatura_media.append(21.8)
temperatura_media.append(27.7)
temperatura_media.append(30.5)
temperatura_media.append(23.6)

for i in temperatura_media:
    print (i)

nomes = []
nomes.append("samuel")
nomes.append("nicolas")
nomes.append("heberton")
nomes.append("denise")
for i in nomes:
    print(i)



usuarios = ["jose,carlos,giovanni,camila"]
for selecionados in usuarios: 
    print (selecionados)


adicionar = usuarios
adicionar.append("leticia")

print(usuarios)