import time
import voltar_menu_sistema

def loop(input1):
    if input1 == "6":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("loop escolhido")
            input_loop = int(input("digite um numero para iniciar o loop:"))

        for i in range(input_loop + 1):
            print(i)

        print("1. sim")
        print("2. não")

        sujestão_loop = input("gostaria de fazer mais loops ?:")

        if sujestão_loop == "1":
            loop(input1)

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu_sistema.voltar_menu()