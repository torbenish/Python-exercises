nome = str(input('Digite seu nome completo: ')).strip()

separa = nome.split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {separa[0]}')
print(f'Seu último nome é {separa[len(separa) - 1]}')