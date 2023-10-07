from CalcCombustivel import CalcCombustivel

print('''
    |------------------------------------------------------------------------------------|
    |Este programa tem como fim calcular o valor gasto de combustivel durante uma viagem,|
    |com base no consumo do seu veículo, e na distância determinada por você !           |
    |------------------------------------------------------------------------------------|
    
    Os combustíveis disponiveis para esse cálculo são:
     ○ Gasolina
     ○ Díesel
     ○ Álcool
''')

calc = CalcCombustivel(
    float(input('Quantos Quilômetros a ser percorrido?\nR.: ')),
    float(input('\nQual o consumo de combustível do veículo?\nR.: '))
)

calc.exibir_resultado()