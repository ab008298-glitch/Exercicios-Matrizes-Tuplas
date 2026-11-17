def verificar_identidade():
    matriz = []

    print("DIGITE OS VALORES DA MATRIZ 3x3")

    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input("Digite um valor: "))
            linha.append(valor)
        matriz.append(linha)

    identidade = True

    for i in range(3):
        for j in range(3):
            if i == j:
                if matriz[i][j] != 1:
                    identidade = False
            else:
                if matriz[i][j] != 0:
                    identidade = False

    print("MATRIZ INFORMADA:")

    for linha in matriz:
        print(linha)

    if identidade:
        print("A matriz é identidade!")
    else:
        print("A matriz não é identidade!")

    print("Explicação: a matriz identidade possui")
    print("1 na diagonal principal e 0 nas demais posições.")

verificar_identidade()