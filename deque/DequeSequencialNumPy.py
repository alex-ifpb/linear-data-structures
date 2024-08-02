import numpy as np

class DequeError(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos
       do Deque é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)

class Deque:
    """
       Classe que implementa a estrutura de dados "Deque".
       Qualquer tipo de dado pode ser armazenado.
       Nesta implementação, a parte traseira do Deque está localizada
       na extremindade direita do array, e a frente na extremidade esquerda

       Foi aplicada a técnica circular tanto para a parte traseira 
       quanto para a frente do deque

     Atributos:
        item (np.ndarray): array para armazenamento dos elementos do Deque
        rear (int): um número inteiro que representa o índice do último
                   elemento da extremidade traseira
        front (int): um número inteiro que representa o índice do primeiro
                    elemento da extremidade frontal
        size (int): um número inteiro que representa a quantidade de 
                   elementos
    """
    def __init__(self, max_size:int = 10):
        self.__items = np.full(max_size,None)
        self.__reset()
        self.__size = 0
    
    def __reset(self):
        '''
        Método privado que reinicia os índices front e rear
        '''
        self.__rear  = 0
        self.__front = 0
    
    def isEmpty(self):
        '''
        check if the deque is empty
        Returns:
            boolean: True if the deque is empty, False otherwise
        '''
        return self.__size == 0
    
    def isFull(self):
        '''
        check if the deque is full
        Returns:
            boolean: True if the deque is full, False otherwise
        '''
        return self.__size == len(self.__items)

    def __len__(self):
        '''
        return the number of elements inside the deque
        Returns:
            int: the number of elements in the deque
        '''
        return self.__size

    def addRear(self, value:any):
        '''
        add an element to the rear of the deque
        Args:
            value (any): the value to be added to the rear of the deque
        Raises:
            DequeError: exception raised when the deque is full
        '''
        if self.isFull():
            raise DequeError("O Deque está cheio")
        if self.isEmpty():
            self.__reset()
        else:
            self.__rear = (self.__rear + 1) % len(self.__items)
        self.__items[self.__rear] = value
        self.__size += 1
    
    def addFront(self, value:any):
        '''
        add an element to the front of the deque
        Args:
            value (any): the value to be added to the front of the deque
        Raises:
            DequeError: exception raised when the deque is full
        '''
        if self.isFull():
            raise DequeError("O Deque está cheio")
        if self.isEmpty():
            self.__reset()
        else:
            self.__front = (self.__front - 1) % len(self.__items)
        self.__items[self.__front] = value
        self.__size += 1

    def removeRear(self):
        '''
        remove an element from the rear of the deque
        Returns:
            any: the element removed from the rear of the deque
        Raises:
            DequeError: exception raised when the deque is empty
        '''
        if self.isEmpty():
            raise DequeError("O Deque está vazio")
        value = self.__items[self.__rear]
        self.__rear = (self.__rear - 1) % len(self.__items)
        self.__size -= 1
        return value
    
    def removeFront(self):
        '''
        remove an element from the front of the deque
        Returns:
            any: the element removed from the front of the deque
        Raises:
            DequeError: exception raised when the deque is empty
        '''
        if self.isEmpty():
            raise DequeError("O Deque está vazio")
        value = self.__items[self.__front]
        self.__front = (self.__front + 1) % len(self.__items)
        self.__size -= 1
        return value
    
    def peekRear(self):
        '''
        return the element at the rear of the deque without removing it
        Returns:
            any: the element at the rear of the deque
        Raises:
            DequeError: exception raised when the deque is empty
        '''
        if self.isEmpty():
            raise DequeError("O Deque está vazio")
        return self.__items[self.__rear]
    
    def peekFront(self):
        '''
        return the element at the front of the deque without removing it
        Returns:
            any: the element at the front of the deque
        Raises:
            DequeError: exception raised when the deque is empty
        '''
        if self.isEmpty():
            raise DequeError("O Deque está vazio")
        return self.__items[self.__front]
        
    def __str__(self):
        '''
        return a string representation of the deque
        Returns:
            str: a string representation of the deque
        '''
        s = 'front->['
        next = self.__front
        for i in range(self.__size):
            s += str(self.__items[next]) + ','
            next = (next + 1) % len(self.__items)  
        s = s.rstrip(',') # remove a última vírgula
        s += ']<-rear\n'
        s += f'front {self.__front} | rear {self.__rear} | size {self.__size}   '
        return s
