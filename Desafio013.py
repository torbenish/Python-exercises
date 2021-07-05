s = float(input("Qual o salário do Funcionário? R$"))

aumento = s * 0.15
novos = s + aumento

print(f'Um funcionário que ganhava R${s:.2f}, com 15% de aumento, passa a receber R${novos:.2f}')
