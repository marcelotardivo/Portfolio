import random

# CRIANDO NOSSA ACADEMIA
class Academia():
    def __init__(self):
        self.halteres = [i for i in range(10,210) if i%2==0] # LISTA DE HALTERES DISPONÍVEIS NA ACADEMIA
        self.porta_halteres = {}
        self.reiniciar_dia()

    def reiniciar_dia(self):
        self.porta_halteres = {i: i for i in self.halteres} # REORGANIZAÇÃO DOS HALTERES EM SEUS RESPECTIVOS ESPAÇOS CORRETOS

    def listar_halteres(self): # APRESENTAÇÃO DOS HALTERES DISPONÍVEIS PARA USO
        return [i for i in self.porta_halteres.values() if i!= 0]

    def listar_espacos(self): # APRESENTAÇÃO DOS HALTERES DISPONÍVEIS PARA USO
        return [i for i,j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso_escolhido): # FUNÇÃO QUE REPRESENTA QUE O CLIENTE PEGOU UM DOS HALTERES DISPONÍVEIS PARA USO
        peso_haltere = list(self.porta_halteres.values()).index(peso_escolhido) # TRAZENDO O ÍNDICE DA POSIÇÃO EM QUE ESTÁ O HALTERE ESCOLHIDO
        espaco_haltere =list(self.porta_halteres.keys())[peso_haltere] # TRAZENDO O ESPAÇO EM QUE ESTÁ O HALTER ESCOLHIDO
        self.porta_halteres[espaco_haltere] = 0 # QUANDO O CLIENTE PEGAR O PESO, O ESPAÇO FICA DISPONÍVEL
        return peso_haltere

    def devolver_haltere(self, posicao, peso):
        self.porta_halteres[posicao] = peso # QUANDO O CLIENTE DEVOLVER O HALTERE, ADICIONAMOS O VALOR À POSIÇÃO

    def calcular_caos(self):
        caos_absoluto = [i for i, j in self.porta_halteres.items() if i != j] # AQUI IDENTIFICAMOS A QUANTIDADE DE HALTERES FORA DE SEUS RESPECTIVOS ESPAÇOS
        return len(caos_absoluto)/len(self.porta_halteres) # AQUI CALCULAMOS O PERCENTUAL DE HALTERES FORA DE SEUS RESPECTIVOS ESPAÇOS

class Cliente:
    def __init__(self, tipo, academia):
        self.tipo = tipo # 1: BAGUNCEIRO; 2: ORGANIZADO
        self.academia = academia # TRAZEMOS A SITUAÇÃO EM QUE A ACADEMIA SE ENCONTRA QUANDO O CLIENTE FOR PEGAR O HALTERE
        self.peso = 0 # INICIALMENTE O CLIENTE NÃO ESTÁ SEGURANDO NENHUM PESO

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres() # LISTANDO TODOS OS PESOS DISPONÍVEIS PARA O CLIENTE PEGAR
        self.peso = random.choice(lista_pesos) # O CLIENTE ESCOLHE UM DOS PESOS, DE MANEIRA ALEATÓRIA
        self.academia.pegar_haltere(self.peso) # QUANDO O CLIENTE PEGAR UM DOS HALTERES, DEIXAMOS O ESPAÇO DISPONÍVEL

    def finalizar_treino(self): # COMO O CLIENTE VAI SE COMPORTAR NA HORA DE DEVOLVER O HALTERE
        espacos = self.academia.listar_espacos() # TODOS OS ESPAÇOS DISPONÍVEIS PARA O CLIENTE ALOCAR O HALTERE
        if self.tipo == 1: # SE O CLIENTE FOR DO TIPO BAGUNCEIRO
                self.academia.devolver_haltere(random.choice(espacos),self.peso) # CLIENTE POSICIONA EM UM ESPAÇO DISPONÍVEL ALEATÓRIO
        elif self.tipo == 2: # SE O CLIENTE FOR DO TIPO ORGANIZADO
            if self.peso in espacos: # SE O ESPAÇO REFERENTE AO PESO ESTIVER DISPONÍVEL
                self.academia.devolver_haltere(self.peso,self.peso) # O CLIENTE POSICIONA NO ESPAÇO REFERENTE AO PESO
            else: # SE O ESPAÇO REFERENTE AO PESO NÃO ESTIVER DISPONÍVEL
                self.academia.devolver_haltere(random.choice(espacos),self.peso) # CLIENTE POSICIONA EM UM ESPAÇO DISPONÍVEL ALEATÓRIO
        self.peso = 0 # AO DEVOLVER O PESO, O CLIENTE NÃO CARREGA PESO NENHUM

academia = Academia()

clientes = [Cliente(1,academia) for i in range(10)] # adicionando um cliente bagunceiro na academia
clientes += [Cliente(2,academia) for i in range(90)] # adicionando dez clientes organizados na academia

random.shuffle(clientes) # aleatorizando a ordem de clientes na lista

lista_caos = []
for k in range(6):
    academia.reiniciar_dia()
    for i in range (10): # CADA CLIENTE TREINA 10 VEZES
        random.shuffle(clientes)
        for cliente in clientes:
            cliente.iniciar_treino()
        for cliente in clientes:
            cliente.finalizar_treino()
    lista_caos += [academia.calcular_caos()]

from statistics import mean
print("Média de percentual de halteres em posição errada: {}".format(round(mean(lista_caos),2)))