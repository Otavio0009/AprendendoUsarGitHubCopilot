dado1 = int(input("Digite um número: "))
dado2 = int(input("Digite outro número: "))

escolhaOperacao = input("Qual o peracao você deseja realizar (+, -, /, *): ")

if escolhaOperacao == "+":
    soma = dado1 + dado2
    print(soma)

elif escolhaOperacao == "-":
    subitracao = dado1 - dado2

    #subitracao = abs(dado1 - dado2) não vai dar valor negativo!

    print(subitracao)

elif escolhaOperacao == "/":
    divisao = dado1 / dado2
    print(divisao)

elif escolhaOperacao == "*":
    mutiplicacao = dado1 * dado2
    print(mutiplicacao)

else:
    print("Operação não catalogada!")
