print('-=-' * 14)
print('\033[1;31;107mAnalisador de Triângulos\033[m')
print('-=-' * 14)
a = float(input('\033[31mPrimeiro segmento: \033[m'))
b = float(input('\033[31mSegundo segmento: \033[m'))
c = float(input('\033[31mTerceiro segmento: \033[m'))

if a > b + c or b > a + c or c > a + b:
    print('\033[34mOs segmentos acima\033[m \033[1:34mNÃO PODEM FORMAR\033[m \033[33mtriângulo!\033[m')
elif a == b == c:
    print('\033[33mOs segmentos acima\033[m \033[1:33mPODEM FORMAR\033[m \033[33mtriângulo\033[m!')
    print('\033[4:33:44mTriângulo equilátero\033[m')
elif a == b or b == c or a == c:
    print('\033[35mOs segmentos acima\033[m \033[1:35mPODEM FORMAR\033[m \033[35mtriângulo!\033[m')
    print('\033[7:97mTriângulo isósceles\033[m')
else:
    print('\033[36mOs segmentos acima\033[m \033[1:36mPODEM FORMAR\033[m \033[36mtriângulo\033[m!')
    print('\033[97:42mTriângulo escaleno\033[m')