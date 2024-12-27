from lista_encadeada.ListaEncadeadaOrdenada import Lista, ListaError

lst = Lista()
try:
    print('TESTE 1: Lista Vazia:', lst.estaVazia())
    print('TESTE 2: Inserindo elementos na lista:')
    print(len(lst))
    lst.inserir(50)
    print(lst)
    lst.modificar(1, 99)
    print(lst)
    lst.inserir(25)
    print(lst)
    lst.inserir(60)
    print(lst)
    lst.inserir(45)
    print(lst)
    lst.inserir(53)
    print(lst)
    lst.inserir(57)
    lst.inserir(25)
    lst.inserir(45)
    print(lst)

    print('\nTESTE 3: iterando os elementos da lista:')
    for carga in lst:
        print(carga,end=' ')
    print() 

    # só funciona o for abaixo se estiver implementado o __reverse__()
    print('\nTESTE 4: Testando o __reverse__():')
    for e in reversed(lst):
        print(f'{e}', end=' ')
    print()

    print('\nTESTE 5: Testando o método remove_duplicatas():')
    lst.remove_duplicatas()
    print(lst)

    print('\nTESTE 6: Testando o método modificar():')
    lst.modificar(2,30)    
    print(lst)
    input('Pressione qualquer tecla para continuar...')


    # print(lst.get(-8))
    #print(lst.get(10))
    #print(lst.get('a'))
    print('Elemento(3):',lst.get(3))
    print('Busca(57)  :',lst.busca(57))

    # Tentando realizar uma modificação inválida
    # lst.modificar(1, 99)


    carga = lst.remover(3)
    print('Remover(3):', carga)
    print(lst)
    carga = lst.remover(5)
    print('Remover(5):', carga)
    print(lst)
    carga = lst.remover(1)
    print('Remover(1):', carga)
    print(lst)

    # Tentando realizar uma remoção inválida
    #valor = lst.remover(15)
    print('Testando o operador in:')
    print('in',45 in lst)

    print('testando o __getitem__():')
    print(lst[2])

    print('Testando o __delitem__():')
    del lst[2]
    print(lst)
    
    print('Testando o __setitem__():')
    lst[2] = 15
    print(lst)



    #valor = lst.remover(15)
 

except ListaError as le:
    print(le)
except Exception as e:
    print('Nossos engenheiros vao analisar esse problema')
    print(e.__class__.__name__)
    print(e)
