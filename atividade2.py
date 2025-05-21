palavra = input("Digite uma palavra: ").lower()
vogais = 0
for letra in palavra:
    if letra in 'aeiouáéíóúãõâêîôû':
        vogais += 1
print(f"Total de vogais: {vogais}")