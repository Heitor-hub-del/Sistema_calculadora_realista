import time
import math


def iniciar():
    print("iniciando.....")

    time.sleep(2)
    print("bem vindo a calculadora realista!   v1.3")

    input1 = input("qual calculo voce deseja fazer?  1.soma 2.subtração 3.multiplicação" \
    " 4.divisão 5.potencialização,6. fazer um loop,  7. porcentagem, 8. fatorial, 9. diferenciar numeros, 10.converter tempo, 11: fazer calculos com letras ou palavras, 12. sair : ")

    print("processando...")

    time.sleep(2)

    if input1 == "1":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")
        if certeza == "1":
            print("soma escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

        resultado_da_soma = num1 + num2 

        print(f"o resultado e: {resultado_da_soma}")

    elif input1 == "2":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")

        if certeza == "1":
            print("subtração escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

        resultado_da_subtração = num1 - num2 

        print(f"o resultado e: {resultado_da_subtração}")

    elif input1 == "3":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")
        if certeza == "1":
            print("multiplicação escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

        resultado_da_multiplicação = num1 * num2

        print(f"o resultado e: {resultado_da_multiplicação}")

    elif input1 == "4":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")

        if certeza == "1":
            print("iniciando.....")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

        resultado_da_divisão = num1 / num2 

        print(f"o resultado e: {resultado_da_divisão}")

    elif input1 == "5":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")

        if certeza == "1":
            print("potencialização escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero"))
    
        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

        resultado_da_potencialização = num1 ** num2 

        print(f"o resultado e: {resultado_da_potencialização}")

    elif input1 == "6":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")

        if certeza == "1":
            print("loop escolhido")
            input_loop = int(input("digite um numero para iniciar o loop:"))

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

        for i in range(input_loop + 1):
            print(i)

    elif input1 == "7":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")

        if certeza == "1":
            print("porcentagem escolhido")
            num = float(input("digite um numero:"))
            porcentagem = float(input("digite a porcentagem:"))

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

        resultado_da_porcentagem = (porcentagem / 100) * num
    
        print(f"o resultado e: {resultado_da_porcentagem}")

    elif input1 == "8":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")
        
        if certeza == "1":
            print("fatorial escolhido")

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

        num1 = int(input("digite o primeiro numero:"))
        num2 = int(input("digite o segundo numero:"))

        resultado_da_fatorial = math.factorial(num1) + math.factorial(num2)

        print(f"o resultado e: {resultado_da_fatorial}")

    elif input1 == "9":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")

        if certeza == "1":
            print("diferenciar numeros escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

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
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")

        if certeza == "1":
            print("conversor de tempo escolhido")

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

            usuario = input("qual voce deseja converter? 1. segundos para minutos 2. minutos para horas 3. horas para dias 4. dias para semana 5. semanas para meses 6. meses para anos :")

            if usuario == "1":
                segundos = int(input("digite os segundos que deseja converter:"))

                minutos = segundos / 60

                print(f"a conversão de {segundos} segundos para minutos é: {minutos} minutos")

            elif usuario == "2":
                minutos = int(input("digite os minutos que deseja converter:"))

                horas = minutos / 60

                print(f"a conversão de {minutos} minutos para horas é: {horas} horas")

            elif usuario == "3":
                horas = int(input("digite as horas que deseja converter:"))

                dias = horas / 24

                print(f"a conversão de {horas} horas para dias é: {dias} dias")

            elif usuario == "4":
                dias = int(input("digite os dias que deseja converter:"))

                semanas = dias / 7

                print(f"a conversão de {dias} dias para semanas é: {semanas} semanas")

            elif usuario == "5":
                semanas = int(input("digite as semanas que deseja converter:"))

                meses = semanas / 4.34524

                print(f"a conversão de {semanas} semanas para meses é: {meses} meses")
            
            elif usuario == "6":
                meses = int(input("digite os meses que deseja converter:"))

                anos = meses / 12

                print(f"a conversão de {meses} meses para anos é: {anos} anos")

            
    if input1 == "11":
        certeza = input("tem certeza que deseja continuar? 1.sim 2.não:")

        if certeza == "1":
            print("calculos com palavras escolhido")

        else:
            print("reniciando.....")
            time.sleep(2)
            iniciar()

        palavra_sinal = input("qual operação voce deseja fazer com as palavras? 1.soma 2.subtração 3.multiplicação 4.divisão 5. potencialização  :")


        palavra1 = input("digite a primeira palavra:")

        palavra1_valor = input("digite o valor numerico da primeira palavra:")

        palavra2 = input("digite a segunda palavra:")

        palavra2_valor = input("digite o valor numerico da segunda palavra:")

            
        if palavra_sinal == "1":
                resultado_palavra_soma = int(palavra1_valor) + int(palavra2_valor)

                print(f"o resultado da soma entre {palavra1} e {palavra2} é: {resultado_palavra_soma}")

        elif palavra_sinal == "2":
                resultado_palavra_subtração = int(palavra1_valor) - int(palavra2_valor)

                print(f"o resultado da subtração entre {palavra1} e {palavra2} é: {resultado_palavra_subtração}")

        elif palavra_sinal == "3":
                resultado_palavra_multiplicação = int(palavra1_valor) * int(palavra2_valor)

                print(f"o resultado da multiplicação entre {palavra1} e {palavra2} é: {resultado_palavra_multiplicação}")
            
        elif palavra_sinal == "4":
                resultado_palavra_divisão = int(palavra1_valor) / int(palavra2_valor)

                print(f"o resultado da divisão entre {palavra1} e {palavra2} é: {resultado_palavra_divisão}")
            
        elif palavra_sinal == "5":
                resultado_palavra_potencialização = int(palavra1_valor) ** int(palavra2_valor)

                print(f"o resultado da potencialização entre {palavra1} e {palavra2} é: {resultado_palavra_potencialização}")

            
    elif input1 == "12":
            certeza = input("tem certeza que deseja sair? 1.sim 2.não:")

            if certeza == "1":
                print("saindo.....")
                time.sleep(2)

            else:
                print("reniciando.....")
                time.sleep(2)
                iniciar()

iniciar()


