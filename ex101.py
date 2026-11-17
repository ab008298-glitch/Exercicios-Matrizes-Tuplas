def calcular_determinante():
    matriz = []

    print("DIGITE OS VALORES DA MATRIZ 3x3")

    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input("Digite um valor: "))
            linha.append(valor)
        matriz.append(linha)

    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[0][2]

    d = matriz[1][0]
    e = matriz[1][1]
    f = matriz[1][2]

    g = matriz[2][0]
    h = matriz[2][1]
    i = matriz[2][2]

    determinante = (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)

    print("\nMATRIZ INFORMADA:")

    for linha in matriz:
        print(linha)

    print("\nO determinante é:", determinante)

    print("\nExplicação: utilizamos a regra de Sarrus.")
    print("Somamos os produtos das diagonais principais")
    print("e subtraímos os produtos das diagonais secundárias.")

calcular_determinante()