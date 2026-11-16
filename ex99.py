def cadastrar_pessoas():
    pessoas = []

    for i in range(10):
        print("Cadastro da pessoa", i + 1)

        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        pessoa = (nome, idade)
        pessoas.append(pessoa)

    print("PESSOAS COM MENOS DE 18 ANOS:")

    for pessoa in pessoas:
        if pessoa[1] < 18:
            print("Nome:", pessoa[0], "Idade:", pessoa[1])

    print("PESSOAS COM 18 ANOS OU MAIS:")

    for pessoa in pessoas:
        if pessoa[1] >= 18:
            print("Nome:", pessoa[0], "Idade:", pessoa[1])


cadastrar_pessoas()