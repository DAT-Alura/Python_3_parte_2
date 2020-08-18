# Perguntas

## Aula 1

1 - Gustavo decidiu praticar o que aprendeu no vídeo deste capítulo e escreveu o seguinte código. Leia-o atentamente:
```py
def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    palavra_secreta = "banana"
    enforcou = false
    acertou = false

    while(Not enforcou and Not acertou):
        print("jogando...")

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()
```
No entanto, seu código não funcionou. Sem executar o programa, apenas olhando o código anterior, podemos afirmar que a quantidade de erros cometidos é:

- 3
- __4__
> São quatro erros. Os valores lógicos das variáveis enforcou e acertou iniciam com letra minúscula. O correto é maiúscula como True e False. Já o operador not foi utilizado duas vezes começando com letra maiúscula, quando no correto é minúscula.
- 2

2 - Qual é o tipo que representa verdadeiro ou falso no mundo Python?

- __bool__
> Correto! O tipo se chama bool!
- int
- bool()
- boolean

> Devemos utilizar o tipo bool para representar verdadeiro (True) e falso (False), por exemplo:
> 
> ```>>> existe = True```  
> ```>>> type(existe)```  
> ```<class 'bool'>```
> 
> Dica: Nesse tipo de perguntas, sinta-se sempre à vontade de usar a documentação do Python. Aliás, aconselhamos a usar a documentação para se acostumar. É um documento bastante técnico e menos didático, mas ajuda tirar dúvidas pontuais: https://docs.python.org/3.5/index.html
