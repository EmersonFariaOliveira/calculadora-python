def ler_numero(mensagem):
    while True:
        try:
            valor = input(mensagem).replace(",", ".")
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite apenas números (ex: 10 ou 3.5).")



def menu():
    print("\n============================")
    print("      CALCULADORA SIMPLES   ")
    print("============================")
    print("1 - Soma           (+)")
    print("2 - Subtração      (-)")
    print("3 - Multiplicação  (*)")
    print("4 - Divisão        (/)")
    print("5 - Potência       (^)")
    print("6 - Resto divisão  (%)")
    print("0 - Sair")



def obter_operacao():
    while True:
        opcao = input("Escolha uma opção (0 a 6): ").strip()
        if opcao in {"0", "1", "2", "3", "4", "5", "6"}:
            return opcao
        print("Opção inválida. Digite um número entre 0 e 6.")



def calcular(opcao, a, b):
    if opcao == "1":
        return a + b
    elif opcao == "2":
        return a - b
    elif opcao == "3":
        return a * b
    elif opcao == "4":
        if b == 0:
            return "Erro: divisão por zero."
        return a / b
    elif opcao == "5":
        return a ** b
    elif opcao == "6":
        if b == 0:
            return "Erro: divisão por zero."
        return a % b
    else:
        return "Opção inválida."



def main():
    print("Bem-vindo(a) à calculadora!")
    while True:
        menu()
        opcao = obter_operacao()

        if opcao == "0":
            confirmar = input("Tem certeza que deseja sair? (s/n): ").strip().lower()
            if confirmar == "s":
                print("Encerrando a calculadora. Até mais!")
                break
            else:
                continue

        a = ler_numero("Digite o primeiro número: ")
        b = ler_numero("Digite o segundo número: ")

        resultado = calcular(opcao, a, b)
        print(f"\nResultado da operação: {resultado}\n")

        continuar = input("Deseja fazer outro cálculo? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando a calculadora. Até mais!")
            break


if __name__ == "__main__":
    main()
