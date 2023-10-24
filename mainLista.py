from lista_sequencial.ListaSequencialNumPy import Lista, ListaException
#from lista_encadeada.ListaSimplesmenteEncadeada import Lista, ListaException
#from lista_encadeada.ListaEncadeadaCircular import Lista, ListaException   

lst = Lista()
try:
    print('Vazia:', lst.estaVazia())
    #print('Cheia:', lst.estaCheia())
    print(len(lst))
    lst.inserir(1,50)
    print(lst)
    lst.inserir(2,55)
    print(lst)
    lst.inserir(3,60)
    print(lst)
    lst.inserir(1,45)
    print(lst)
    lst.inserir(3, 53)
    print(lst)
    lst.inserir(5,57)
    print(lst)

    # print(lst.elemento(-8))
    #print(lst.elemento(10))
    #print(lst.elemento('a'))
    print('Elemento(3):',lst.elemento(3))
    print('Busca(45):',lst.busca(45))
    lst.modificar(3, 99)
    print('Modificar(3,99):', lst)
    #lst.busca(40)


    carga = lst.remover(3)
    print('Remover(3):', carga)
    print(lst)
    carga = lst.remover(5)
    print('Remover(5)carga:', carga)
    print(lst)
    carga = lst.remover(1)
    print('Remover(1):', carga)
    print(lst)

    #valor = lst.remover(15)

    input('Pressione qualquer tecla para finalizar...')

except ListaException as le:
    print(le)
except Exception as e:
    print('Nossos engenheiros vao analisar esse problema')
    print(e.__class__.__name__)
    print(e)
