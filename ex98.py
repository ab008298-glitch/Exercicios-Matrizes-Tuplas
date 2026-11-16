def somar_matrizes():
    matriz1 = []
    matriz2 = []
    resultado = []

    print("DIGITE OS VALORES DA PRIMEIRA MATRIZ")

    for i in range(4):
        linha = []
        for j in range(3):
            valor = int(input("Digite um valor: "))
            linha.append(valor)
        matriz1.append(linha)

    print("DIGITE OS VALORES DA SEGUNDA MATRIZ")

    for i in range(4):
        linha = []
        for j in range(3):
            valor = int(input("Digite um valor: "))
            linha.append(valor)
        matriz2.append(linha)

    for i in range(4):
        linha = []
        for j in range(3):
            linha.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(linha)

    print("RESULTADO DA SOMA: ")

    for linha in resultado:
        print(linha)


somar_matrizes()