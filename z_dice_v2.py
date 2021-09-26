from random import randint


# definicao de classes e métodos
class Jogador:
    def __init__(self, nome, cerebro, tiro, passo):
        self.nome = nome
        self.cerebro = cerebro
        self.tiro = tiro
        self.passo = passo

    cerebro = 0
    tiro = 0
    passo = 0

    def mostra_pontos(self):
        print("Cérebros: ", self.cerebro, "Tiros: ", self.tiro, "Passos: ", self.passo)

    def set_cerebro(self):
        pass

    def set_tiro(self):
        pass

    def set_passo(self):
        pass


# definicao de listas
copo_dados = []
dado_gr = ("T", "P", "C", "P", "C", "T")
dado_yw = ("T", "P", "T", "C", "P", "T")
dado_rd = ("C", "P", "C", "T", "P", "C")

lista_jogadores = []


# definicao de funcoes
def enche_copo():
    for i in range(0, 6):
        copo_dados.append(dado_gr)
    for i in range(0, 4):
        copo_dados.append(dado_yw)
    for i in range(0, 3):
        copo_dados.append(dado_rd)


def rola_dado():
    for i in range(0, len(copo_dados)):
        dado = randint(0, len(copo_dados) - 1)
        dado_jogado = copo_dados.pop(dado)
        return dado_jogado


# definicao de variaveis globais
partida = False

# lógica do jogo

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
            pass  # todo: adicionar intância de classe Jogador
        else:
            print("Valor invalido, o jogo precisa de pelo menos 2 jogadores.\n")

        enche_copo()
        partida = True

    except:
        print("Valor invalido, o jogo precisa de pelo menos 2 jogadores.\n")

while partida == True:
    try:
        pass
    except:
        pass
