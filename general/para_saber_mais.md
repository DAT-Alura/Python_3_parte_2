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

## Set

### Quando uma sequência não é suficiente

Já aprendemos algumas características das sequências. Elas guardam valores de qualquer tipo de dado e possuem uma determinada ordem, pois possuem um índice. As sequências também são chamadas de coleções e são o arroz e feijão para qualquer desenvolvedor Python!

Agora dá uma olhada no exemplo abaixo onde criamos uma lista de CPFs:

```py
lista = [11122233344, 22233344455, 33344455566]
```

Nada errado aqui, mas imagine agora que você precisa evitar que exista algum CPF duplicado nesta lista. Isso é algo muito comum no dia-a-dia! Em muitas circunstâncias precisamos de uma coleção que não permita valores duplicados, mas nada nos impede adicionar um mesmo CPF nessa lista, por exemplo:

```py
lista.append(11122233344) #funciona!
```

Isso também funciona se fosse uma tuple! Uma tuple também permite elementos duplicados!

### Conhecendo o set

E agora? Será que o Python não oferece alguma coleção onde não podem existir elementos duplicados? Claro que existe uma coleção com esse propósito e ela se chama __set__.

Veja o mesmo exemplo, mas agora inicializando um set:

```py
colecao = {11122233344, 22233344455, 33344455566}
```

Repare que usamos {} chaves para declarar os elementos iniciais. Pouca diferença comparando com as sequências, não?

### Adicionando elementos no set

Para adicionar um elemento a um set devemos chamar a função ```add``` (invés da ```append```):

```py
colecao.add(44455566677) #vai adicionar pois não existe ainda
```

E se usarmos um CPF que já existe? Não deve funcionar, certo? Vamos testar,e ver que o set vai ignorá-lo:

```py
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!
```

### set não possui um índice

É importante notar que o set não é uma sequência, pois não tem um índice. O código abaixo não funciona:

```py
colecao[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```

Isso mesmo, não tem índice. E como não temos um índice não sabemos em qual ordem vem os valores quando imprimimos um set de dentro de um laço for:

```py
for cpf in colecao:
     print(cpf)
```

Imprime:

```py
11122233344
44455566677
33344455566
22233344455
```

Repare que os elementos foram listados fora da ordem de inserção. Isso acontece porque o set não é ordenado.

### Resumindo

Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos duplicados dentro do set.

Respire fundo e fique tranquilo pois o ```set``` será abordado ainda com mais detalhe em outros cursos. Vamos continuar?

## Dictionary

Você aguenta aprender mais um pouco sobre coleções? Então vamos lá :)

Vamos lembrar rapidamente do último exemplo no vídeo quando misturamos as listas e tuples. Primeiro criamos pessoas com nome e idade usando ```tuple```:

```py
pessoa1 = ("Nico", 39)
pessoa2 = ("Flavio", 37)
pessoa3 = ("Marcos", 30)
```

Depois guardamos as tuples dentro de uma lista:

```py
instrutores = [pessoa1, pessoa2, pessoa3]
```

Se imprimimos ```instrutores``` recebemos:

```py
[('Nico', 39), ('Flavio', 37), ('Marcos', 30)]
```

Para saber a idade do ```Flavio```, devemos usar os índices (primeiro da lista, depois da tuple). Lembrando que acessamos o índice com os ```[]```:

```py
instrutores[1][1]
37
```

Agora vem o problema: E se não sabemos a posição do ```Flavio```? Em geral, como podemos descobrir a idade de um instrutor sem saber a posição dele?

### Instrutor pelo nome

Repare que temos, na nossa coleção, sempre um __nome__ associado com a __idade__. Sempre temos um par de valores, aqui é:

```py
nome : idade
```

Invés de usar a posição gostaria de descobrir a idade através do nome, algo assim:

```py
instrutores['Flavio']
```

Só que isso não vai funcionar com lista, nem com tuple, nem combinando os dois :( É preciso usar uma nova estrutura de dados, o __Dictionary__!

### Conhecendo o dictionary

Para criar um dicionário devemos inicializar os instrutores de um modo um pouco diferente. Veja o código:

```
instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
```

Repare que usamos as chaves ```{}``` (como se fosse um set), mas sempre tem em pares. O primeiro par é ```'Nico' : 39```, o segundo é ```'Flavio': 37```, etc.

Nesse par, temos no lado esquerdo a __chave__ e no lado direito o ```valor```. Isso é importante pois usamos a chave para recuperar um valor e assim resolvemos nosso problema:

```py
instrutores['Flavio']
```

Imprime:

```py
37
```

Isso foi apenas uma introdução, mas não se preocupe pois veremos ainda mais sobre dicionários dentro da carreira Python 3.

## Outra maneira de sair do loop

Vimos nesse capítulo que as variáveis ```acertou``` e ```enforcou``` foram usadas para controlar a saída do loop. Enquanto elas não forem verdadeiras, o código dentro do loop será executado. Para que o loop seja encerrado, criamos atribuições para essas variáveis.

```py
enforcou = erros == 6
acertou = "_" not in letras_acertadas
```

Contudo, essa não é única maneira de sair de um loop. Podemos usar também a palavra reservada break que, quando executada, irá encerrar o loop naquele ponto. Como podemos alterar nosso código da forca para utilizar o break e sair do while?

## Inicializando uma lista de números pares

O recurso List Comprehension também permite utilizar condições para o preenchimento da lista. Considere o objetivo de inicializar uma lista com os números pares a partir de uma lista de números inteiros qualquer, por exemplo, os números 1,3,4,5,7,8,9. Para descobrir se um número é par, usamos a condição numero%2 == 0, que verifica se o resto de uma divisão por 2 é zero. O código abaixo usa um loop para inicializar a lista de pares.
```py
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
```
Pesquise como o podemos usar o List Comprehension para fazer o mesmo que o código acima.

Resposta:

Dado o código de geração da lista de pares abaixo:
```py
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
```
O código usando List Comprehension relativo ficaria muito mais enxuto:
```py
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
```
Repare o ```if``` depois do ```for``` que define a condição! Muito melhor não?

## With

Já falamos da importância de fechar o arquivo, certo? Veja o código abaixo que justamente usa a função close :

```py
logo = open('palavras.txt', 'r')
data = logo.read()
logo.close()
```

Agora imagine que dê algum problema na hora da leitura quando chamarmos a função ```read()```. Será que mesmo com erro o arquivo será fechado?

Se for algum erro grave, o programa pode parar a execução sem ter fechado o arquivo! Isso seria muito ruim ...

Para evitar esse tipo de situação, o Python criou uma sintaxe especial para abertura de arquivo. Veja só:

```py
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
```

Repare que o ```with``` usa a função ```open```. Repare também que não fechamos o arquivo. Isso não é mais necessário pois o Python vai cuidar disso e, mesmo com erro, garantirá o fechamento do arquivo! Muito melhor não?
