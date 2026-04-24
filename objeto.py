vendedor = "lyra"
vendas = 600
meta = 500 
if vendas >= meta:
    print("meta batida")
else:
   print("não bateu a meta")

class Vendedor():  # classe (molde / modelo)
    
   def __init__(self, nome):  # método construtor (cria o objeto)
      self.nome = nome       # atributo (característica do objeto)
      self.vendas = 0        # atributo (cada objeto começa com 0 vendas)

   def vendeu(self, vendas):  # método (ação do objeto)
      self.vendas = vendas   # altera o valor de vendas daquele objeto

   def bateu_meta(self, meta):  # método (ação do objeto)
      if self.vendas > meta:
        print(self.nome, "bateu a meta")
      else:
         print(self.nome, "não bateu a meta")


# AQUI COMEÇAM O objetos (INSTÂNCIAS)

Vendedor1 = Vendedor("lyra")  
# objeto criado a partir da classe Vendedor
# esse objeto tem seus próprios dados (nome = lyra, vendas = 0)

Vendedor1.vendeu(1000)  
# o objeto Vendedor1 está usando o método vendeu()

Vendedor1.bateu_meta(600)  
# o objeto Vendedor1 verifica se bateu a meta


Vendedor2 = Vendedor("Cristian")  
# outro objeto (independente do primeiro)

Vendedor2.vendeu(400)  
# esse objeto tem um valor diferente de vendas

Vendedor2.bateu_meta(600)  
# resultado diferente porque os dados são diferentes

#-------------------------------------------------
class Carro:
    def __init__(self, marca, modelo):
        # inicializa os atributos do objeto
        self.marca = marca
        self.modelo = modelo

    def buzinar(self):
        print("Bii bii!")

carro1 = Carro("Toyota", "Corolla")

print(carro1.marca)   # Toyota
print(carro1.modelo)  # Corolla

carro1.buzinar()



