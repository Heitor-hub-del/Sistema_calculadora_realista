import time
import voltar_menu_sistema


def multiplicação(input1):

    if input1 == "3":

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
            voltar_menu_sistema.voltar_menu()

            resultado_da_multiplicação = num1 * num2

            print(f"o resultado e: {resultado_da_multiplicação}")

            sujestão_soma = input("voce gostaria de fazer mais somas?:")

            if sujestão_soma == "1":
                multiplicação(input1)

            else:
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()
