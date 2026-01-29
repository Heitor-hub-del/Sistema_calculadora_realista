import voltar_menu_sistema
import time


def formação_palavras(input1):
            print("1. sim")
            print("2. não")

            certeza = input("tem certeza que deseja continuar?:")

            if certeza == "1":
                palavra1 = input("digite a primeira palavra:")
                palavra2 = input("digite a segunda palavra:")

                palavra_combinar_resultado = palavra1 + palavra2

                print(palavra_combinar_resultado)
                
            else:
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()