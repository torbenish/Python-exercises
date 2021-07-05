dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
custo_carro = dias * 60
custo_km = km * 0.15
soma = custo_carro + custo_km


print(f'O total a pagar é de R${custo_carro + custo_km:.2f}')