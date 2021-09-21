# Disciplina de Raciocíno computacional - PUCPR - Aluno: Ricardo A. Soares Leite
import random
from collections import namedtuple
comeca_partida = False

#define os valores para os dados
dado_vermelho = namedtuple("Vermelho", ["Cerebro", "Passos", "Cerebro", "Tiro", "Passos", "Cerebro"])
dado_verde = namedtuple("Verde", ["Tiro", "Passos", "Cerebro", "Passos", "Cerebro", "Tiro"])
dado_amarelo = namedtuple("Amarelo", ["Tiro", "Passos", "Tiro", "Cerebro", "Passos", "Tiro"])

#define as listas
copo_dados = []
dados_jogados = []
lista_jogadores = []

comeca_partida = False
turno = False

def adicionar_dados():    #adicionar os dados
    for i in range(0, 6):
        copo_dados.append(dado_verde)
    for i in range(0, 4):
        copo_dados.append(dado_amarelo)
    for i in range(0, 3):
        copo_dados.append(dado_vermelho)







while len(lista_jogadores) == 0:
    # numero_jogadores = int(input("Digite o número de jogadores na partida: \n"))
    # for ind in range(0, numero_jogadores):
    #     nome = input("Qual o nome do jogador? \n")
    try:
        numero_jogadores = int(input("Digite o número de jogadores na partida: \n"))
        if numero_jogadores >= 2:
            for i in range(0, numero_jogadores):
                nomes = input("Qual o nome do jogador?" )
                lista_jogadores.append(nomes)
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
                num_sorteado = int(random.randrange(len(copo_dados)))
                print("Dado sorteado {}: {} ".format((i + 1), num_sorteado))

                dado_sorteado = copo_dados[num_sorteado]  # 'lança' o dado e verifica qual a face sorteada
                face_dado = int(random.randrange(0, 5))  # obtem a face do dado

                if dado_sorteado[face_dado] == "C":  # tirou "cerebro no dado
                    print("Você comeu um cérebro!!")
                    cerebros = cerebros + 1
                    copo_dados.remove(dado_sorteado)

                elif dado_sorteado[face_dado] == "T":  # tirou tiro no dado
                    print("Você levou um tiro!!")
                    tiros = tiros + 1
                    copo_dados.remove(dado_sorteado)

                else:
                    print("A vítima escapou!!")


        elif jogar == 2:
            pontos = cerebros
            print("Turno finalizado! Fez", pontos, "pontos!")
            print(lista_jogadores)
            turno += 1
            tiros = 0

        elif jogar == 3:
            print("Próximo jogador!")
            adicionar_dados()
            vez = lista_jogadores.index(player[i])








        #try:
         #   if():
          #  else:

        #except:
        #    print()

        # if numero_jogadores >= 2:
        #     comeca_partida = True # iniciar a partida
        #     cerebros = 0
        #     tiros = 0
        #     adicionar_dados()
        #     i = 1
        #     while (i < numero_jogadores +1):
        #         player = dict({'jogador': i, 'cerebros': 0, 'tiros': 0})
        #         lista_jogadores.append(player)
        #         i = i + 1


