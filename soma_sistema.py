import time
import voltar_menu_sistema

def soma(input1):

    if input1 == "1":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("soma escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))
            
            resultado_da_soma = num1 + num2 

            print(f"o resultado e: {resultado_da_soma}")

            print("1. sim")
            print("2. não")

            sujestão_soma = input("voce gostaria de fazer mais somas?:")

            if sujestão_soma == "1":
                soma(input1)

            else:
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()