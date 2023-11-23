import random

def mensagem_de_boas_vindas():
    print("Muito bem-vindo(a) ao jogo da forca em Python")

def pegar_palavra():
    with open("C://Alura//Python//Forca//PalavrasForca.txt", "r", encoding="utf-8") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializar_letras(letras):
    return ["_" for letra in palavra_secreta]   # List Comprehension

def recebendo_chute():
    chute = input("Qual a letra que deseja chutar? ")
    chute = chute.strip().upper()
    return chute

def verificando_chute(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta :
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


mensagem_de_boas_vindas()
palavra_secreta = pegar_palavra()
letras_acertadas = inicializar_letras(palavra_secreta)

print(letras_acertadas, "\n")

gameover = False
acertou = False
erros = 0

while (not gameover and not acertou):

    chute = recebendo_chute()

    if (chute in palavra_secreta):
        for letra in palavra_secreta:
            verificando_chute(chute, letras_acertadas, palavra_secreta)
    else:
        erros += 1
        tentativas_restantes = len(palavra_secreta) - erros
        print("Você ainda tem {} tentativas".format(tentativas_restantes))

    gameover = erros == len(palavra_secreta)
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

if (acertou):
    print("Parabéns você ganhou!")
else:
    print("Você perdeu! A palavra secreta era {}".format(palavra_secreta))