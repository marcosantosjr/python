#calculadora básica

def calculadora():
    x = ''

    # Get operation input
    while x not in ["+", "-", "*", "/"]:
        x = input("Qual operação você deseja fazer? '+' '-' '*' '/'\n")

    # Get number inputs
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, digite números válidos!")
        return

    # Perform calculation
    if x == "+":
        resultado = a + b
        print(f"\nO resultado da soma é: {resultado}")
    elif x == "-":
        resultado = a - b
        print(f"\nO resultado da subtração é: {resultado}")
    elif x == "*":
        resultado = a * b
        print(f"\nO resultado da multiplicação é: {resultado}")
    elif x == "/":
        try:
            resultado = a / b
            print(f"\nO resultado da divisão é: {resultado}")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida!")


# Run the calculator
calculadora()
