def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

def calculator():
    while True:
        print("Selecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo da calculadora.")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {add(num1, num2)}\n")

        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtract(num1, num2)}\n")

        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiply(num1, num2)}\n")

        elif escolha == '4':
            result = divide(num1, num2)
            print(f"Resultado: {num1} / {num2} = {result}\n")

        else:
            print("Escolha inválida!\n")

calculator()
