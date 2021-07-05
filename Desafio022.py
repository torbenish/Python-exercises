nome = str(input('Digite seu nome: ')).strip()

separa = nome.split()

print(f'''Analisando seu nome...
Seu nome em maiúscula é {nome.upper()}
Seu nome em minúscula é {nome.lower()}
Seu nome tem ao todo {len(nome.replace(" ",""))}
Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras''')
