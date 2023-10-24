from deque.DequeSequencialNumPy import Deque, DequeException
#from deque.DequeEncadeado import Deque, DequeException

d = Deque(5)
try:
    print(d)
    d.addFront(10)
    print(d)
    d.addFront(20)
    print(d)
    d.addRear(30)
    print(d)
    d.addRear(40)
    print(d)
    d.addFront(50)
    print(d)

    for i in range(len(d)):
        print(d.removeRear())
    print(d)
    d.addFront(10)
    print(d)
except DequeException as de:
    print(de)
