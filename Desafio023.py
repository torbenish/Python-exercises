num = int(input('Informe um número: '))

#n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#print(f'''Analisando o número {num}
#Unidade: {n[3]}
#Dezena: {n[2]}
#Centena: {n[1]}
#Milhar: {n[0]}''')

print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
