import random
import time 
import os 

temp = '🐶🐶🐒🐒🐱🐱🐴🐴🐷🐷🐢🐢🐇🐇🐝🐝'
figuras = list(temp)

print('='*40)
print('Jogo da Memória')
print('='*40)

nome = input('Digite seu nome: ')
pontuacao = 0

jogo = []
apostas = []

def preenche_matriz():
    for i in range(4):
        jogo.append([])
        apostas.append([])

        #Sorteio 
        for _ in range(4):
            num = random.randint(0, len(figuras)-1)
            jogo[i].append(figuras[num])
            apostas[i].append('♦️ ')
            figuras.pop(num)

def mostra_tabuleiro():
    os.system('cls')
    print('   1   2   3   4')
    for i in range(4):
        print(f'{i+1}', end='')
        for j in range(4):
            print(f' {jogo[i][j]} ', end='')
        print('\n')

    print('Memorize a posição dos bichos...')
    time.sleep(2)

    print('Contagem regressiva: ', end = '')
    for i in range(10, 0, -1):
        print(i , end =' ', flush = True)
        time.sleep(1)

    os.system('cls')

def mostra_apostas():
    os.system('cls')
    print('   1   2   3   4')
    for i in range(4):
        print(f'{i+1}', end='')
        for j in range(4):
            print(f' {apostas[i][j]} ', end='')
        print('\n')

preenche_matriz()
mostra_tabuleiro()

mostra_apostas()

def faz_aposta(num):
    while True:
        mostra_apostas()
        posicao = input(f'{num}ª Coordenada (2 numeros: linha e coluna): ')
        if len(posicao) != 2:
            print('Informe uma dezena, por exemplo: 12, 24, 31...')
            time.sleep(2)
            continue
        x = int(posicao[0]) -1
        y = int(posicao[1]) -1
        try: 
            if apostas[x][y] == '♦️ ':
                apostas[x][y] = jogo[x][y]
                break
            else:
                print('Coordenada já apostada.')
                time.sleep(2)
        except IndexError:
            print('Coordenada Inválida... repita.')
            time.sleep(2)
    return x, y

def verifica_tabuleiro():
    faltam = 0
    for i in range(4):
        for j in range(4):
            if apostas[i][j] == '♦️ ':
                faltam += 1
    return faltam


while True:
    x1, y1 = faz_aposta(1)
    x2, y2 = faz_aposta(2)
    mostra_apostas()

    if apostas[x1][y1] == apostas[x2][y2]:
        print('Parabéns! Você acertou!')
        pontuacao += 10
        contador = verifica_tabuleiro()
        if contador == 0:
            print('Parabéns! Você venceu!🏆')
            print(f'Jogador: {nome} Pontuação: {pontuacao}')
            break
        else:
            print(f'Faltam {contador/2} bicho(s) para descobrir...')
            time.sleep(2)
    else:
        print('Você errou, tente novamente...')
        pontuacao -= 5
        time.sleep(2)
        apostas[x1][y1] = '♦️ '
        apostas[x2][y2] = '♦️ '
        sair = input('Deseja sair? (S/N): ')
        if sair == 's'.lower():
            break
    
    
 #==============================#
 #          Exercicios          #
 #==============================#
 #1. Solicitar nome do jogador 
 #2. Definir pontuação (acerto +10, erro -5)
 #3. No final exibir nome e pontuação 
 #4. Armazenar hora inicial e final e exibir o tempo de jogo 
 #5. Salvar nome, pontuação e tempo em arquivo texto
 #6. Mostrar ranking
