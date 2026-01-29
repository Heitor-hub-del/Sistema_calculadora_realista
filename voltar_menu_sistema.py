
import time
import math

def voltar_menu():
    
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. potencialização")
    print("6. fazer um loop")
    print("7. porcentagem")
    print("8. fatorial")
    print("9. diferenciar numeros")
    print("10. converter tempo")
    print("11. fazer calculos com letras ou palavras")
    print("12. formação de palavras")
    print("13. usar os conceitos matematicos")
    print("14. sair")

    input1 = input("digite o numero do calculo que deseja fazer:")

    print("processando...")

    time.sleep(2)

    if input1 == "1":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("soma escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu()
            

        resultado_da_soma = num1 + num2 

        print(f"o resultado e: {resultado_da_soma}")

    elif input1 == "2":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("subtração escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu()

        resultado_da_subtração = num1 - num2 

        print(f"o resultado e: {resultado_da_subtração}")

    elif input1 == "3":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        
        if certeza == "1":
            print("multiplicação escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu()
        resultado_da_multiplicação = num1 * num2

        print(f"o resultado e: {resultado_da_multiplicação}")

    elif input1 == "4":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("iniciando.....")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu()

        resultado_da_divisão = num1 / num2 

        print(f"o resultado e: {resultado_da_divisão}")

    elif input1 == "5":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("potencialização escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero"))
    
        else:
            print("voltando ao menu....")
            voltar_menu()

        resultado_da_potencialização = num1 ** num2 

        print(f"o resultado e: {resultado_da_potencialização}")

    elif input1 == "6":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("loop escolhido")
            input_loop = int(input("digite um numero para iniciar o loop:"))

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu()

        for i in range(input_loop + 1):
            print(i)

    elif input1 == "7":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("porcentagem escolhido")
            num = float(input("digite um numero:"))
            porcentagem = float(input("digite a porcentagem:"))

            resultado_da_porcentagem = (porcentagem / 100) * num
    
            print(f"o resultado e: {resultado_da_porcentagem}")

        elif certeza == "2":
            print("voltando ao menu....")
            voltar_menu()
            

    elif certeza == "8":
        pass
        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")
        
        if certeza == "1":
            print("fatorial escolhido")

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu()

        num1 = int(input("digite o primeiro numero:"))

        resultado_da_fatorial = math.factorial(num1)

        print(f"o resultado e: {resultado_da_fatorial}")

        


    elif input1 == "9":
    

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("diferenciar numeros escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("voltando ao menu....")
            voltar_menu()

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

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("conversor de tempo escolhido")

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu()

            print("1. segundos para minutos")
            print("2. minutos para horas")
            print("3. horas pára dias")
            print("4. dias para semanas")
            print("5. semanas para meses")
            print("6. meses para anos")

            usuario = input("qual voce deseja converter?:")

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

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("calculos com palavras escolhido")

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu()

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

            print("1. sim")
            print("2. não")

            certeza = input("tem certeza que deseja continuar?:")

            if certeza == "1":
                palavra1 = input("digite a primeira palavra:")
                palavra2 = input("digite a segunda palavra:")

                palavra_combinar_resultado = palavra1 + palavra2

                print(palavra_combinar_resultado)
                
            else:
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu()

    elif input1 == "13":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("uso de conceitos selecionado")

        elif certeza == "2":
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu()

            print("1. cos")
            print("2. sin")
            print("3. tan")
            print("4. atan")
            print("5. acosh")
            print("6. asinh")
            print("7. asin")
            print("8. cosh")
            print("9. atan2")
            print("10. atanh")
            print("11. sinh")
            print("12. log")
            print("13. log2")
            print("14. log10")
            print("15. log1p")

            conceito_input = input("qual conceito voce quer fazer?:")

            if conceito_input == "1":
                num1 = int(input("digite um numero:"))

                cos_resultado = math.cos(num1)

                print(f"o resultado e: {cos_resultado}")

            elif conceito_input == "2":
                num1 = int(input("digite um numero:"))

                sin_resultado = math.sin(num1)

                print(f"o resultado e: {sin_resultado}")

            elif conceito_input == "3":
                num1 = int(input("digite um numero:"))

                tan_resultado = math.tan(num1)

                print(f"o resultado e: {tan_resultado}")

            elif conceito_input == "4":
                num1 = int(input("digite um numero:"))

                atan_resultado = math.atan(num1)

                print(f"o resultado e: {atan_resultado}")

            elif conceito_input == "5":
                num1 = int(input("digite um numero:"))

                acosh_resultado = math.acosh(num1)

                print(f"o resultado e: {acosh_resultado}")
                
            elif conceito_input == "6":
                num1 = int(input("digite um numero:"))

                asinh_resultado = math.asinh(num1)

                print(f"o resultado e: {asinh_resultado}")
                
            elif conceito_input == "7":
                num1 = int(input("digite um numero:"))

                asin_resultado = math.asin(num1)

                print(f"o resultado e: {asinh_resultado}")

            elif conceito_input == "8":
                num1 = int(input("digite um numero:"))

                cosh_resultado = math.cosh(num1)

                print(f"o resultado e: {cosh_resultado}")

            elif conceito_input == "9":
                num1 = int(input("digite um numero:"))

                atan2_resultado = math.atan2(num1)

                print(f"o resultado e: {atan2_resultado}")

            elif conceito_input == "10":
                num1 = int(input("digite um numero:"))

                atanh_resultado = math.atanh(num1)

                print(f"o resultado e: {atanh_resultado}")

            elif conceito_input == "11":
                num1 = int(input("digite um numero:"))

                sinh_resultado = math.sinh(num1)

                print(f"o resultado e: {sinh_resultado}")

            elif conceito_input == "12":
                num1 = int(input("digite um numero:"))

                log_resultado = math.log(num1)

                print(f"o resultado e: {log_resultado}")

            elif conceito_input == "13":
                num1 = int(input("digite um numero:"))

                log2_resultado = math.log2(num1)

                print(f"o resultado e: {log2_resultado}")

            elif conceito_input == "14":
                num1 = int(input("digite um numero:"))

                log10_resultado = math.log10(num1)

                print(f"o resultado e: {log10_resultado}")

            elif conceito_input == "15":
                num1 = int(input("digite um numero:"))

                log1p_resultado = math.log1p(num1)

                print(f"o resultado e: {log1p_resultado}")


    elif input1 == "14":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("saindo")

        else:
            voltar_menu()
            

             



