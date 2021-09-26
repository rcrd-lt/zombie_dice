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

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self,nome):
        return nome

    def set_cerebro(self, cerebro):
        self.cerebro = cerebro

    def set_tiro(self, tiro):
        self.tiro = tiro

    def set_passo(self,passo):
        self.passo = passo


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
turno = False

# lógica do jogo

print("---------------\n")
regras = int(input("Bem vindo ao Zombie Dice Redux, deseje ler as regras do jogo? [1] - Sim [2] - Não\n"))
if regras == 1:
    print("REGRAS DO JOGO")
    partida = True
elif regras == 2:
    print("Ok, vamos prosseguir")
    partida = True

while partida == True:
    try:
        print("*** Partida iniciada ***")
        enche_copo()
        jogador1 = Jogador
        jogador1.set_nome(input("Digite o nome do jogador: \n"))
        jogador1.set_passo(0)
        jogador1.set_tiro(0)
        jogador1.set_cerebro(0)
        turno = True

        while turno == True:
            try:
                print("Olá {}, o que deseja fazer:\n [1] - Rolar dados [2] - Exibir status [3] Encerrar".format(jogador1.get_nome()))

            except:
                pass
    except:
        pass
