import time
import voltar_menu_sistema

def subtração(input1):

    if input1 == "2":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("subtração escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

            resultado_da_subtração = num1 - num2 

            print(f"o resultado e: {resultado_da_subtração}")

            print("1. sim")
            print("2. não")

            sujestão_subtração = input("gostaria de fazer mais subtrações?:")

            if sujestão_subtração == "1":
                subtração(input1)
            
            else:
            
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()