print("bem vindo a calculadora realista!")

input1 = input("qual calculo voce deseja fazer?  1.soma 2.subtração 3.multiplicação 4.divisão: ")

if input1 == "1":
    num1 = int(input("digite o primeiro numero:"))
    num2 = int(input("digite o segundo numero:"))

    resultado_da_soma = num1 + num2

    print(f"o resultado e: {resultado_da_soma}")

elif input1 == "2":
    num1 = int(input("digite o primeiro numero:"))
    num2 = int(input("digite o segundo numero:"))

    resultado_da_subtração = num1 - num2

    print(f"o resultado e: {resultado_da_subtração}")

elif input1 == "3":
    num1 = int(input("digite o primeiro numero:"))
    num2 = int(input("digite o segundo numero:"))

    resultado_da_multiplicação = num1 * num2

    print(f"o resultado e: {resultado_da_multiplicação}")

elif input1 == "4":
    num1 = int(input("digite o primeiro numero:"))
    num2 = int(input("digite o segundo numero:"))

    resultado_da_divisão = num1 / num2

    print(f"o resultado e: {resultado_da_divisão}")
    
    