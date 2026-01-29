import math
import time
import voltar_menu_sistema


def conceitos(input1):
     if input1 == "13":

        print("1. sim")
        print("2. não")

        certeza = input("tem certeza que deseja continuar?:")

        if certeza == "1":
            print("uso de conceitos selecionado")

            print("1. cos")
            print("2. sin")
            print("3. tan")
            print("4. atan")
            print("5. acosh")
            print("6. asinh")
            print("7. asin")
            print("8. cosh")
            print("9. atan2")
            print("10. atanh")
            print("11. sinh")
            print("12. log")
            print("13. log2")
            print("14. log10")
            print("15. log1p")

            conceito_input = input("qual conceito voce quer fazer?:")

            if conceito_input == "1":
                num1 = int(input("digite um numero:"))

                cos_resultado = math.cos(num1)

                print(f"o resultado e: {cos_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "2":
                num1 = int(input("digite um numero:"))

                sin_resultado = math.sin(num1)

                print(f"o resultado e: {sin_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "3":
                num1 = int(input("digite um numero:"))

                tan_resultado = math.tan(num1)

                print(f"o resultado e: {tan_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "4":
                num1 = int(input("digite um numero:"))

                atan_resultado = math.atan(num1)

                print(f"o resultado e: {atan_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "5":
                num1 = int(input("digite um numero:"))

                acosh_resultado = math.acosh(num1)

                print(f"o resultado e: {acosh_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")
                
            elif conceito_input == "6":
                num1 = int(input("digite um numero:"))

                asinh_resultado = math.asinh(num1)

                print(f"o resultado e: {asinh_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")
                
            elif conceito_input == "7":
                num1 = int(input("digite um numero:"))

                asin_resultado = math.asin(num1)

                print(f"o resultado e: {asinh_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "8":
                num1 = int(input("digite um numero:"))

                cosh_resultado = math.cosh(num1)

                print(f"o resultado e: {cosh_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "9":
                num1 = int(input("digite um numero:"))

                atan2_resultado = math.atan2(num1)

                print(f"o resultado e: {atan2_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "10":
                num1 = int(input("digite um numero:"))

                atanh_resultado = math.atanh(num1)

                print(f"o resultado e: {atanh_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "11":
                num1 = int(input("digite um numero:"))

                sinh_resultado = math.sinh(num1)

                print(f"o resultado e: {sinh_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "12":
                num1 = int(input("digite um numero:"))

                log_resultado = math.log(num1)

                print(f"o resultado e: {log_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "13":
                num1 = int(input("digite um numero:"))

                log2_resultado = math.log2(num1)

                print(f"o resultado e: {log2_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "14":
                num1 = int(input("digite um numero:"))

                log10_resultado = math.log10(num1)

                print(f"o resultado e: {log10_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            elif conceito_input == "15":
                num1 = int(input("digite um numero:"))

                log1p_resultado = math.log1p(num1)

                print(f"o resultado e: {log1p_resultado}")

                print("1. sim")
                print("2. não")

                sujestões_conceitos = input("gostaria de usar mais os conceitos matematicos?:")

            if sujestões_conceitos == "1":
                    conceitos(input1)

            else:
                print("voltando ao menu....")
                time.sleep(2)
                voltar_menu_sistema.voltar_menu()