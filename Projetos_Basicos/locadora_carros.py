# NOME DO SCRIPT: LOCADORA DE CARROS
# AUTOR: MARCELO TARDIVO

import pandas as pd 

# GERANDO A LISTA DE CARROS
disponiveis = {'fabricante':['Fiat','Chevrolet','Chevrolet','Hyundai','Fiat'],
        'modelo':['Uno','Tracker','Spin','Hb20'],
        'diária':[50.00,100.00,150.00,200.00,250.00]}
disponiveis = pd.DataFrame.from_dict(disponiveis, orient='index').T
alugados = pd.DataFrame()

def pagina_inicial():
    print("=================================================================================================")
    print("BEM VINDO À FERRAMENTA DE LOCADORA DE VEÍCULOS.")
    print("1. Acessar a lista de carros disponíveis para alugar.")
    print("2. Acessar a lista de carros alugados")
    print("3. Sair da ferramenta.")
    opcao = int(input("Informe a opção desejada: "))
    return opcao

def lista_menu(lista_disponiveis):
    print("===== LISTA DE CARROS DISPONÍVEIS PARA ALUGAR ===================================================")
    print(lista_disponiveis)
    print("=================================================================================================")

def alugar(item, alugados, disponiveis):
    # ADICIONAR CARRO SELECIONADO AOS ALUGADOS
    alugados = pd.concat([alugados,pd.DataFrame(disponiveis.iloc[item]).T]).reset_index(drop=True)
    # REMOVER CARRO SELECIONADO DOS DISPONÍVEIS
    disponiveis = disponiveis[disponiveis.index!=item].reset_index(drop=True)
    return alugados, disponiveis

def devolver(item, alugados, disponiveis):
    # ADICIONAR CARRO SELECIONADO AOS ALUGADOS
    disponiveis = pd.concat([disponiveis,pd.DataFrame(alugados.iloc[item]).T]).reset_index(drop=True)
    # REMOVER CARRO SELECIONADO DOS DISPONÍVEIS
    alugados = alugados[alugados.index!=item].reset_index(drop=True)
    return alugados, disponiveis

while True:
    opcao = pagina_inicial()
    if opcao == 1:
        lista_menu(disponiveis)
        item = int(input("Informe o id do carro que deseja alugar (digite -1 para voltar para a página inicial): "))
        if item == -1:
            print("\n")
        elif len(disponiveis[disponiveis.index == item]) == 0:
            print("Carro não encontrado.")
        else:
            dias = int(input("Informe a quantidade de dias que o carro estará alugado: "))
            if dias > 0:
                opcao = input("Tem certeza que deseja alugar por {0}. <S/N>".format(dias*float(disponiveis.loc[item,'diária'])))
                if opcao == 'S':
                    print(disponiveis.loc[item,'fabricante'] + " " + disponiveis.loc[item,'modelo'] + " alugado com sucesso!")
                    alugados, disponiveis = alugar(item, alugados, disponiveis)
    
    elif opcao == 2:
        lista_menu(alugados)
        item = int(input("Informe o id do carro que deseja alugar (digite -1 para voltar para a página inicial): "))
        if item == -1:
            print("\n")
        elif len(alugados[alugados.index == item]) == 0:
            print("Carro não encontrado.")
        else:
            opcao = input("O carro {0} voltará a ficar disponível para alugar. Tem certeza? <S/N>".format(alugados.loc[item,'fabricante'] + " " + alugados.loc[item,'modelo']))
            if opcao == 'S':
                    alugados, disponiveis = devolver(item, alugados, disponiveis)

    elif opcao == 3:
        print("Ferramenta cancelada.")
        break