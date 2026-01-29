import voltar_menu_sistema
import time

def numeros_diferença(input1):

    if input1 == "9":
        
        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("diferenciar numeros escolhido")
            num1 = int(input("digite o primeiro numero:"))
            num2 = int(input("digite o segundo numero:"))

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu_sistema.voltar_menu()

        numero_diferença = input("digite o < ou > ou = para saber qual numero sera comparado do maior ou do menor ou igual:")

        if numero_diferença == "<":
            if num1 < num2:
                print(f"o numero {num1 or num2} e menor que {num1 or num2}")
            else:
                print(f"o numero {num2 or num1} e menor que {num1 or num2}")

                print("1. sim")
                print("2. não")

                numero_diferença_sujestão = input("gostaria de comparar mais numeros?:")

                if numero_diferença_sujestão == "1":
                    numeros_diferença(input1)

                else:
                    print("voltando ao menu....")
                    time.sleep(2)
                    voltar_menu_sistema()

        elif numero_diferença == ">":
            if num1 > num2:
                 print(f"o numero {num1 or num2} e maior que {num1 or num2}")
            else:
                print(f"o numero {num2 or num1} e maior que {num1 or num2}")

                print("1. sim")
                print("2. não")

                numero_diferença_sujestão = input("gostaria de comparar mais numeros?:")

                if numero_diferença_sujestão == "1":
                    numeros_diferença(input1)

                else:
                    print("voltando ao menu....")
                    time.sleep(2)
                    voltar_menu_sistema()

        elif numero_diferença == "=":
            if num1 == num2:
                 print("os numero são iguais")
            else:
                print("os numeros não são iguais")
        
                print("1. sim")
                print("2. não")

                numero_diferença_sujestão = input("gostaria de comparar mais numeros?:")

                if numero_diferença_sujestão == "1":
                    numeros_diferença(input1)

                else:
                    print("voltando ao menu....")
                    time.sleep(2)
                    voltar_menu_sistema.voltar_menu()
            

 