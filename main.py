input('Bem vindo ao jogo da luta! Pess. ENTER ↵ para continuar ')
input('As características principais de seu persoagem são: Vitalidade e Ataque.')
input('Seu personagem inicia com 100 pontos de cada atributo.')

valid_nome1 = False                                             #Validação dos nomes
valid_nome2 = False
while valid_nome1 == False:
    nome1 = input('\nDigite o nome do seu personagem:\n')
    if nome1.isalpha():
        valid_nome1 = True
    else:
        print('\nDigite apenas letras.')
while valid_nome2 == False:
    nome2 = input('Digite o nome do seu oponente:\n')
    if nome2.isalpha():
        valid_nome2 = True
    else:
        print('\nDigite apenas letras.')                         #Validação dos nomes

input('\n{}, prepare-se que você acaba de se inscrever no jogo da luta.'.format(nome1))
input('Lute contra {} com todas suas forças!'.format(nome2))
input('\n{}, para vencer você precisa atacar e tirar todos pontos de vitalidade de {}.'.format(nome1,nome2))


jogador1 = {'Vida':100,'Ataque':100,'Defesa':100}               #Características Iniciais do jogador
jogador2 = {'Vida':100,'Ataque':100,'Defesa':100}               #Características Iniciais da máquina

from random import randint                                      #Para utilizar números aleatórios
from random import uniform                                      #Para utilizar números aleatórios
from time import sleep

def calcula_ataque(x):                                          #Função que calcula um valor aleatório
    ataque = x * uniform(2.0,4.5)
    ataque //= 15
    return ataque

input('\nPREPARADO?\n')
input('\nPressione ENTER para atacar:\n')

print(('-')*20)
print('Começa a pancadaria!')
print(('-')*20)
sleep(1)

soco = calcula_ataque(jogador1['Ataque'])                                                   #Chamar a função de ataque considerando a força de ataque das características do jogador
jogador2['Vida'] = jogador2['Vida'] - soco                                                  #Subtração dos PV pelo valor do ataque
print('Eita, NOSSA!')
sleep(1)
print('{} acerta um soco na cara de {}.'.format(nome1,nome2))
sleep(2)
print('{} perde {} PV.'.format(nome2,soco))
sleep(2)
print('{} começa a chorar, deixando {} irritado.'.format(nome2,nome1))
sleep(2)
input('{} fica com {}PV após esse socão.'.format(nome2,jogador2['Vida']))                   #Imprime a quantidade de vida após o ataque

input('\n{}, fica esperto que agora você tem que se defender.'.format(nome1))
input('Quando estiver pronto pressione a tecla ENTER.')

soco = calcula_ataque(jogador2['Ataque'])
jogador1['Vida'] = jogador1['Vida'] - soco
sleep(1)
print('Quibisurdo!!!')
sleep(1)
print('Um soco no nariz foi recebido.')
sleep(2)
print('{} perde {} PV por ter levado esse murro na fuça.'.format(nome1,soco))
sleep(2)
input('{} fica com {}PV após receber um soco no nariz.'.format(nome1,jogador1['Vida']))     #Imprime a quantidade de vida após o ataque    
sleep(2)
input('\nApós essa troca de agressões, o nível de cansaço e stress aumenta.')
sleep(0.8)
input('{} está ofegante e {}, cansado.'.format(nome2,nome1))
ataque = randint(5,10)                                                                      #Aleatório para redução do ataque jogador 1
jogador1['Ataque'] = jogador1['Ataque'] - ataque 
sleep(1)
input('\nDevido ao cansaço, {} perde {} pontos de ataque.'.format(nome1,ataque))

ataque = randint(5,10)                                                                      #Aleatório para redução do ataque jogador 2
jogador2['Ataque'] = jogador2['Ataque'] - ataque 
input('{} machucou seu braço, comprometendo {} pontos de seu ataque.'.format(nome2,ataque))


input('\nAgora é o momento da voadora, dessa vez quem começa atacando é {}.'.format(nome2))
input('Se prepara pq lá vem bicuda!')

print()
print(('-')*20)
print('  Momento Bicuda!')
print(('-')*20)
sleep(2)

voadora = calcula_ataque(jogador2['Ataque'])                                                #Chamar a função de ataque considerando a força de ataque das características do jogador
jogador1['Vida'] = jogador1['Vida'] - voadora                                               #Subtração dos PV pelo valor do ataque
print('\nAgora eu vi!')
sleep(2)
print('{} sai voando nas costas de {}.'.format(nome2,nome1))
sleep(2)
print('{} perde {} PV.'.format(nome1,voadora))   
sleep(2)
input('{}PV é o que resta para {} após essa voadora na coluna.'.format(jogador1['Vida'],nome1))                   #Imprime a quantidade de vida após o ataque

