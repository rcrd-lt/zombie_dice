# Disciplina de Raciocíno computacional - PUCPR - Aluno: Ricardo A. Soares Leite
import random

comeca_partida = False

#define os valores para os dados
dado_vermelho = ("Cerebro", "Passos", "Cerebro", "Tiro", "Passos", "Cerebro")
dado_verde = ("Tiro", "Passos", "Cerebro", "Passos", "Cerebro", "Tiro")
dado_amarelo = ("Tiro", "Passos", "Tiro", "Cerebro", "Passos", "Tiro")

#define as listas
copo_dados = []
dados_jogados = []
lista_jogadores = []

cerebros = 0
tiros = 0

comeca_partida = False
turno = False


# mostrar os dados;
# mostrar os dados no copo;
# pegar cada um dos tipos de dados (verde, amarelo, vermelho);
# verificar score (cérebros, tiros e passos).

def adicionar_dados():    #adicionar os dados
    for i in range(0, 6):
        copo_dados.append(dado_verde)
    for i in range(0, 4):
        copo_dados.append(dado_amarelo)
    for i in range(0, 3):
        copo_dados.append(dado_vermelho)


def lanca_dados():
    num_sorteado = int(random.randrange(len(copo_dados)))
    print("Dado sorteado {}: {} ".format((i + 1), num_sorteado))

    dado_sorteado = copo_dados[num_sorteado]  # 'lança' o dado e verifica qual a face sorteada
    face_dado = int(random.randrange(0, 5))  # obtem a face do dado

    if dado_sorteado[face_dado] == "C":  # tirou "cerebro no dado
        print("Você comeu um cérebro!!")
        copo_dados.remove(dado_sorteado)

    elif dado_sorteado[face_dado] == "T":  # tirou tiro no dado
        print("Você levou um tiro!!")
        copo_dados.remove(dado_sorteado)

    else:
        print("A vítima escapou!!")



while len(lista_jogadores) == 0:
    # numero_jogadores = int(input("Digite o número de jogadores na partida: \n"))
    # for ind in range(0, numero_jogadores):
    #     nome = input("Qual o nome do jogador? \n")
    try:
        numero_jogadores = int(input("Digite o número de jogadores na partida: \n"))
        if numero_jogadores >= 2:
            for i in range(0, numero_jogadores):
                nome = input("Qual o nome do jogador?" )
                lista_jogadores.append(nome)
        else:
            print("O jogo precisa de 2 ou mais jogadores!\n")
        comeca_partida = True
        turno = True
        adicionar_dados()
    except:
        print("O jogo precisa de 2 ou mais jogadores!\n")


print("Partida iniciada! ")
while comeca_partida == True:   #PAREI AQUI RS

    #Rever loops
    #adicionar turnos
    #troca de jogadores

    for i in range(len(lista_jogadores)):
        try:
            print("\n olá, {}, digite o que deseja fazer:".format(nome))
            jogar = int(input("[1] - Jogar os dados, [2] Finalziar turno ou [3] Trocar de jogador: \n"))
        except:
            print("valor inválido!")
        if jogar == 1:
            for i in range(0, 3):
                lanca_dados()

        elif jogar == 2:
            pontos = cerebros
            print("Turno finalizado! Fez", pontos, "pontos!")
            print(lista_jogadores)
            turno += 1

        elif jogar == 3:
            print("Próximo jogador!")
            adicionar_dados()