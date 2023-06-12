def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def main():
    print("Bem-vindo à calculadora!")
    print("-------------------------")

    while True:
        print("Selecione uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = somar(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = subtrair(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcao == "3":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcao == "4":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = dividir(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcao == "5":
            print("Saindo da calculadora...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
