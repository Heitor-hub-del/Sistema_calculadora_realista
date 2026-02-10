import math
import time
import voltar_menu_sistema
import consultar_valores_sistema_volta

def valores_sistema(input1):
    if input1 == "14":
        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar? :")

        if certeza == "1":
            print("1. ver valor de pi")
            print("2. ver valor de euler")

            valores_sistema_input = input("digite o numero do valor para consultar o valor:")

            if valores_sistema_input == "1":
                pi_valor = math.pi.__float__()

                print(f"o valor de pi e: {pi_valor}")

                print("1. ver mais valores")
                print("2. fazer contas com o valor do pi")
                print("3. sair do menu")

                pi_valor_sugestão = input("digite o que deseja fazer agora:")

                if pi_valor_sugestão == "1":
                    while True:
                        print("voltando ao menu de valores....")
                        time.sleep(2)
                        consultar_valores_sistema_volta.valores_sistema_voltar(input1)
                
                elif pi_valor_sugestão == "2":
                    print("1. soma")
                    print("2. subtração")
                    print("3. multiplicação")
                    print("4. divisão")
                    print("5. potencialização")

                    pi_valor_operadores = input("digite o numero da operação que deseja fazer:")

                    if pi_valor_operadores == "1":
                        pi1 = math.pi.__float__()
                        pi2 = math.pi.__float__()

                        pi_resultado_soma = pi1 + pi2

                        print(f"o resultado da soma de pi e: {pi_resultado_soma}")

                    elif pi_valor_operadores == "2":
                        pi1 = math.pi.__float__()
                        pi2 = math.pi.__float__()

                        pi_resultado_subtração = pi1 - pi2

                        print(f"o resultado da subração de pi e: {pi_resultado_subtração}")
                        
                    elif pi_valor_operadores == "3":
                        pi1 = math.pi.__float__()
                        pi2 = math.pi.__float__()

                        pi_resultado_multiplicação = pi1 * pi2

                        print(f"o resultado da multiplicação de pi e: {pi_resultado_multiplicação}")

                    elif pi_valor_operadores == "4":
                        pi1 = math.pi.__float__()
                        pi2 = math.pi.__float__()

                        pi_resultado_divisão = pi1 / pi2

                        print(f"o resultado da divisão de pi e: {pi_resultado_divisão}")

                    elif pi_valor_operadores == "5":
                        pi1 = math.pi.__float__()
                        pi2 = math.pi.__float__()

                        pi_resultado_potencialização = pi1 ** pi2

                        print(f"o resultado da potencialização de pi e: {pi_resultado_potencialização}")


            if valores_sistema_input == "2":
                euler_valor = math.e.__float__()

                print(f"o valor de euler e: {euler_valor}")
                
                print("1. ver mais valores")
                print("2. fazer contas com o valor do euler")
                print("3. sair do menu")

                euler_valor_sugestão = input("digite o que deseja fazer agora:")

                if euler_valor_sugestão == "1":
                    while True:
                        print("voltando ao menu de valores....")
                        time.sleep(2)
                        consultar_valores_sistema_volta.valores_sistema_voltar(input1)

                if euler_valor_sugestão == "2":
                    print("1. soma")
                    print("2.")

                    
                


