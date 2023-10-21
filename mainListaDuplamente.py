from lista_encadeada.ListaDuplamenteEncadeada import Lista,ListaException
lst = Lista()
try:
    lst.inserir(1,25)
    lst.inserir(1,30)
    lst.inserir(1,40)
    lst.inserir(4,50)
    lst.inserir(2,60)
    lst.inserir(5,70)
    print(lst)
    print('Tamanho: ',len(lst))

    #print('Invertida:')
    #lst.imprimirReverso()

    #print()

    # só funciona o for abaixo se estiver implementado o __getitem__()
    print('Testando o __getitem__():')
    for i in range(1,len(lst)+1):
        print(lst[i], end=' ')
    print()

    # só funcionada com o __iterator__ e __next__
    print('Testando o __iterator__():')
    for e in lst:
        print(f'{e},',end=' ')
    print()

    # só funciona o for abaixo se estiver implementado o __reverse__()
    print('Testando o __reverse__():')
    for e in reversed(lst):
        print(f'{e},', end=' ')
    print()

    lst.remover(1)
    lst.remover(5)      
    lst.remover(3)
    print(lst)
    lst.modificar(1,160)
    lst.modificar(2,130)
    lst.modificar(3,170)
    #lst.modificar(4,180)
    print(lst)
    while(not lst.estaVazia()):
        print(lst.remover(1))
    print(lst)

except ListaException as le:
    print(le)  
except Exception as e:
    print('Classe: ', e.__class__.__name__)
    print('Mensagem de Erro:', e)
    print('Nossos engenheiros vao analisar esse problema')
