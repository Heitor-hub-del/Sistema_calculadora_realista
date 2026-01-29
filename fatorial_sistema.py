import math
import time
import voltar_menu_sistema
import fatorial_menu_volta_sistema

def fatorial(input1):
    if input1 == "8":
        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")
        
        if certeza == "1":
            print("fatorial escolhido")

            num1 = int(input("digite o primeiro numero:"))

            resultado_da_fatorial = math.factorial(num1)

            print(f"o resultado e: {resultado_da_fatorial}")

            print("1. sim")
            print("2. não")
            print("3. fazer fatorial com operadores")

            sujestão_fatorial = input("gostaria de fazer mais um fatorial ou fazer fatorial com operadores?:")

            if sujestão_fatorial == "1":
                fatorial(input1)

            elif sujestão_fatorial == "2":

                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()

            else:
                fatorial_menu_volta_sistema.volta_menu()
                
        

    
    
