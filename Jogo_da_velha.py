velha = [ [0 for i in range(3)] for j in range(3)]
max_jogadas = 9
linha = 0
coluna = 0
jogada = 0
continuar = 0


def verifica_conitnuar(msg):
    global continuar
    ok = False
    valor = 0
    while True:
        continuar = str(input(msg))
        if continuar.isnumeric():
            valor = int(continuar)
            ok = True
        else:
            print("Valor inválido, tente novamente")
        if ok:
            break
    return valor


def verifica_linha(msg):
    global linha
    ok = False
    valor = 0
    while True:
        linha = str(input(msg))
        if linha.isnumeric():
            valor = int(linha)
            ok = True
        else:
            print("Valor inválido, tente novamente")
        if ok:
            break
    return valor


def verifica_coluna(msg):
    global coluna
    ok = False
    valor = 0
    while True:
        coluna = str(input(msg))
        if coluna.isnumeric():
            valor = int(coluna)
            ok = True
        else:
            print("Valor inválido, tente novamente")
        if ok:
            break
    return valor




def menu():
    continuar=1
    while continuar:
        continuar = verifica_conitnuar("0. Sair \n"+
                              "1. Jogar novamente\n")
        if continuar == 1:
            redefine()
        elif continuar == 0:
            print("Saindo...")
        else:
            print("Valor inválido, tente novamente")


def game():
        jogada=0
        try:
            while vitoria() == 0 and jogada < max_jogadas:
                print("\nJogador: ", jogada%2 + 1)
                exibe()
                linha  = verifica_linha("\nLinha..:")
                coluna = verifica_coluna("Coluna.:")


                if velha[linha-1][coluna-1] == 0:
                    if(jogada%2+1)==1:
                        velha[linha-1][coluna-1]=1
                    else:
                        velha[linha-1][coluna-1]=-1
                else:
                    print("Não esta vazio")
                    jogada -=1


                if vitoria():
                    print("Jogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")


                if empate():
                    print("Jogado empatou após", jogada+1," rodadas")
                   
                jogada +=1
        except:
            print("Valor fora do intervalo, favor reiniciar o jogo!")
           


   
def vitoria():
    # Verifica linhas
    for i in range(3):
        soma = velha[i][0]+velha[i][1]+velha[i][2]
        if soma==3 or soma ==-3:
            return 1


    # Verifica colunas
    for i in range(3):
        soma = velha[0][i]+velha[1][i]+velha[2][i]
        if soma==3 or soma ==-3:
            return 1


    # Verifica diagonal principal e secundária
    diagonal_1 = velha[0][0]+velha[1][1]+velha[2][2]
    diagonal_2 = velha[0][2]+velha[1][1]+velha[2][0]
    if diagonal_1==3 or diagonal_1==-3 or diagonal_2==3 or diagonal_2==-3:
        return 1


    return 0


  # Verifica empate  
def empate():
    global jogada
    if jogada > max_jogadas:
        menu()
  # Exibe o jogo da velha  
def exibe():
    print(" 1   2   3")
    for i in range(3):
        for j in range(3):
            if velha[i][j] == 0:
                print(" _ ", end=' ')
            elif velha[i][j] == 1:
                print(" X ", end=' ')
            elif velha[i][j] == -1:
                print(" O ", end=' ')
           
        print()
               
def redefine():
    global velha
    global max_jogadas
    global linha
    global coluna
    velha = [ [0,0,0],
             [0,0,0],
             [0,0,0] ]
    max_jogadas = 9
    linha = 0
    coluna = 0
    game()


menu()