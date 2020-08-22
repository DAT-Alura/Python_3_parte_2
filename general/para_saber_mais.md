# Para saber mais

## Built-In

No curso anterior, falamos bastante sobre as funções built-in, como type(..), int() ou input(..). Lembrando que funções built-in são aquelas que você não precisa importar explicitamente, pois elas estão disponíveis para seu uso automaticamente.

Existe uma função relacionado com o tipo bool, com o mesmo nome. Veja o código abaixo:
```py
>>> bool(0)
False
>>> bool("")
False
>>> bool(None)
False
>>> bool(1)
True
>>> bool(-100)
True
>>> bool(13.5)
True
>>> bool("teste")
True
>>> bool(True)
True
```
Repare que os valores vazios ou zeros são considerado False, do contrário são considerados True.

A função executa por baixo dos panos algo que se chama de "Truth Value Testing". Isto é, decidir quando um valor é considerado True ou False.

## Alterações com strings

No último vídeo vimos uma série de funções que fazem parte do tipo str (string). Algumas funções foram úteis para verificar se há alguma substring dentro da palavra, como por exemplo find, startswith ou endswith.

Outras funções tem a função de alterar a palavra como upper, lower, capitalize ou strip. Quando falamos sobre esse tipo de funções, é importante lembrar que elas na verdade não alteram a string original. Por exemplo, veja esse código abaixo e tente descobrir a saída:
```py
>>> palavra = "alura"
>>> palavra.upper()
>>> print(palavra) #qual é o resultado?
```
A resposta é "alura" com letras minúsculas! Isto é porque o upper sempre devolve uma nova string e não altera a string original. Essa regra também aplica para todas as outras funções do tipo str!

O tipo str foi criado de tal maneira que é impossível alterá-lo, qualquer função de alteração devolve uma nova string, que representa a alteração. Esse principio também é chamado de imutabilidade. Strings são imutáveis, são sequências imutáveis!

O mais legal ainda é que strings não são a única sequência imutável e veremos ainda nesse curso uma outra. Aguarde :)

## Outros recursos com a lista

Além das funções min(), max() e len() que vimos neste capítulo, as listas do Python tem outros recursos que facilitam nossa vida. Vamos conhecer alguns deles:

### A função .count()

Um jeito fácil de contar o número de ocorrências de um determinado elemento em uma lista é a função .count() das listas, veja:

```py
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))
```

O código acima nos retorna 3, pois em nossa lista encontramos 3 vezes o número zero nela.

Utilizando a função .count() podemos por exemplo, detectar quantas letras ainda faltam para o nosso usuário preencher:

```py
letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
```

### A função .index()

Uma outra função que pode ser bastante útil é a função .index(), que nos retorna o índice da primeira ocorrência de um determinado elemento em uma lista, veja:

```py
frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))
```

O código acima nos retorna 3, pois é o índice da primeira ocorrência do elemento 'Uva' na lista frutas (lembre-se nas listas começamos a contar do índice 0).

Só tome cuidado quando utilizar a função .index(), pois a mesma pode retornar um erro caso você tente buscar pelo índice de um elemento que não existe. Veja o caso abaixo:

```py
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas.index('Melancia'))
```

Ao tentar buscar pela fruta 'Melancia', obteremos o erro "ValueError: 'Melancia' is not in list" no console, já que é impossível buscar o índice de algo que não está na lista. Por isto, é sempre uma boa prática verificar se o elemento está na lista com o operador in antes de obter o seu índice. Um código ideal que faz uso da função index() é demonstrado abaixo:

```py
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))
```

Assim temos certeza que a fruta_buscada está dentro da lista antes de perguntarmos o seu índice, evitando assim de receber um erro no console.
