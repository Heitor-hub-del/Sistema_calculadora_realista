import time

def iniciar():
    print("iniciando.....")

    time.sleep(2)
    print("bem vindo a calculadora realista!")

    input1 = input("qual calculo voce deseja fazer?  1.soma 2.subtração 3.multiplicação 4.divisão 5.potencialização,6. fazer um loop,  7. porcentagem, 8. fatorial, 9. diferenciar numeros, 10. sair: ")

    print("processando...")

    time.sleep(2)

    if input1 == "1":
        print("soma escolhido")
        num1 = int(input("digite o primeiro numero:"))
        num2 = int(input("digite o segundo numero:"))

        resultado_da_soma = num1 + num2 

        print(f"o resultado e: {resultado_da_soma}")

    elif input1 == "2":
        print("subtração escolhido")
        num1 = int(input("digite o primeiro numero:"))
        num2 = int(input("digite o segundo numero:"))

        resultado_da_subtração = num1 - num2 

        print(f"o resultado e: {resultado_da_subtração}")

    elif input1 == "3":
        print("multiplicação escolhido")
        num1 = int(input("digite o primeiro numero:"))
        num2 = int(input("digite o segundo numero:"))
    

        resultado_da_multiplicação = num1 * num2

        print(f"o resultado e: {resultado_da_multiplicação}")

    elif input1 == "4":
        print("iniciando.....")
        num1 = int(input("digite o primeiro numero:"))
        num2 = int(input("digite o segundo numero:"))
    

        resultado_da_divisão = num1 / num2 

        print(f"o resultado e: {resultado_da_divisão}")

    elif input1 == "5":
        print("potencialização escolhido")
        num1 = int(input("digite o primeiro numero:"))
        num2 = int(input("digite o segundo numero"))
    
        resultado_da_potencialização = num1 ** num2 

        print(f"o resultado e: {resultado_da_potencialização}")

    elif input1 == "6":
        print("loop escolhido")
        input_loop = int(input("digite um numero para iniciar o loop:"))

        for i in range(input_loop + 1):
            print(i)

    elif input1 == "7":
        print("porcentagem escolhido")
        num = float(input("digite um numero:"))
        porcentagem = float(input("digite a porcentagem:"))

        resultado_da_porcentagem = (porcentagem / 100) * num
    
        print(f"o resultado e: {resultado_da_porcentagem}")

    elif input1 == "8":
        print("fatorial escolhido")

        import math

        num1 = int(input("digite o primeiro numero:"))
        num2 = int(input("digite o segundo numero:"))

        resultado_da_fatorial = math.factorial(num1) + math.factorial(num2)

        print(f"o resultado e: {resultado_da_fatorial}")

    elif input1 == "9":

        print("diferenciar numeros escolhido")
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


    elif input1 == "10":
        print("tem certeza que deseja sair?")
        saida = input("1.sim 2.não:")

        if saida == "1":
            print("saindo...")
            time.sleep(2)
        
        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

iniciar()