from modelos.restaurante import Restaurante
from modelos.cadapio.bebida import Bebida
from modelos.cadapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
prato_paozinho = Prato('Pãozinho', 2.0, 'Pãozinho da Donatella')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()
