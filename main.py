import math

def conversor_celsius_fah (temperatura):
    tem_em_fah = temperatura * 9/5 + 32
    print (f"{round(tem_em_fah)} °F")

def conversor_fah_celsius(temperatura):
    temp_em_celsius = (temperatura - 32) * 5/9
    print(f"{round(temp_em_celsius)} °C")


def inicio():
    resposta_user = int(input("Para converter de Celsius para Fahrenheit, tecle: 1\nPara converter de Fahrenheit para Celsius,tecle 2:"))
    if resposta_user == 1 :
        temperatura = int(input("Digite a temperatura em graus Celsius: "))
        print(f"{temperatura} °C em °F é: ")
        conversor_celsius_fah(temperatura)

    elif resposta_user ==2 :
        temperatura = int(input("Digite a temperatura em graus Fahrenheit: "))
        print(f"{temperatura} °F em °C  é: ")
        conversor_fah_celsius(temperatura)

    else:
        nova_tentativa = input("O valor digitado não corresponde a nenhuma das alternativas, deseja tentar novamente (S ou N):").lower()
        if nova_tentativa == "s":
            inicio()
        else:
            print("Obrigado por usar nosso conversor! ")


inicio()