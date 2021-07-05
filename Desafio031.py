dist = int(input('Qual a distância da sua viagem? '))
#passagem1 = dist * 0.5
#passagem2 = dist * 0.45
#if dist <= 200:
    #print(f'Você está preste a começar uma viagem de {dist:.1f}Km')
    #print(f'E o preço da sua passagem será de R${passagem1:.2f}')
#else:
    #print(f'Você está prestes a começar uma viagem de {dist:.1f}km')
    #print(f'E o preço da sua passagem será de R${passagem2:.2f}')
print(f'Você está prestes a começar uma viagem de {dist:.1f}Km')
preço = dist * 0.5 if dist <= 200 else dist * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')