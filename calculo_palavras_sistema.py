import time
import voltar_menu_sistema

def calculo_palavras(input1):

    if input1 == "11":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("calculos com palavras escolhido")

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu_sistema.voltar_menu()

        print("1. soma")
        print("2. subtração")
        print("3.multiplicação")
        print("4. divisão")
        print("5. potencialização")

        palavra_sinal = input("qual operação voce deseja fazer com as palavras? :")

        palavra1 = input("digite a primeira palavra:")

        palavra1_valor = input("digite o valor numerico da primeira palavra:")

        palavra2 = input("digite a segunda palavra:")

        palavra2_valor = input("digite o valor numerico da segunda palavra:")

            
        if palavra_sinal == "1":
                resultado_palavra_soma = int(palavra1_valor) + int(palavra2_valor)

                print(f"o resultado da soma entre {palavra1} e {palavra2} é: {resultado_palavra_soma}")

                print("1. sim")
                print("2. não")

                calculo_palavras_sujestão = input("gostaria de fazer mais calculos com palavras?:")


                if calculo_palavras_sujestão == "1":
                      calculo_palavras(input1)

                else:
                    print("voltando ao menu....")
                    time.sleep(2)
                    voltar_menu_sistema.voltar_menu()
            

        elif palavra_sinal == "2":
                resultado_palavra_subtração = int(palavra1_valor) - int(palavra2_valor)

                print(f"o resultado da subtração entre {palavra1} e {palavra2} é: {resultado_palavra_subtração}")

                print("1. sim")
                print("2. não")

                calculo_palavras_sujestão = input("gostaria de fazer mais calculos com palavras?:")

                if calculo_palavras_sujestão == "1":
                      calculo_palavras(input1)

                else:
                    print("voltando ao menu....")
                    time.sleep(2)
                    voltar_menu_sistema.voltar_menu()

        elif palavra_sinal == "3":
                resultado_palavra_multiplicação = int(palavra1_valor) * int(palavra2_valor)

                print(f"o resultado da multiplicação entre {palavra1} e {palavra2} é: {resultado_palavra_multiplicação}")

                print("1. sim")
                print("2. não")

                calculo_palavras_sujestão = input("gostaria de fazer mais calculos com palavras?:")

                if calculo_palavras_sujestão == "1":
                      calculo_palavras(input1)

                else:
                    print("voltando ao menu....")
                    time.sleep(2)
                    voltar_menu_sistema.voltar_menu()
            
        elif palavra_sinal == "4":
                resultado_palavra_divisão = int(palavra1_valor) / int(palavra2_valor)

                print(f"o resultado da divisão entre {palavra1} e {palavra2} é: {resultado_palavra_divisão}")

                print("1. sim")
                print("2. não")

                calculo_palavras_sujestão = input("gostaria de fazer mais calculos com palavras?:")

                if calculo_palavras_sujestão == "1":
                      calculo_palavras(input1)

                else:
                    print("voltando ao menu....")
                    time.sleep(2)
                    voltar_menu_sistema.voltar_menu()
            
        elif palavra_sinal == "5":
                resultado_palavra_potencialização = int(palavra1_valor) ** int(palavra2_valor)

                print(f"o resultado da potencialização entre {palavra1} e {palavra2} é: {resultado_palavra_potencialização}")

                print("1. sim")
                print("2. não")

                calculo_palavras_sujestão = input("gostaria de fazer mais calculos com palavras?:")

                if calculo_palavras_sujestão == "1":
                      calculo_palavras(input1)

                else:
                    print("voltando ao menu....")
                    time.sleep(2)
                    voltar_menu_sistema.voltar_menu()