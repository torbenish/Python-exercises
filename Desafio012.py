p = float(input('Qual o preço do produto? R$'))

desconto = p * 0.05
novop = p - desconto

print(f'O produto que custava R${p:.2f}, na promoção com desconto de 5% vai custar R${novop:.2f}')