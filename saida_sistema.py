import voltar_menu_sistema
import time

def saida():
        
        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja sair?:")

        if certeza == "1":
            print("saindo.....")
            time.sleep(2)

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu_sistema.voltar_menu()