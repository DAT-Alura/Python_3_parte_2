import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt")
    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = (input("Qual a letra? ")).strip().upper()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        if (erros == 6 or '_' not in letras_acertadas):
            break

    if('_' not in letras_acertadas):
        print("Você acertou! :)")
    else:
        print("Você errou! :(")


if(__name__ == "__main__"):
    jogar()
