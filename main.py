#programa_principal
#receber_peso
#receber_altura
#confirmar_dados
#converter
#calcular_imc
#classificar_imc
#mostrar_estado

from calculos import receber_peso, receber_altura, confirmar_dados, calcular_imc, classificar_imc

while True:
    try:
        peso = receber_peso()       
        peso = float(peso)       
        altura = receber_altura()
        altura = float(altura)
        
    except ValueError:
        print("Digite apenas numeros. ")
        continue

    confirma = confirmar_dados()
    if confirma:
     print("Os seus dados estao corretos, prosseguindo com o programa.")

    else:
     print("Os seus dados estao incorretos, reiniciando o programa.")
     continue

    calcula = calcular_imc(peso, altura)
    print(f"\nSeu IMC: {calcula}")

    classificacao = classificar_imc(calcula)
    print(f"\nA sua classificaçao atual é: {classificacao}")
    break

      

        
