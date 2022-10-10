# Pedro Victor Saraiva de  Sá - RM 93627

'''
Jogo da velha
'''

import random

'''
Função que inicializa o tabuleiro, isto é, prepara o tabuleiro para a jogada.Os parâmetros e o retorno devem ser definidos pelo programador.

1º while -> Criando variável linha com lista vazia e variável "j" que servirá como coluna

2º while -> While que será interado para inicializar as 3 colunas que cada linha irá possuir, percebe-se que quando esse loop é finalizado e passado para a próxima linha, o valor da variável j é zerado

No fim a variável "linha" armazena o valor da linha com os valores das 3 colunas e passamos um "append" na variável "tabuleiro" para armazenar esses valores.

Quando o loop do 1º while chegar ao fim será retornado a variável "tabuleiro" com o valor das 3 linhas e das 3 colunas
'''
def inicializaTabuleiro():
    tabuleiro = []
    i = 0
    while i < 3:
        linha = []
        j = 0
        while j < 3:
            coluna = " "
            linha.append(coluna)
            j+=1
        tabuleiro.append(linha)
        i+=1
    return tabuleiro


'''
Função que imprime o tabuleiro de jogo da velha para o usuário. Obviamente, se ele já estiver preenchido com X's e O's, 
então estes deverão ser impressos.Não há retorno. Os parâmetros devem ser definidos pelo programador.

Essa função que terá a representação gráfica do "Jogo da Velha". Será muito utilizada na função "modoJogador()" logo abaixo.

@while - A partir dos prints gerados nesse while que será apresentado os valores que vão ser colocados em cada coluna das 3 linhas do jogo da velha

Utilizei a condicional If para dar um fim a essa linha gerado no momento que chegar na 3º linha (índice 2)
''' 
def imprimirTabuleiro(tabuleiro):
    print("\n")
    i = 0
    while i < 3:
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i != 2:
            print("-----------")
        if i == 2:
            print("\n")
        i+=1


'''
Função que imprime menu principal do jogo. Os parâmetros e o retorno devem ser definidos pelo programador.

@var pontjX - Significa pontuação jogador X
@var pontjO - Significa pontuação jogador O

Caso você escolha jogar, será chamado a função "modoJogador()" contendo o programa principal logo abaixo
'''
def imprimeMenuPrincipal():
    print("\nJogo da Velha")
    print("1 - Jogador Usuário contra Jogador Usuário \n2 - Sair\n")
    opcao = int(input("Digite a opção desejada: "))
    pontjX = 0
    pontjO = 0
    if opcao == 1:
        modoJogador(pontjX, pontjO)
    else:
        print("Obrigado por jogar!\nEncerrando programa...")
        exit()


'''
Função sem parâmetros lê e devolve para o usuário a coordenada da linha.

Está retornando "linha - 1" por causa que a busca pela linha está sendo feita a partir do seu índice
'''
def lerLinha():
    linha = int(input("Digite a linha (1, 2 ou 3): "))
    return linha - 1


'''
Função sem parâmetros lê e devolve para o usuário a coordenada da coluna.

Mesma lógica da função "lerLinha()" logo acima.
'''
def lerColuna():
    coluna = int(input("Digite a coluna (1, 2 ou 3): "))
    return coluna - 1

'''
Função que imprime o status do jogo, ou seja, a pontuação de cada jogador na partida. Essa função deve ser chamada diversas vezes, sempre que iniciar um novo jogo. 
Não há retorno. Os parâmetros devem ser definidos pelo programador.

Função apenas de imprimir a pontuação de cada jogador ao final.
'''
def imprimePontuacao(jogadorX, jogadorO):
    print(
        f"-*Pontuação*-\nJogador (X): {jogadorX} x Jogador (O): {jogadorO}")


'''
Recebe coordenadas de linha e coluna e verifica se aquela posição é válida (ou seja, se ela já está ocupada no tabuleiro e se aquela posição está vazia). O retorno deve ser definido pelo programador. Sugestão: retornar um valor booleano. Observação: se preferir, você pode adicionar adicionais além das coordenadas de linha e coluna nessa função.

1º validação - Se a linha ou a coluna for maior que 3 ou menor que 1 significa que não faz parte das posições do tabuleiro, assim está fora da matriz

2º validação - Se a coluna da linha que você escolheu for diferente de " ", significa que já está ocupada

3º validação - Se a coluna da linha que você escolheu for igual a " ", significa que não está ocupado. Então é true.
'''
def posicaoValida(linha, coluna, tabuleiro):
    if linha not in range(3) or coluna not in range(3):
        print("Posição fora da Matriz! Digite novamente...")
        imprimirTabuleiro(tabuleiro)
        return False
    elif tabuleiro[linha][coluna] != " ":
        print("Posição já ocupada! Digite novamente...")
        imprimirTabuleiro(tabuleiro)
        return False
    elif tabuleiro[linha][coluna] == " ":
        return True


