largura:float = float(input('Qual a largura do cômodo ?'))
profundidade:float = float(input('Qual a profundidade do cômodo ?'))
altura:float = 2.9 #Altura pé de piso

print ( 'A area das paredes é: ', 
       (2 * (largura + profundidade) * altura))
