from deque.DequeSequencialNumPy import Deque, DequeError
# from deque.DequeEncadeadoHeadTail import Deque, DequeError

d = Deque()
try:
    print(d)
    d.add_frente(10)
    print(d)
    d.add_frente(20)
    print(d)
    d.add_frente(30)
    print(d)
    d.add_cauda(40)
    print(d)
    d.add_frente(50)
    print(d)

    print('busca()', d.busca(40))
    print('get()', d.get(3))
    print('in', 10 in d) # __contains__()
    print('len()', len(d))

    print('iterador:')
    for carga in d:
        print(carga, end=' ')

    print('\nTestando o __getitem__():')
    print(d[2])

    print('removendo das extremidades:')
    for i in range(len(d)):
        print(d.remove_frente())
        print(d.remove_cauda())
    print(d)
    d.add_frente(10)
    print(d)
except DequeError as de:
    print(de)
