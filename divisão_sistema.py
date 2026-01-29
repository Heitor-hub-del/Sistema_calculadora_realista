import time
import voltar_menu_sistema

def divisão(input1):
    if input1 == "4":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("iniciando.....")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

            resultado_da_divisão = num1 / num2 

            print(f"o resultado e: {resultado_da_divisão}")

            print("1. sim")
            print("2. não")

            sujestão = input("gostaria de fazer mais divisão?:")

            if sujestão == "1":
                divisão(input1)

            else:
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()