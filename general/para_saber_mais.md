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
