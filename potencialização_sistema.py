import time
import voltar_menu_sistema

def potencialização(input1):
    if input1 == "5":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("potencialização escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero"))
    
        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu_sistema.voltar_menu()

            resultado_da_potencialização = num1 ** num2 

            print(f"o resultado e: {resultado_da_potencialização}")

            print("1. sim")
            print("2. não")

            sujestão_potencialização  = input("gostaria de fazer mais potencialização?:")

            if sujestão_potencialização == "1":
                potencialização(input1)

            else:
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()
