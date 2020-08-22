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

## Aula 2

1 - Temos a seguinte variável declarada, que armazena uma string:
```py
palavra = "aluracursos"
```
Com base na variável declarada anteriormente, marque somente as verdadeiras:

- palavra.find('s') # resultado é 9
- __palavra.find("l") # resultado é 1__
> Correto! Lembrando que as posições começam de 0 até o tamanho da string menos um. A posição 1 é a segunda letra, logo "l".
- palavra.find("a") # resultado é 4
- __palavra.find("b") # resultado é -1__
> Correto! Quando a busca nada encontra, o resultado é sempre -1.

> A função find encontra a primeira ocorrência do texto que estamos procurando e devolve o índice. Lembrando também que o índice começa com 0.
> 
> O find também aceita um segundo parâmetro, que define a partir de qual posição gostaríamos de começar, por exemplo:
> ```py
> >>> palavra = "aluracursos"
> >>> palavra.find("a",1) #procurando "a" a partir da segunda posição 
> 4
> ```

2 - Uma palavra nada mais é do que uma sequência de caracteres. Tanto isso é verdade, que podemos usar o laço for para iterar. Nesse contexto iterar significa receber em cada iteração uma letra da palavra.
Sabendo disso, qual das opções abaixo itera corretamente através da palavra Alura?

- A
```py
palavra = "Alura"
for letra in palavra:
    if(letra == "l"):
    print("Achou!")
```

- __B__
```py
palavra = "Alura"
for letra in palavra:
    if(letra == "l"):
        print("Achou!")
```
> Correto! Respeita a indentação do Python.

- C
```py
palavra = "Alura"
for palavra in letra:
    if(letra == "l"):
        print("Achou!")
```

> Nesse curso vamos falar ainda muito mais sobre sequências, mas já saiba que uma string não é a única sequência no mundo Python!

3 - Vamos recordar um exemplo de formatação de strings em Python:
```py
a = "Cavalo"
b = "Calopsita"
"{} e {}".format(b, a)
```
O que será exibido no terminal?

- 'Calopsita Cavalo'
- 'Cavalo e Calopsita'
- __'Calopsita e Cavalo'__
> Correto! Nossa string possui duas lacunas definidas com {}. Os parâmetros passados para a função format são passados na mesma ordem para preencherem a lacuna.

4 - Clarice aprendeu que strings não são apenas um local onde armazenamos informações, elas também sabem executar tarefas. Por exemplo, ela aprendeu a usar .format para formatar uma string.

Ela decidiu experimentar usar .capitalize no seguinte exemplo:
```py
nome = "clarice"
nome.capitalize()
```
No entanto, ao imprimir a variável nome, logo depois da instrução nome.capitalize(), a variável continuou com a primeira letra minúscula:
```py
nome = "clarice"
nome.capitalize()
print(nome) ## continua como clarice e não Clarice como ela esperava
```
Marque a opção abaixo que corrige o código de Clarice para que o resultado de print(nome) seja seu nome iniciando com a letra maiúscula.

- __A__
```py
nome = "clarice"
nome = nome.capitalize()
print(nome)
```
> Correto! Quando chamamos capitalize, no lugar dela alterar a variável, ela devolve um novo texto modificado. É por isso que precisamos capturar o retorno de capitalize() na própria variável, para que ela passe a apontar para o novo valor.
- B
```py
nome = "clarice"
nome.capitalize(nome)
print(nome)
```
- C
```py
nome = "clarice"
nome2 = nome.capitalize()
print(nome)
```
