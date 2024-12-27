# from fila_encadeada.FilaEncadeadaNoCabeca import Fila, FilaError
# from fila_encadeada.FilaEncadeadaHeadAndTail import Fila, FilaError
from fila_sequencial.FilaSequencialCircularNumPy import Fila, FilaError

f = Fila()

try:
    print(f)
    for i in range(1,4):
        f.enfileirar(i*10)
    # f.printArray() # só para sequencial circular
    
    print('Tamanho: ', len(f))
    print(f)
    print('Elemento da frente: ', f.frente())
  
    #print(f.elemento(-8))
    print('Elemento 2: ', f.get(2))
    #print(f.elemento('a'))

    print('Busca(20):', f.busca(20))
    #print('Busca(80):', f.busca(80))

    print('desenfileirar():', f.desenfileirar())
    f.enfileirar(111)
    f.enfileirar(112)
    f.enfileirar(113)
 
    print('desenfileirar():', f.desenfileirar())
    print(f)

    print('Testando o __contains__():')
    print(30 in f)

    print('Testando o __iter__():')
    for carga in f: # da base em direção ao topo
        print(carga, end=' ')

    print('\nTestando o __getitem__():')
    print(f[4])


 
except FilaError as fe:
    print(fe)
except Exception as e:
    print('Classe: ', e.__class__.__name__, ' msg: ', e)
    print('Nossos engenheiros vao analisar esse problema')

