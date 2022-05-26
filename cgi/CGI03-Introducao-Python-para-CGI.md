# Uma introdução ao Python para scripts CGI

## Variáveis

Variáveis são criadas na primeira vez que um valor é atribuído a elas. Não existe a etapa de "declaração de variáveis" como em outras linguagens.

``` python
x = 10 

# a variável x é criada no momento que atribuímos o valor 10 a ela

print(x)

# imprime o conteúdo da variável x
```

## Tipos de dados (mascaramento)

As variáveis em Python podem conter qualquer tipo de valor. Elas não são "tipadas". Se quisermos atribuir um tipo a uma variável precisamos fazer um "mascaramento" (casting) de tipo. 

``` python
x = str(10)

# a variável x é criada mas agora seu tipo é String. Strings são uma cadeia de caracteres, como veremos adiante. Ou seja, aqui a variável x não contém um número inteiro - o número 10 - mas sim dois caracteres - o caracter 1 e caracter 0 - assim: '10'. Seu valor é, portanto, um texto e não um número.

y = int(10)

# aqui, sim, a variável y armazena um valor numérico de tipo inteiro, um int.
```

Para saber qual o tipo de uma variável usamos a função <code>type()</code>

``` python
print(type(x))

# imprime o tipo da variável x
```

## Criando Strings

Para criar uma string diretamente, sem fazer mascaramento de tipo, basta colocar o valor da string entre aspas duplas ou aspas simples.

``` python
texto = "Oi, oi, oi!"

# a variável chamada texto agora armazena a String "Oi, oi, oi!" (sem incluir as aspas, que são usadas apenas para indicar ao Python que o conteúdo que está entre elas é uma cadeia de caracteres, uma String)

x = 'Oi, oi, oi'

# é o mesmo que no caso anterior. A variável x agora armazena a cadeia de caracteres "Oi, oi, oi".

nome = "Gustavo"

# Uma cadeia de caracteres que forma a palavra Gustavo.

```

## Atribuição múltipla de valores

Podemos atribuir vários valores a variáveis diferens ao mesmo tempo, em uma só linha de código.

``` python
nome, apelido = "Gustavo", "profe"


# aqui criamos duas variáveis, chamadas nome e apelido. nome contém a string "Gustavo" e apelido contém a string "profe".

# essa linha é equivalente a:

nome = "Gustavo"
apelido = "profe"

```

## Tipos de dados comuns do Python

Estes são alguns tipos de dado comuns do Python, separados em grupos:

### Texto: <code>str</code>
``` python
nome = "Gustavo"
```
### Números: <code>int, float</code>
``` python
x = 10 # este é um inteiro
y = 10.5 # este é um float
```

### Lógicos: <code>bool</code>
``` python
pronto = True
# este é um Booleano com valor de verdade True (verdadeiro)

acabou = False
# booleano com valor Falso
```


1. Sequências: <code>range, list</code>

``` python
nomes = ["André", "Amanda", "Arthur", "Bernardo"]

# nomes é uma variável que armazena uma lista de strings

# podemos acessar cada uma das strings dessa lista através de seu índice, que é a posição que a string ocupa na lista. 

print(nomes[0]) # imprime "André"
print(nomes[1]) # imprime "Amanda"

# o índice dos valores de uma lista começa em 0


print(nomes[1:3])

# imprime os valores que estão entre os índices que vão de 1 a 3, parando no último valor, ou seja, o último valor não é incluído 

# o resultado é ['Amanda', 'Arthur']
```

1. Conjuntos: <code>set</code>

Conjuntos são diferentes de listas porque os valores que fazem parte de um conjunto não estão ordenados.

``` python
nomes = {"André", "Amanda", "Arthur", "Bernardo"}

# usamos chaves {} para criar um conjunto

```

Como não temos um índice para acessar os valores de um conjunto, já que eles não estão ordenados como em uma lista, precisamos passar por todos os valores de um conjunto para acessá-los ou para procurar um valor específico. 

``` python
for um_nome in nomes: 
    print(um_nome)
```

Esse comando, chamado 'for',percorre o conjunto <code>nomes</code> indo de valor em valor, na ordem em que estiverem armazenados.

Para cada valor ('for' quer dizer 'para') ele usa a variável que no exemplo chamamos de <code>um_nome</code> para armazenar esse valor. Em seguida o <code>for</code> executa o código que vem depois dos "dois pontos".

Então o que esse trecho de código está fazendo?

O <code>for</code> está iterando sobre o conjunto <code>nomes</code> e imprimindo (comando print()) cada um dos valores do conjunto. E ele faz isso armazenando os valores do conjunto, um de cada vez em <code>um_nome</code> e depois imprimindo o valor dessa variável. Na próxima iteração do <code>for</code> o valor de <code>um_nome</code> será o valor do próximo ítem do conjunto e o <code>print(um_nome)</code> irá imprimir esse outro valor e assim por diante até o final do conjunto.


### Dicionário: <code>dict</code>

Dicionários são usados para criar relações entre dois valores, que podem ser de qualquer tipo. Como em um dicionário de verdade, onde associamos um significado a uma palavra-chave.

``` python

enderecos = {
  "André": "Porto Alegre",
  "Amanda": "Cachoeirinha",
  "Bernardo": "Canoas"
}

## Cria um mapa que mapeia uma string (que contém um nome) a outra string (que contém um endereço)


```

Dicionários são como tabelas, com duas colunas, onde a primeira coluna é a <code>chave</code> que usamos para indexar os valores que estão armazenados na segunda coluna - que é chamada de coluna dos <code>valores</code>

Para acessar os valores de um Dicionário usamos a <code>chave</code> como índice e recebemos como resposta o <code>valor</code> associado a ela.

``` python

cidade = enderecos["Amanda"]

# retorna o valor "Cachoeirinha" e armazena ele na variável cidade

print(cidade)

# imprime "Cachoeirinha"

```


Para acessar todas as <code>chaves</code> de um Dicionário podemos usar o método <code>keys()</code>.

``` python
for x in enderecos.keys():
    print(x)

# imprime todos os valores da coluna que contém as chaves da tabela
```

Para acessar todos os <code>valores</code> da tabela usamos o método <code>values()</code>.

``` python
for x in enderecos.values():
    print(x)
```

Para acessar <code>chaves</code> e <code>valores</code> ao mesmo tempo:

``` python
for x, y in enderecos.item()
    print(x, y)
```

## Estruturas de controle condicional - If..Else

Podemos executar um bloco de código condicionalmente. Isso quer dizer que o bloco de código será executado apenas se uma determinada condição for satisfeita (for verdadeira).

Para isso usamos valores Booleanos (Verdadeiro/Falso) que são testados pelo comando <code>if</code>

``` python
nome = "amanda"

if nome == "amanda":
	print("sim")
    
if nome == "bernardo":
	print ("nao")

```