cid = str(input('Em que cidade você nasceu? ')).strip()
print(f'É verdade que Santo aparece no começo? {cid[:5].upper() == "SANTO"}')