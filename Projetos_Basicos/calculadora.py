# NOME DO SCRIPT: CALCULADORA
# AUTOR: MARCELO TARDIVO

# IMPORTAR BIBLIOTECAS
from IPython.display import clear_output

# 1. FUNÇÕES
# 1.1 MENU
def menu():
    print("Selecione a operação desejada. \n \n")
    print("1. Soma (X + Y)")
    print("2. Subtração (X - Y)")
    print("3. Multiplicação (X * Y)")
    print("4. Divisão (X / Y)")
    print("9. Para sair da caluladora.")
    operacao = int(input("Operação desejada: "))
    return operacao

# 1.2 OPERAÇÕES
def soma(x,y):
    resultado = x + y
    return resultado

def subtracao(x,y):
    resultado = x - y
    return resultado

def multiplicacao(x,y):
    resultado = x * y
    return resultado

def divisao(x,y):
    if y == 0:
        resultado = "Impossível dividir por 0."
    else:
        resultado = x / y
    return resultado

def seleciona_operacao(operacao):
    if operacao == 1:  
        clear_output()
        print("Operação selecionada: Soma")
        x = float(input("Valor de X: "))
        y = float(input("Valor de Y: "))
        resultado = soma(x,y)

    elif operacao == 2:
        clear_output()
        print("Operação selecionada: Subtração")
        x = float(input("Valor de X: "))
        y = float(input("Valor de Y: "))
        resultado = subtracao(x,y)

    elif operacao == 3:
        clear_output()
        print("Operação selecionada: Multiplicação")
        x = float(input("Valor de X: "))
        y = float(input("Valor de Y: "))
        resultado = multiplicacao(x,y)

    elif operacao == 4:
        clear_output()
        print("Operação selecionada: Divisão")
        x = float(input("Valor de X: "))
        y = float(input("Valor de Y: "))
        resultado = divisao(x,y)

    elif operacao == 9:
        clear_output()
        resultado = "sair"
        
    return resultado

validacao = 'S'
variavel = ''
while (variavel != 'sair') and (validacao == 'S'):
    variavel = seleciona_operacao(menu())
    if variavel != 'sair':
        print(variavel)
        validacao = input("Deseja realizar mais alguma operação? <S/N>")
    if validacao != 'S' or variavel == 'sair':
        print("Calculadora encerrada")