voadora = calcula_ataque(jogador1['Ataque'])                                                #Chamar a função de ataque considerando a força de ataque das características do jogador
jogador2['Vida'] = jogador2['Vida'] - voadora                                               #Subtração dos PV pelo valor do ataque
input('\n{}, prepare as pernas pq agora é hora de usá-las.'.format(nome1))
input('PRONTO?')
sleep(1)
print('\nEu heeeeeeeeein!')
sleep(2)
print('{} acerta um chute na boca do estômago de {}.'.format(nome1,nome2))
sleep(2)
print('{} perde {} PV.'.format(nome2,voadora))   
sleep(2)
input('{} fica com {}PV após esse golpe na barriga.'.format(nome2,jogador2['Vida']))                   #Imprime a quantidade de vida após o ataque

input('\nA coisa começa a ficar preta.')
sleep(0.5)
input('{} olha para {} e {} olha para {}.'.format(nome1,nome2,nome2,nome1))
input('{} começa a se irritar e dar chilique.'.format(nome2))
input('{} não suporta tanta frescura e solta um peido.'.format(nome1))
input('{} tenta prender sua respiração mas {} começa a ventilar a carniça para cima de {}.'.format(nome2,nome1,nome2))
input('{} fica debilitado devido à potência do peido de {}.'.format(nome2,nome1))
#input('Então {} entra em um acordo com {} para escolherem o vencedor através do Par ou Impar.'.format(nome2,nome1))
input('O cheiro do peido fica impregnado em {}, despertando uma força impressionante.'.format(nome2))
input('{} encontra um pedaço de pau podre e vai para cima de {}.'.format(nome2,nome1))
input('A raiva é tão grande que uma paulada é fatal.')
sleep(1)

print()
print(('-')*20)
print('   Momento Tenso!')
print(('-')*20)
print()
sleep(2)

input('{} pede desculpas e diz que não imaginava que o peido seria tão carnicento.'.format(nome1))
input('Mas isso não é suficiente para fazer com que {} desista da paulada.'.format(nome2))
sleep(1)

print()
print(('-')*20)
print('   !!! ATENÇÃO !!!')
print(('-')*20)
print()
sleep(2)
input('{} tem 50% de chance de sobreviver, basta desviar da paulada e efetuar um contra-ataque.'.format(nome1))
input('Não reclama pq a culpa é do seu peido.')
print('Fica ativo pq ele tá chegando...')
sleep(2)
print('5')
sleep(1)
print('4')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(2)
print('{} veio correndo com toda sua fúria com um pedaço de pau podre em suas mãos.'.format(nome2))
sleep(3.5)
input('{} levanta o pau e ...'.format(nome2))
sleep(2)
input('\n**\nUm número aleatório entre 1 e 2 será sorteado.\nSe {} escolher o número correto, sobrevive, senão, irá morrer com a paulada.\n**\n'.format(nome1))

valid_num = False
while valid_num == False:
    numero_sorteado = str(randint(1,2))
    numero_escolhido = input('Digite 1 ou 2:\n')
    if numero_escolhido == '1' or numero_escolhido == '2':
        valid_num = True
        if numero_sorteado == numero_escolhido:
            input('{} desce o pedaço de pau em {}, mas {} foi mais esperto.'.format(nome2,nome1,nome1))
            input('Conseguiu desviar e voltou com uma joelhada na cara de {}.'.format(nome2))
            print('O vencedor foi...')
            sleep(2)
            print('...')
            sleep(2)
            print('...')
            sleep(2)
            print('**********')
            print(nome1.upper())
            print('**********')
            sleep(2)
            print('Que sorte em kkkkk')
        else:
            input('{} desce o pedaço de pau em {}...'.format(nome2,nome1))
            input('e acerta em cheio, o pau ate quebrou...'.format(nome1))
            input('{} desmaia e fica inconsciente.'.format(nome1))
            print('O vencedor foi...')
            sleep(2)
            print('...')
            sleep(2)
            print('...')
            sleep(2)
            print('**********')
            print(nome2.upper())
            print('**********')
            sleep(2)
            print('Viu, quem mandou você peidar kkkk')


""" PAR OU IMPAR 
valid_escolha = False
while valid_escolha == False:
    poi = input('\nEscolha par ou impar digitando [P] ou [I]:\n').lower()
    if poi == 'i' or poi == 'p':
        valid_escolha = True

valid_entrada = False                                       #Valida a entrada do número inteiro de 0 a 10.
num_maq = randint(0,10)
while valid_entrada == False:
    num_esco = input('Escolha um número:\n')
    try:
        num_esco = int(num_esco)
        if num_esco <0 or num_esco >10:
            print('\nEscolha apenas números entre 0 e 10.')
        else:
            valid_entrada = True
    except:
        print('\nDigite apenas números inteiros')

soma = num_esco + num_maq

if soma % 2 == 0:
    result = 'par'
    resultado = 'p'
else:
    result = 'impar'
    resultado = 'i'

if poi == 'i':
    escolha = 'impar'
else:
    escolha = 'par'

print('E o vencedor foi ...')
sleep(2)
input()
print('\n{} escolheu {} e o número {}, {} escolheu {}.'.format(nome1,escolha,num_esco,nome2,num_maq))    
sleep(1)
if poi == resultado:
    print('Parabéns, {} foi o vencedor da luta!\n'.format(nome1))
else:
    print('{} foi o vencedor!!!! {} perdeu, culpa do peido carnicento.\n'.format(nome2,nome1))
"""
