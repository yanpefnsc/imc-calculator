def receber_peso():
    peso = input("Digite o seu peso: ")
    return peso

def receber_altura():
    altura = input("Digite a sua altura: ")
    return altura

def confirmar_dados():
    dado = input ("O seu peso está correto?sim/nao : ")
    dado = dado.lower()
    if dado == "sim":
        return True
    else:
        return False      
    
def calcular_imc (peso, altura):
    resultado = peso / altura ** 2
    return resultado
    
def classificar_imc(imc):    
    if imc < 18.5:
        return "Voce esta abaixo do peso"
        
    elif imc < 25:
        return "Voce esta saudavel"
        
    elif imc < 30:
        return "Voce esta com sobrepeso"
    
    else:
        return "Obesidade grau 1"
        
        
        