'''
Função que verifica se houve um vencedor, seja ele o jogador 1, jogador 2 ou máquina. 
Os parâmetros e o retorno devem ser definidos pelo programador.

1º for - Utiliza condicional para definir se o valor de cada uma das 3 linhas possuem valores iguais e diferentes de vazio

2º for - Utiliza condicional para definir se o valor de cada uma das 3 colunas possuem valores iguais e diferentes de vazio

3º if e elif - Verificação especificas paras as diagonais da esquerda para direita e direita para esquerda, respectivamente

4º Else - Ninguém venceu, jogo continua.
'''
def verificaVencedor(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            print(f"O jogador com {tabuleiro[i][0]} venceu!")
            return True
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != " ":
            print(f"O jogador com {tabuleiro[0][j]} venceu!")
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        print(f"O jogador com {tabuleiro[0][0]} venceu!")
        return True
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        print(f"O jogador com {tabuleiro[2][0]} venceu!")
        return True
    else:
        return False

'''
Função que verifica se o jogo encerrou em velha, isto é, empate.
Os parâmetros e o retorno devem ser definidos pelo programador.
'''

def verificaVelha(tabuleiro):
    contador = 0
    for i in tabuleiro:
        for j in i:
            if j != " ":
                contador += 1
    if contador == 9:
        print("O jogo empatou!")
        return True
    else:
        return False

'''
Função que realiza todas as operações para a opção de usuário-jogador vs usuário-jogador.
Os parâmetros e o retorno devem ser definidos pelo programador.

@while - Verifica apenas se deu empate ou houve um vencedor, Caso haja, então o loop acaba e vai para condicional para realizar uma pergunta para caso queira jogar novamente, assim realizando a recursividade.
'''
def modoJogador(pontjX, pontjO):
    tabuleiro = inicializaTabuleiro()
    jogadorX = "X"
    jogadorO = "O"
    aux = False
    imprimePontuacao(pontjX, pontjO)
    while aux == False:
        imprimirTabuleiro(tabuleiro)
        jogadaUsuario(tabuleiro, jogadorX)
        aux = verificaVencedor(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            pontjX += 1
            break
        aux = verificaVelha(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            break
        imprimirTabuleiro(tabuleiro)
        jogadaUsuario(tabuleiro, jogadorO)
        aux = verificaVencedor(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            pontjX += 1
            break
        aux = verificaVelha(tabuleiro)
        if aux == True:
            imprimirTabuleiro(tabuleiro)
            break
    cond = input("Deseja jogar novamente? (S/N) ")
    if cond == "S" or cond == "s":

        # Utilizando recursividade, reaproveitando a própria função e fazendo ela consumir ela mesmo em mais jogadas até que o usuário escreva algo fora da condição logo acima
        modoJogador(pontjX, pontjO)
    else:
        print("\nObrigado por jogar!\nEncerrando programa...")
        return


'''
Função que recebe as coordenadas de linha e coluna e preenche exclusivamente o tabuleiro. O atribuição no tabuleiro só pode ser feito por esta função. Ela deverá ser usada pelos jogadores e pelo computador. A função jogada apenas atribui "X" ou "O" no tabuleiro. A validação da jogada (por exemplo, se a coordenada é válida ou não) deve ser feita em outra função. Observação: se preferir, você pode adicionar adicionais além das coordenadas de linha e coluna nessa função. O retorno deve ser definido pelo programador.
'''
def jogar(linha, coluna, tabuleiro, XouO):
    tabuleiro[linha][coluna] = XouO


'''
Função que recebe as coordenadas do jogador e obrigatoriamente chama a função jogar para inserir no tabuleiro.
O retorno deve ser definido pelo programador.
'''
def jogadaUsuario(tabuleiro, XouO):
    print(f"Jogador {XouO} digite a linha e a coluna que deseja jogar:")
    linha = lerLinha()
    coluna = lerColuna()
    if posicaoValida(linha, coluna, tabuleiro) == True:
        jogar(linha, coluna, tabuleiro, XouO)
    else:
        # Caso a posição não seja válida, a função é chamada novamente
        jogadaUsuario(tabuleiro, XouO)


'''
Principal
'''
imprimeMenuPrincipal()
