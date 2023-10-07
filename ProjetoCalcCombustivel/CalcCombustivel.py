class CalcCombustivel:

    def __init__(self, __km_p, __consumo):
        self.__custo_gasolina = (5.70 / __consumo) * __km_p
        self.__custo_diesel = (5.20 / __consumo) * __km_p
        self.__custo_alcool = (3.20 / __consumo) * __km_p

    @property
    def custo_gasolina(self):
        return self.__custo_gasolina
    
    @property
    def custo_diesel(self):
        return self.__custo_diesel
    
    @property
    def custo_alcool(self):
        return self.__custo_alcool

    def exibir_resultado(self):
        print(f'\nCusto com gasolina: R${self.__custo_gasolina:.2f}')
        print(f'Custo com diesel: R${self.__custo_diesel:.2f}')
        print(f'Custo com alcool: R${self.__custo_alcool:.2f}\n')