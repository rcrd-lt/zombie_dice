import random

#definicao de classes e métodos
class Jogador:
    def __init__(self, nome, cerebro, tiro, passo):
        self.nome = nome
        self.cerebro = cerebro
        self.tiro = tiro
        self.passo = passo

class Dado:
    def __init__(self):
        self.dado_gr = ("T", "P", "C", "P", "C", "T")
        self.dado_yw = ("T", "P", "T", "C", "P", "T")
        self.dado_rd = ("C", "P", "C", "T", "P", "C")

#definicao de listas
copo_dados = []
lista_jogadores = []

#definicao de funcoes
def enche_copo():
    pass #todo: adicionar instâncias da classe Dado a copo_dados


#definicao de variaveis globais
partida = False


#lógica do jogo

print("---------------\n")
regras = int(input("Bem vindo ao Zombie Dice Redux, deseje ler as regras do jogo? [1] - Sim [2] - Não\n"))
if regras == 1:
    print("REGRAS DO JOGO")
elif regras == 2:
    print("Ok, vamos prosseguir")

while len(lista_jogadores) == 0:
    try:
        q_jogadores = int(input("Informe o numero de jogadores:\n"))
        if q_jogadores >= 2:
            pass #todo: adicionar intância de classe Jogador
        else:
            print("Valor invalido, o jogo precisa de pelo menos 2 jogadores.\n")

        enche_copo()

    except:
        print("Valor invalido, o jogo precisa de pelo menos 2 jogadores.\n")