<h1 align="center">Estruturas de Dados Lineares Orientada a Objetos</h1>

Este repositório reúne diferentes implementações na Linguagem `Python` de Estruturas de Dados lineares (Lista, Pilha, Fila e Deque) utilizando as técnicas <b>sequencial</b> e <b>encadeada</b>. As estruturas de dados são estudadas, discutidas e implementadas nos cursos de Sistemas para Internet e Redes de Computadores do IFPB Campus João Pessoa.

Contribua com o aprimoramento das implementações informando situações em que o uso das estruturas apresentou alguma falha.

## Autor
Professor Alex Sandro da Cunha Rêgo<br>
Lattes: http://lattes.cnpq.br/1582109846489096<br>
Doutor em Ciência da Computação
Instituto Federal da Paraíba - Campus João Pessoa

## Pré-Requisitos
+  Conhecimentos básicos na sintaxe de programação na linguagem Python;
+  Entendimento da construção e uso de Classes e Objetos (Paradigma Orientado a Objetos)

## Características
As estruturas de dados presentes neste repositório estão codificadas de maneira que possam ser manuseadas com a notação de `[]`, assim como é feito com a manipulação de `list()` em Python. Porém, considera como `índice` valores de `1` até `n`. Os seguintes métodos especiais estão presentes nas classes, utilizando como exemplo um objeto chamado `minha_lista` (se aplica também para pilha, fila e deque):	

`__getitem__()`: permite definir como acessar elementos de uma classe personalizada usando a notação de colchetes `[]`. Exemplo:

print(minha_lista[3]) # acessa o terceiro elemento da lista 

`__setitem__()`: permite definir como modificar elementos de uma classe personalizada usando a notação de colchetes `[]`. Exemplo:

minha_lista[3] = value

`__delitem__()`: permite que a classe personalizada possa deletar elementos utilizando a palavra chave `del`. Exemplo:

del minha_lista[3] 

`__contains__()`: permite verificar se uma chave está contida em uma determinada coleção, usando o operador `in`. Neste caso, o operando usado em conjunto do operador `in` deve ser algo em que se deseja verificar se está na lista de elementos. Exemplo:
```
if key in minha_lista:
      pass
```
`__reversed__()`: método mágico usado para emular o comportamento do objeto à chamada da função `reversed()` de Python.

`__iter__()`: Método mágico que permite a iteração sobre os elementos da lista utilizando a estrutura `for` iterável. Exemplo:
```
for item in minha_lista:
      print(item)
```
Obs: `__getitem__()` e `__setitem__()` são usados apenas em atributos indexados tais como arrays, dicionários e lista. Para maiores informações, consultar a documentação de Python.

## Estruturas de Dados
| Nome | Descrição |
| ------ | ----------- |
| **Lista Encadeada** | Lista Simplesmente Encadeada, Lista Duplamente Encadeada, Lista Simplesmente Encadeada Circular, Lista Simplesmente Encadeada Ordenada |
| **Lista Sequencial** | Lista sequencial usando `list` como array, Lista sequencial usando array `NumPy` |
| **Pilha Encadeada** | Pilha simplesmente encadeada |
| **Pilha Sequencial**  | Pilha usando array `NumPy` |
| **Fila Encadeada** | Fila encadeada com uso da abordagem `head` and `tail` e com `nó cabeça` |
| **Fila Sequencial** | Fila sequencial circular usando array `NumPy` |
| **Deque** | Deque sequencial circular usando array `NumPy` e encadeado com uso da abordagem `head` and `tail`|

## Métodos

A tabela a seguir ilustra os métodos em comum nas diferentes implementações das estruturas lineares. Maiores detalhes sobre cada método
podem ser obtidos na documentação presente em cada código.

| Implementação       | Pilha | Lista       | Fila          | Deque |
| ------------------- |-------|-------------| ------------- | -------------- |
| estaVazia()         | sim   |  sim        |        sim         |   sim  |
| estaCheia()         | SEQ   |  SEQ        |        SEQ         |   SEQ  |
| get()               | sim   |  sim        |        sim         |    sim   |
| modificar()         | N/A   |  sim        |        N/A         |    N/A   |
| busca()             | sim   |  sim        |        sim         |    sim   |
| inserir()           | sim   |  sim        |        sim         |    sim   |
| append()            | N/A   |  sim        |        N/A         |    N/A   |
| add_frente()        | N/A   |  N/A        |        N/A         |    sim   |
| add_cauda()         | N/A   |  N/A        |        N/A         |    sim   |
| remover()           | sim   |  sim        |        sim         |    sim   |
| remove_frente()     | N/A   |  N/A        |        N/A         |    sim   |
| remove_cauda()      | N/A   |  N/A        |        N/A         |    sim   |
| remove_duplicatas() | N/A   |  Sim (*)    |        N/A         |    N/A   |
| topo()              | sim   |  N/A        |        N/A         |    N/A   |
| frente()            | N/A   |  N/A        |        sim         |    sim   |
| cauda()             | N/A   |  N/A        |        N/A         |    sim   |
| `__str__()`         | sim   |  sim        |        sim         |    sim   |
| `__len__()`         | sim   |  sim        |        sim         |    sim   |
| `__iter__()`        | sim   |  sim        |        sim         |    sim   |
| `__next__()`        | sim   |  sim        |        sim         |    sim   | 
| `__reversed__()`    | N/A   |  sim        |        N/A         |    N/A   |
| `__getitem__()`     | sim   |  sim        |        sim         |    sim   | 
| `__setitem__()`     | N/A   |  sim        |        N/A         |    N/A   |
| `__contains__()`    | sim   |  sim        |        sim         |    sim   |
| `__delitem__()`     | N/A   |  sim        |        N/A         |    N/A   |

N/A: Não se aplica<br> 
SEQ: Apenas para implementações sequenciais<br>
(*): Apenas para lista ordenada