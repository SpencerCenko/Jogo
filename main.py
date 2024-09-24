'''
Jogo do Adivinhe o Número
Data: 30/07/2024
Autor: Spencer Cenko
'''
#objetivo desenvolver um jogo em que o usuario deve tentar adivinhar um numero secreto sorteado pelo pc

#módulos e bibliotecas
from random import randint #importa o randint da biblioteca random
#variaveis
msg = "" #variavel para mensagens
numerosecreto = 0 #usado para o sorteio do numero secreto

#constantes
CAR = "!" #caractere usado para desenhar a estrutura do jogo
TDT = 50 #tamanho da tela a ser desenhada
MAR = 2 #margem 2 caracteres
INI = 1 #define o inicio do range
FIM = 100 #define o final do range
TVS = 3 #define o numero de tentativas
#listas
listaMsgs = [] #variavel para lista de msgs

#funções
#função para mostrar uma linha de caracteres
def mostralinha(): #função para mostrar a linha
  print(CAR*TDT) #printa car vezes tdt

#função para mostrar um texto centralizado entre um dos caracteres
#função para mostrar um cabecalho com texto entre linhas
def msgCentro(msg): #define a mensagem do centro
  print(f"{CAR} {msg:^{TDT-MAR-MAR}} {CAR}") #printa a mensagem no centro do bloco feito dos caracteres escolhidos
def cabecalho(listaMsgs): #define o cabeçalho
  mostralinha() #mostra a linha
  for msg in listaMsgs: 
    msgCentro(msg)
  mostralinha() #mostra a linha
#função para sortear o numero secreto
def sorteianum(): #define a função de sortear o numero
  numerosecreto = randint(INI,FIM) #sorteia o numero desde a variavel ini ate a fim
  return numerosecreto #retorna o numerosecreto
def pegaResposta(): #define pega resposta
  resposta = input(f"{CAR} Sua Resposta: ") #pega a resposta
  while not resposta.isdigit(): #enquanto resposta não for um digito
    listaMsgs = ["Resposta Invalida!", "Tente um numero"] #diz resposta invalida
    cabecalho(listaMsgs) # abre o cabeçalho
    resposta = input(f"{CAR} Sua resposta: ") #pega a resposta
  resposta = int(resposta) #define resposta com inteiro
  return resposta #retorna resposta
  
#função para dar a dica
def dica(numerosecreto, resposta): #define dica
  if numerosecreto > resposta: #se numero secreto for maior que resposta
    cabecalho("Tente um numero maior") #cabeçalho diz tente um numero maior
  else: # contrario do if
    cabecalho("Tente um numero menor")#cabeçalho diz tente um numero menor
    
#função para startar o jogo
def startgame(): #define o startgame
  TVS = 3 #define o numero de tentativas
  numerosecreto = sorteianum() #fala que numero secreto é recebe sorteianum
  listaMsgs = ["JOGO DO ADIVINHE O NUMERO", "Powered by spencer cenko"] #fala que o cabeçalho é o definido
  cabecalho(listaMsgs) #abre o cabeçalho
  playgame(TVS, numerosecreto) #chama playgame

def playgame(TVS, numerosecreto): #define playgame
  for tentativas in range(TVS): # define o numero de tentativas
    resposta = pegaResposta() #pega a resposta
    testeacerto = resposta == numerosecreto #testa se você acertou o numero secreto
    if testeacerto: #casi acerte      
      listaMsgs = ["OLOKO BIXO!!!", "ACERTROU MEMO!!!", "PARABENS YOU WIN!"] #coloca na lista de mensagens as palavras em questão
      cabecalho(listaMsgs) #abre o cabeçalho
      break #para o codigo
    elif tentativas != 2: # se tentativas não for igual a 2
      listaMsgs = ["pior que o catavento", "fraco demais"] #coloca na lista de mensagens essas palavras
      dica(numerosecreto, resposta) # da dica
    else: #caso não tenha a condição anterior
      cabecalho("esperava mais") #coloca esperava mais no cabeçalho
  else: #caso não tenha a condição anterior
    listaMsgs = ["o numero secreto era", numerosecreto, "parabens you lose"] #coloca na lista de mensagens a palavra em questão
    cabecalho(listaMsgs) #abre o cabecalho
    listaMsgs = ["Deseja jogar novamente?", "[ 0 - nao]", "[1 - sim"] # coloca na lista de mensagens a pergunta se quer jogar dnv ou não
    cabecalho(listaMsgs) #abre o cabeçalho
    resposta = pegaResposta() 
    if resposta == 1: #se respostaq for igual a 1
      startgame() #começa o jogo
    else: #se não
      listaMsgs = ("FOI BOM JOGAR COM VC - ATÉ") #diz a frase em questão
      cabecalho(listaMsgs) #abre o cabeçalho
      
#programa principal
startgame() #começa o jogo
