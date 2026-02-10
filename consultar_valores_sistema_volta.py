import math
import time
import voltar_menu_sistema

def valores_sistema_voltar(input1):
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


            if valores_sistema_input == "2":
                euler_valor = math.e.__float__()

                print(f"o valor de euler e: {euler_valor}")
                
                print("1. ver mais valores")
                print("2. fazer contas com o valor do euler")
                print("3. sair do menu")

                euler_valor_sugestão = input("digite o que deseja fazer agora:")
