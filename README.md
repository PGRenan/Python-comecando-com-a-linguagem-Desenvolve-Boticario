# Python-comecando-com-a-linguagem-Desenvolve-Boticario
 Este projeto faz parte do plano de estudos elaborado pela Alura para o programa de formação Desenvolve (3ª edição), trilha de dados, em parceria com a Boticário.

# Começando com a linguagem Python

Criando um jogo para aprender os recursos fundamentais do Python 3.

  - [1. Instalação do Python 3](#1-instalação-do-python-3)
  - [2. Lidando com a entrada do usuário](#2-lidando-com-a-entrada-do-usuário)
  - [3. Testando valores](#3-testando-valores)
  - [4. A sequência do jogo](#4-a-sequência-do-jogo)
  - [5. Iterando de maneira diferente](#5-iterando-de-maneira-diferente)
  - [6. Gerando números aleatórios](#6-gerando-números-aleatórios)
  - [7. Nível e Pontuação](#7-nível-e-pontuação)
  - [8. Organizando ainda melhor o nosso código](#8-organizando-ainda-melhor-o-nosso-código)
  - [9. Comparando Python com C](#9-comparando-python-com-c)

Saiba mais sobre o curso [aqui](https://cursos.alura.com.br/course/python-introducao-a-linguagem) ou acompanhe minhas anotações abaixo. ⬇️

## 1. Instalação do Python 3

### **Instalação do Python no Windows**

- Acessar a página do Python [aqui](https://www.python.org/) e fazer o download
- Marcar a opção `Add Python to PATH` antes de instalar
- Verificar instalação e versão a partir do `cmd` com `python --version`

### **Função print e variáveis**

A função `print` do Python funciona de forma semelhante ao `document.write` do JavaScript. Serve para imprimir (mostrar) uma mensagem na tela.

```py
print("Olá, mundo!")
```

A função `print` pode receber valores diversos, entre eles:

- `value` o valor ou valores, propriamente ditos, separados por vírgula
- `sep` o separador de valores, sendo o padrão um espaço em branco `sep=' '`
- `end` o finalizador da função, tendo como padrão uma quebra de linha `end='\n'`

Ao declarar uma variável é possível verificar o tipo de valor que foi utilizado, com a função `type()`. Nos casos abaixo, teremos uma `string` e um número `inteiro`.

```py
pais = "Itália"
type(pais)      # str = string

titulos = 4
type(titulos)   # int = inteiro
```

O Python trabalha com `tipagem dinâmica`, pois não é necessário dizer que existe uma variável. Basta dizer o nome e o valor da variável e ele já reconhece o tipo automaticamente. Sendo possível reatribuir valores de maneira dinâmica.

```py
pais = "Brasil" # type(pais) >>> <class 'str'>
pais = 55       # type(pais) >>> <class 'int'>
pais = 7.9      # type(pais) >>> <class 'float'>
```

Diferente do JavaScript que utiliza o `camelCase` como padrão de escrita. O Python utiliza por convenção o padrão `snake_case` para nomes de variáveis e identificadores.

```py
idade_esposa = 20
perfil_vip = 'Flávio Almeida'
recibos_em_atraso = 30
```

***

## 2. Lidando com a entrada do usuário

### **Comparando variáveis**

Assim como no JavaScript, o Python utiliza funções de comparação para fazer uma solicitação ou confirmação com o usuário. É o caso do `input` e do `if/else`.

```py
numero_secreto = 8
chute = input("Chute um número de 1 a 10", chute)

if(numero_secreto == chute):
  print("Você acertou")
else:
  print("Você errou")
```

Porém, o Python não converte texto para número sozinho. É preciso fazer essa conversão manualmente, utilizando a função `int`

```py
numero_secreto = 42

chute_str = input("Digite o seu número: ")  # chute como string

print("Você digitou ", chute_str)

chute = int(chute_str)                      # conversão

if numero_secreto == chute:                 # chute como número
    print("Você acertou!")
else:
    print("Você errou!")
```

O uso de parênteses no Python é opcional para as funções `if`, `while` e `for`. Uma vez que os parênteses ajudam na leitura e entendimento do código, seu uso se faz importante. Sendo necessário sempre manter os parênteses nos casos de operações aritméticas para controle da ordem de execução dos cálculos.

```py
if numero_secreto == chute:

# é o mesmo que

if(numero_secreto == chute):
```

O Python não faz conversão de texto em número, então é necessário converter manualmente as somas realizadas. Porém, ele realiza uma multiplicação de forma diferente, veja:

```py
numero1 = 10
numero2 = "20"
produto = numero1 * numero2

print(produto)

# o resultado é 20202020202020202020
```

Existe um termo para o resultado acima, é o `syntax sugar`. ao invés de escrever o número 20, 10 vezes. Podemos simplificar e escrever `10 * "20"`. Isso simplifica algo trabalhoso, mas não muda a característica de conversão de texto para número.

***

## 3. Testando valores

### **A condição elif**

O comando `elif` realiza a verificação de outra expressão, caso a primeira validação seja falsa. Sendo ele uma junção do `else` com o `if`. Podendo, também, aninhar em outros comandos.

```py
if(acertou):
  print("Você acertou")
else:
  if(chute > numero_secreto):
    print("O chute foi maior")
  elif(chute < numero_secreto):
    print("O chute foi menor")
```

***

## 4. A sequência do jogo

### **O laço com while**

O `while` é uma função que executa uma rotina. Ele possui uma condição de entrada e executa um bloco enquanto a condição declarada nele for verdadeira.

```py
numero_secreto = 42
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
  print("Tentativa", rodada, "de", total_tentativas)

  chute_str = input("Digite o seu número: ")
  print("Você digitou ", chute_str)
  chute = int(chute_str)

  acertou = chute == numero_secreto
  maior   = chute  > numero_secreto
  menor   = chute  < numero_secreto

  if (acertou):
    print("Você acertou!")
  else:
    if (maior):
      print("Você errou! O seu chute foi maior do que o número secreto.")
    elif (menor):
      print("Você errou! O seu chute foi menor do que o número secreto.")

  rodada = rodada + 1
```

### **Formatação de strings**

A expressão `str.format()` é utilizada para formatar strings para que seja melhor visualizado o que se pede. A string não é dividida ao meio para inserir uma variável, mas é sinalizado com "{}" que existe algo ali. Posteriormente, declarado no método format.

```py
quantidade = 6
print("Você ganhou", quantidade, "troféus.")

# utilizando format
print("Você ganhou {} troféus".format(quantidade))
```

Um número nas chaves pode ser usado para referenciar a posição do objeto passado no format. Outro nome para essa formatação é interpolação.

***

## 5. Iterando de maneira diferente

### **O laço for**

Outra função de repetição é chamada de `for`. Nela é possível definir os valores manualmente ou utilizar a função `range(start, stop, step)` para reduzir o código (o step é opcional). Tendo cuidado com o range, pois a posição final é não-inclusiva, ou seja, para que ele conte ade 1 até 10, usa-se o 11 como posição final.

```py
for rodada in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# com o range
for rodada in range(1, 11)

#incrementando o range de 2 em 2
for rodada in range(1, 11, 2)
```

Assim como em outras linguagens, para forçar a parada do laço no caso de acerto, pode-se utilizar a função `break`. Ao contrário do break, a função `continue` faz com que a rotina continue ou se repita a partir de um determinado ponto, caso o usuário não digite o que foi solicitado.

```py
print("Digite um número de 1 a 10")

if(chute < 1 or chute > 10):
  print("Digite um número de 1 a 10")
  continue

if(acertou):
  print("Você acertou")
  break
```

### **Formatação de strings 2**

Com a função `.format()` também é possível preencher caracteres em branco para alinhar dados numéricos em formato `float`. Float é o formato equivalente a números decimais, contudo é possível formatar inteiros também.

```py
"R$ {:f}".format(1.59)      # imprime "R$ 1.590000"
"R$ {:.2f}".format(1.59)    # imprime "R$ 1.59"
"R$ {:.2f}".format(1.5)     # imprime "R$ 1.50"
"R$ {:7.2f}".format(1234,5) # imprime "R$ 1234.50"
"R$ {:7.2f}".format(4,5)    # imprime "R$    4.50"
"R$ {:07.2f}".format(4,5)   # imprime "R$ 0004.50"
"R$ {:08.3f}".format(4,5)   # imprime "R$ 00004.500"
"R$ {:07d}".format(4,5)     # imprime "R$ 0000004"
"R$ {:07d}".format(46)      # imprime "R$ 0000046"
"R$ {:7d}".format(46)       # imprime "R$      46"

# formatando datas
"Data {:2d}/{:2d}".format(9, 4)     # imprime "Data  9/ 4"
"Data {:02d}/{:02d}".format(9, 4)   # imprime "Data 09/04"
"Data {:02d}/{:02d}".format(19, 11) # imprime "Data 19/11"
```

Com o `.format()`, podemos especificar a ordem em que os parâmetros aparecem na string, basta apenas colocar entre as chaves {} da string formatada qual parâmetro você quer exibir. É válido lembrar também, que o primeiro parâmetro é o zero, pois tradicionalmente na computação começamos contando de zero.

### **Formatted strings literals**

Quando colocamos a letra f antes das aspas, informamos ao Python que estamos utilizando uma f-string. Dessa forma o Python consegue, em tempo de execução, captar a expressão que está entre chaves {} e avaliá-la. Além de variáveis, podemos passar também de funções e métodos:

```py
>>> nome = 'Matheus'
>>> print(f'Meu nome é {nome}')

# imprime "Meu nome é Matheus"

nome = 'Matheus'
print(f'Meu nome é {nome.lower()}')

# imprime "Meu nome é matheus"
```

***

## 6. Gerando números aleatórios

### **Gerando e arredondando números aleatórios**

O módulo `random` é utilizado para gerar números pseudo-aleatórios. Também pode-se selecionar os elementos de uma lista de forma aleatória ou exibir o seu resultado embaralhado. Ele é formado por diversas funções que utilizam dados gerados a partir de um algoritmo de um dado original e produz um resultado aleatório com base nesse valor.

```py
random.seed()                       # inicializa o gerador de número aleatório
random.random()                     # retorna um decimal aleatório entre 0.0 e 1.0
random.randrange(start, stop, step) # retorna um número decimal aleatórios com passos
random.randint(start, stop)         # retorna um número inteiro aleatório
random.choice()                     # cria uma sequencia de números aleatórios
random.shuffle()                    # embaralha a sequência de números aleatórios
```

Porém, antes de utilizar o random é necessário importar ele como uma biblioteca, através do `import random`. Ele não está automaticamente disponível antes da importação.

***

## 7. Nível e Pontuação

### **Definindo uma pontuação para o usuário**

É possível definir um nível de dificuldade, o número de tentativas e calcular o resultado para o usuário obter uma pontuação ao final do jogo.

Contudo, se o resultado for negativo, pode-se utilizar a função `abs()`, que trata o número como absoluto. Então se a subtração retornar um número negativo, será mostrado apenas os pontos do usuário, sem sinal.

```py
pontos_perdidos = abs(numero_secreto - chute)

# O usuário tem 40 pontos e perde 60, o resultado seria -20
# Mas com a declaração de número absoluto, o resultado é 20
```

### **Funções built-in**

As funções `built-in` fazem parte da biblioteca padrão do Python e podem ser chamadas a qualquer momento, em todos os lugares. A [documentação](https://docs.python.org/3/library/functions.html) possui uma lista dessas funções. Segue alguns exemplos já visto nas aulas:

```py
abs()
float()
format()
input()
int()
print()
range()
round()
str()
sum()
```

A versão 3 do Python sempre retorna um número inteiro (tipo `int`) ao utilizar a função `round()` para arredondar um número decimal. No entanto, quando um valor é igualmente próximo de dois números, eles são arredondados para o número **PAR** mais próximo, veja:

```py
round(3.5)  # resultado 4
round(4.5)  # resultado 4 também

round(2.5)  # resultado 2
```

### **Divisão de float e integer**

O operador de divisão sempre retorna um valor decimal `float`, mesmo quando não for necessário. Contudo, existe outro operador semelhante que retorna uma divisão como `int` sem arredondar.

```py
3 / 2   # resultado 1.5
2 / 2   # resultado 1.0

3 // 2  # resultado 1
```

***

## 8. Organizando ainda melhor o nosso código

### **Criando funções para os nossos jogos**

É possível criar funções, atribuindo um código a ela e depois importando em outro arquivo. Para isso, escreve-se `def nome_da_funcao():` e todo o código precisa ser indentado para depois ser importado `import nome_da_funcao` e executado `nome_da_funcao()` no outro arquivo. Além disso, uma função também pode receber parâmetros e retornar algum valor:

```py
def soma(a, b):
  return a + b

s = soma(3, 4)
```

### **Diferenciando um arquivo executado de um importado**

Ao definir uma função e importar ela num arquivo diferente do original, ao rodar o original não temos o resultado esperado, pois agora ele só executa dentro da função criada. Para resolver isso, cria-se uma condição no arquivo original, com uma variável, para que ele execute o código sem chamar a função.

```py
# adivinhacao.py
import random
def jogar():
    # código omitido
if (__name__ == "__main__"):
    jogar()

# forca.py
def jogar():
    # código omitido
if (__name__ == "__main__"):
    jogar()

# jogos.py
if (__name__ == "__main__"):
    escolhe_jogo()
```

No exemplo acima, temos 2 jogos que são importados em um terceiro arquivo, para que se escolha qual jogar. Contudo, sem a condição declarada no `if` o código só é executado quando importado, com a condição declarada, ambos os arquivos podem executar os códigos com ou sem import.

***

## 9. Comparando Python com C

### **Python vs C**

Analisando o código e percebendo as diferenças entre as linguagens:

1. A primeira diferença que vemos é que no **C** precisamos importar mais bibliotecas, isso porque algumas funções no C não são built-in, como a de imprimir `(printf)` e a de capturar entrada do usuário `(scanf)`, por isso para utilizá-las é necessário importar algumas bibliotecas.
   
2. Outra diferença é que no **C** somos obrigados a definir a função `main`, que é considerada o início de qualquer programa, sem ela nada vai funcionar. Ao contrário do **Python**, já que nós só criamos a função `jogar()` quando precisamos importar o arquivo em outro, mas antes nós conseguíamos executar diretamente o jogo sem problemas.

3. No capítulo 1 falamos sobre tipagem de variáveis, e o **C** é uma linguagem que possui a `tipagem estática`, ou seja, quando declaramos uma variável, precisamos dizer qual será o tipo dela e esse tipo nunca mudará. O **Python**, como já sabemos, é uma linguagem que possui a `tipagem dinâmica`, já que o tipo da variável varia de acordo com o valor que ela recebe, por isso que em Python não podemos declarar variáveis vazias, só definindo o seu nome, porque se não atribuirmos um valor a uma variável, o Python não saberá o seu tipo.

4. O resto do código é bem parecido, com algumas diferenças de sintaxe e nomenclatura, como por exemplo a sintaxe dos blocos, para definir um bloco no **C** devemos colocá-lo entre `chaves` e a `indentação` não é obrigatório, apesar de todos os desenvolvedores utilizarem por conta da formatação do código, já no **Python** só precisamos colocar os `dois pontos` e `indentar` o código do bloco; o **C** também te obriga a colocar `ponto e vírgula` ao final das instruções.

5. O ambiente do **C** exige que primeiramente devemos passar o código fonte (o arquivo .c) para um `compilador`. O compilador (**gcc**) lê o código fonte e faz uma análise da sintaxe, se esquecemos algum ponto e vírgula, ou de tipar alguma variável, etc. E feita essa análise, o compilador cria um `outro arquivo`, e é esse arquivo que podemos executar.

```c
gcc adivinhacao.c o adivinhacao

ou

gcc -std=c99 adivinhacao.c -o adivinhacao

/*
  Esse comando compila o arquivo adivinhacao.c
  Se tudo estiver correto, criará o arquivo executável adivinhacao.
  Agora é só executar o arquivo gerado.
*/

./adivinhacao
```

6. Em **Python**, conseguimos executar um arquivo em `qualquer sistema operacional`, basta ter o Python 3 instalado. Já o arquivo executável do **C**, gerado pelo compilador, `não é executável em um sistema operacional diferente`. É preciso compilar novamente o código fonte no sistema operacional desejado, para ter um executável funcional. Logo, o Python tem uma portabilidade maior que o C.

7. Podemos executar o arquivo `jogos.py` e reparar na pasta que é criada dentro do diretório, a `pycache`. Se formos ver o que tem dentro da sua pasta, vemos que há dois arquivos referentes aos módulos importados no jogos.py, ou seja, um arquivo referente à `adivinhacao` e outro à `forca`.
   
8. O que o Python faz ao vivo é ler os módulos importados e os `compila para bytecode`. Esse código foi criado ao mesmo tempo em que executamos o arquivo jogos.py. Apesar do Python ter um `ambiente de interpretação`, ele compila os módulos importados para melhorar o desempenho, a execução do ambiente, mesmo que não tenha esse processo de compilação explícito.

⬆️ [Voltar ao topo](#começando-com-a-linguagem-python) ⬆️