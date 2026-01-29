import math
import time
import fatorial_sistema
import voltar_menu_sistema
import fatorial_menu_volta_sistema

def volta_menu():
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. potencialização")
        
    fatorial_operadores = input("digite o numero da operação para fazer com o fatorial:")


    if fatorial_operadores == "1":

            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

            num1_fatorial = math.factorial(num1)
            num2_fatorial = math.factorial(num2)

            fatorial_soma_resultado = num1_fatorial + num2_fatorial

            print(f"o resultado e: {fatorial_soma_resultado}")

            print("1. sim")
            print("2. não")

            sujestão_fatorial_operador = input("gostaria de voltar ao menu?:")

            if sujestão_fatorial_operador == "1":
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()
            
            else:
                print("voltando ao menu fatorial....")
                time.sleep(2)
                fatorial_menu_volta_sistema.volta_menu()

    elif fatorial_operadores == "2":
         
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

            num1_fatorial = math.factorial(num1)
            num2_fatorial = math.factorial(num2)

            fatorial_subtração_resultado = num1_fatorial - num2_fatorial

            print(f"o resultado e: {fatorial_subtração_resultado}")

            print("1. sim")
            print("2. não")

            sujestão_fatorial_operador = input("gostaria de voltar ao menu?:")

            if sujestão_fatorial_operador == "1":
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()
            
            else:
                print("voltando ao menu fatorial....")
                time.sleep(2)
                fatorial_menu_volta_sistema.volta_menu()

    elif fatorial_operadores == "3":
            
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

            num1_fatorial = math.factorial(num1)
            num2_fatorial = math.factorial(num2)

            fatorial_multiplicação_resultado = num1_fatorial * num2_fatorial

            print(f"o resultado e: {fatorial_multiplicação_resultado}")

            print("1. sim")
            print("2. não")

            sujestão_fatorial_operador = input("gostaria de voltar ao menu?:")

            if sujestão_fatorial_operador == "1":
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()
            
            else:
                print("voltando ao menu fatorial....")
                time.sleep(2)
                fatorial_menu_volta_sistema.volta_menu()

    elif fatorial_operadores == "4":
            
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))
            
            num1_fatorial = math.factorial(num1)
            num2_fatorial = math.factorial(num2)

            fatorial_divisão_resultado = num1_fatorial / num2_fatorial

            print(f"o resultado e: {fatorial_divisão_resultado}")

            print("1. sim")
            print("2. não")

            sujestão_fatorial_operador = input("gostaria de voltar ao menu?:")

            if sujestão_fatorial_operador == "1":
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()
            
            else:
                print("voltando ao menu fatorial....")
                time.sleep(2)
                fatorial_menu_volta_sistema.volta_menu()
    

    elif fatorial_operadores == "5":
            
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

            num1_fatorial = math.factorial(num1)
            num2_fatorial = math.factorial(num2)

            fatorial_potencialização_resultado = num1_fatorial ** num2_fatorial

            print(f"o resultado e: {fatorial_potencialização_resultado}")

            print("1. sim")
            print("2. não")

            sujestão_fatorial_operador = input("gostaria de voltar ao menu?:")

            if sujestão_fatorial_operador == "1":
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()
            
            else:
                print("voltando ao menu fatorial....")
                time.sleep(2)
                fatorial_menu_volta_sistema.volta_menu()
