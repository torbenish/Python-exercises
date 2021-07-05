salario = float(input('Qual o salário do funcionário? '))

novo = salario + (salario * 0.10) if salario > 1250 else salario + (salario * 0.15)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.')