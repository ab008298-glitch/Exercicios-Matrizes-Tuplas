def calcular_determinante():

    print("Programa para calcular o determinante de uma matriz 2x2")
    print()

# Solicita os valores da matriz
a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))
c = int(input("Informe o terceiro valor: "))
d = int(input("Informe o quarto valor: "))

determinante = (a * d) - (b * c)

print()
print(f"O determinante é: {determinante}")

calcular_determinante()
 