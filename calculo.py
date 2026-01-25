print("bem vindo a calculadora realista!")

input1 = input("qual calculo voce deseja fazer?  1.soma 2.subtração 3.multiplicação 4.divisão 5.potencialização,6. fazer um loop,  7. porcentagem, 8. fatorial, 9. diferenciar numeros, 10. sair: ")

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

elif input1 == "5":
    num1 = int(input("digite o primeiro numero:"))
    num2 = int(input("digite o segundo numero"))
    
    resultado_da_potencialização = num1 ** num2 

    print(f"o resultado e: {resultado_da_potencialização}")

elif input1 == "6":
    input_loop = int(input("digite um numero para iniciar o loop:"))

    for i in range(input_loop + 1):
        print(i)

elif input1 == "7":
    num = float(input("digite um numero:"))
    porcentagem = float(input("digite a porcentagem:"))

    resultado_da_porcentagem = (porcentagem / 100) * num

    print(f"o resultado e: {resultado_da_porcentagem}")

elif input1 == "8":

    import math

    num1 = int(input("digite o primeiro numero:"))
    num2 = int(input("digite o segundo numero:"))

    resultado_da_fatorial = math.factorial(num1) + math.factorial(num2)

    print(f"o resultado e: {resultado_da_fatorial}")

elif input1 == "9":

    num1 = int(input("digite o primeiro numero:"))
    num2 = int(input("digite o segundo numero:"))

    numero_diferença = input("digite o < ou > ou = para saber qual numero sera comparado do maior ou do menor ou igual:")

    if numero_diferença == "<":
        if num1 < num2:
            print(f"o numero {num1 or num2} e menor que {num2 or num1}")
        else:
            print(f"os numeros são iguais")

    elif numero_diferença == ">":
        if num1 > num2:
            print(f"o numero {num1 or num2} e maior que {num2 or num1}")
        else:
            print(f"os numeros são iguais")

    elif numero_diferença == "=":
        if num1 == num2:
            print(f"os numeros são iguais")
        else:
            print(f"os numeros são diferentes e não sao iguais")

elif input1 == "9":
    print("saindo...")