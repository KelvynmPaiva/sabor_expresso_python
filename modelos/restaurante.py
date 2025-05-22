class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Burguer King', 'Hamburgueria')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

print(restaurante_praca)
print(restaurante_pizza)

