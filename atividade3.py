numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

numeros_dobro = [num * 2 for num in numeros]

print("\nLista original:", numeros)
print("Lista com dobro dos valores:", numeros_dobro)

soma = sum(numeros)
print("Soma dos números originais:", soma)

media = soma / len(numeros)
print("Média dos números originais:", media)