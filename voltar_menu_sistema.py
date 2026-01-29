
import time
import math
import voltar_menu_sistema
import soma_sistema
import subtração_sistema
import multiplicação_sistema
import divisão_sistema
import potencialização_sistema
import loop_sistema
import porcentagem_sistema
import fatorial_sistema
import diferenciar_numeros_sistema
import conversor_tempo_sistema
import calculo_palavras_sistema
import formação_palavras_sistema
import conceitos_sistema
import saida_sistema

def voltar_menu():
    
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. potencialização")
    print("6. fazer um loop")
    print("7. porcentagem")
    print("8. fatorial")
    print("9. diferenciar numeros")
    print("10. converter tempo")
    print("11. fazer calculos com letras ou palavras")
    print("12. formação de palavras")
    print("13. usar os conceitos matematicos")
    print("14. sair")

    input1 = input("digite o numero do calculo que deseja fazer:")

    print("processando...")

    time.sleep(2)

    if input1 == "1":
        soma_sistema.soma(input1)
        

    elif input1 == "2":
        subtração_sistema.subtração(input1)
        

    elif input1 == "3":
        multiplicação_sistema.multiplicação(input1)
        

    elif input1 == "4":
        divisão_sistema.divisão(input1)
        

    elif input1 == "5":
        potencialização_sistema.potencialização(input1)
        
    elif input1 == "6":
        loop_sistema.loop(input1)

    elif input1 == "7":
        porcentagem_sistema.porcentagem(input1)
        
    elif input1 == "8":
        fatorial_sistema.fatorial(input1)
        

    elif input1 == "10":
        conversor_tempo_sistema.converte_tempo(input1)
        

    if input1 == "11":
        calculo_palavras_sistema.calculo_palavras(input1)

         
    elif input1 == "12":
        formação_palavras_sistema.formação_palavras(input1)
            

    elif input1 == "13":
        conceitos_sistema.conceitos(input1)     


    elif input1 == "14":
        saida_sistema.saida()
        
            

             



