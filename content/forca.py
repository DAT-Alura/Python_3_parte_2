def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "batata"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = (input("Qual a letra? ")).strip()
        index = 0
        for letra in palavra_secreta.upper():
            if (chute.upper() == letra):
                print("Encontrei a letra {} na posição {}".format(chute, index))
            index = index + 1
        print("jogando ...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
