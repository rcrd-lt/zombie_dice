# Disciplina de Raciocíno computacional - PUCPR - Aluno: Ricardo A. Soares Leite
import random

# define os valores para os dados
dado_vermelho = ("Cerebro", "Passos", "Cerebro", "Tiro", "Passos", "Cerebro")
dado_verde = ("Tiro", "Passos", "Cerebro", "Passos", "Cerebro", "Tiro")
dado_amarelo = ("Tiro", "Passos", "Tiro", "Cerebro", "Passos", "Tiro")

# define as listas
copo_dados = []
dados_jogados = []
lista_jogadores = []
cerebros = []
tiros = []
passos = []

comeca_partida = False
turno = False

# pegar cada um dos tipos de dados (verde, amarelo, vermelho);
# verificar score (cérebros, tiros e passos).

def adicionar_jogador():
    for jogador in range(0, numero_jogadores):
        nome = input("Qual o nome do jogador? \n")
        lista_jogadores.append(nome)


def adicionar_dados():  # adicionar os dados
    for i in range(0, 6):
        copo_dados.append(dado_verde)
    for i in range(0, 4):
        copo_dados.append(dado_amarelo)
    for i in range(0, 3):
        copo_dados.append(dado_vermelho)


def lanca_dados():
    c = 0
    t = 0
    p = 0
    num_sorteado = int(random.randrange(len(copo_dados)))
    dado_sorteado = copo_dados[num_sorteado]  # 'lança' o dado e verifica qual a face sorteada
    face_dado = int(random.randrange(0, 5))  # obtem a face do dado

    if dado_sorteado[face_dado] == "Cerebro":  # tirou "cerebro no dado
        print("Você comeu um cérebro!!")
        copo_dados.remove(dado_sorteado)
        cerebros.append(c)

    elif dado_sorteado[face_dado] == "Tiro":  # tirou tiro no dado
        print("Você levou um tiro!!")
        copo_dados.remove(dado_sorteado)
        tiros.append(t)

    else:
        print("A vítima escapou!!")
        passos.append(p)


def mostra_copo():              #adicionar ao fim da rodada
    print("Os dados restantes são: {} \n".format(copo_dados))


while len(lista_jogadores) == 0:
    try:
        numero_jogadores = int(input("Digite o número de jogadores na partida: \n"))
        if numero_jogadores >= 2:
            adicionar_jogador()
        else:
            print("O jogo precisa de 2 ou mais jogadores!\n")
        comeca_partida = True
        turno = True
        adicionar_dados()
    except:
        print("O jogo precisa de 2 ou mais jogadores!\n")

print("Partida iniciada! ")
while comeca_partida == True:
    try:
        adicionar_dados()
        print("\n olá, digite o que deseja fazer:")
        jogar = int(input("[1] - Jogar os dados, [2] Finalizar turno \n"))
    except:
        print("valor inválido!")

        if jogar == 1:
            for i in range(0, 3):
                lanca_dados()
                mostra_copo()

        elif jogar == 2:
            print("O jogo foi finalizado")
            comeca_partida = False
            restart = input("Deseja iniciar a partida novamente? [s] Sim - [n] Não")
            if restart == 's':
                comeca_partida == True
            elif restart == 'n':
                print("Obirgado por jogar! Até a próxima!")