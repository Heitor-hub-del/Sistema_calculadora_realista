import voltar_menu_sistema
import time

def converte_tempo(input1):

    if input1 == "10":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("conversor de tempo escolhido")

        else:
            print("voltando ao menu....")
            time.sleep(2)
            voltar_menu_sistema.voltar_menu()


            print("1. segundos para minutos")
            print("2. minutos para horas")
            print("3. horas pára dias")
            print("4. dias para semanas")
            print("5. semanas para meses")
            print("6. meses para anos")

            usuario = input("qual voce deseja converter?:")

            if usuario == "1":
                segundos = int(input("digite os segundos que deseja converter:"))

                minutos = segundos / 60

                print(f"a conversão de {segundos} segundos para minutos é: {minutos} minutos")

                print("1. sim")
                print("2. não")

                sujestões_conversor_tempo = input("gostaria de continuar de converter tempo?:")

            elif usuario == "2":
                minutos = int(input("digite os minutos que deseja converter:"))

                horas = minutos / 60

                print(f"a conversão de {minutos} minutos para horas é: {horas} horas")

                print("1. sim")
                print("2. não")

                sujestões_conversor_tempo = input("gostaria de continuar de converter tempo?:")

            elif usuario == "3":
                horas = int(input("digite as horas que deseja converter:"))

                dias = horas / 24

                print(f"a conversão de {horas} horas para dias é: {dias} dias")

                print("1. sim")
                print("2. não")

                sujestões_conversor_tempo = input("gostaria de continuar de converter tempo?:")

            elif usuario == "4":
                dias = int(input("digite os dias que deseja converter:"))

                semanas = dias / 7

                print(f"a conversão de {dias} dias para semanas é: {semanas} semanas")

                print("1. sim")
                print("2. não")

                sujestões_conversor_tempo = input("gostaria de continuar de converter tempo?:")

            elif usuario == "5":
                semanas = int(input("digite as semanas que deseja converter:"))

                meses = semanas / 4.34524

                print(f"a conversão de {semanas} semanas para meses é: {meses} meses")

                print("1. sim")
                print("2. não")

                sujestões_conversor_tempo = input("gostaria de continuar de converter tempo?:")
            
            elif usuario == "6":
                meses = int(input("digite os meses que deseja converter:"))

                anos = meses / 12

                print(f"a conversão de {meses} meses para anos é: {anos} anos")

                print("1. sim")
                print("2. não")

                sujestões_conversor_tempo = input("gostaria de continuar de converter tempo?:")

                if sujestões_conversor_tempo == "1":
                    converte_tempo(input1)
                
                else:
                    print("voltando ao menu....")
                    time.sleep(2)
                    voltar_menu_sistema.voltar_menu()