import time
import voltar_menu_sistema

def porcentagem(input1):
    if input1 == "7":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("porcentagem escolhido")
            num = float(input("digite um numero:"))
            porcentagem = float(input("digite a porcentagem:"))

            resultado_da_porcentagem = (porcentagem / 100) * num
    
            print(f"o resultado e: {resultado_da_porcentagem}")

            print("1. sim")
            print("2. não")

            sujestão_porcentagem = input("gostaria de fazer mais porcentagem?:")

            if sujestão_porcentagem == "1":
                porcentagem(input1)

            else:
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()