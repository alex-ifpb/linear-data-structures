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
    
    def estaVazia(self):
        '''
        Verifica se o deque está vazio
        Returns:
            boolean: True se o deque estiver vazio, False caso contrário
        '''
        return self.__size == 0
    
    def estaCheia(self):
        '''
        Verifica se o deque está cheio
        Returns:
            boolean: True se o deque estiver cheio, False caso contrário
        '''
        return self.__size == len(self.__items)

    def __len__(self):
        '''
        Retorna o número de elementos no deque
        Returns:
            int: o número de elementos no deque
        '''
        return self.__size

    def add_cauda(self, carga:any):
        '''
        Adiciona um elemento na extremidade traseira do deque
        Args:
            carga (any): o valor a ser adicionado na extremidade traseira do deque
        Raises:
            DequeError: exceção lançada quando o deque está cheio
        '''
        if self.estaCheia():
            raise DequeError("add_cauda(): O Deque está cheio")  
        elif self.estaVazia(): # faz cauda e frente apontarem para o mesmo lugar
            self.__reset()
        else:
            self.__rear = (self.__rear + 1) % len(self.__items)
        self.__items[self.__rear] = carga
        self.__size += 1
    
    def add_frente(self, carga:any):
        '''
        Adiciona um elemento na extremidade frontal do deque
        Args:
            carga (any): o valor a ser adicionado na extremidade frontal do deque
        Raises:
            DequeError: exceção lançada quando o deque está cheio
        '''
        if self.estaCheia():
            raise DequeError("add_frente(): O Deque está cheio")
        elif self.estaVazia():
            self.__reset()
        elif self.__front == 0:
            self.__front = len(self.__items) - 1
        else:
            self.__front -= 1

        self.__items[self.__front] = carga
        self.__size += 1

    def remove_cauda(self)->any:
        '''
        Remove um elemento da extremidade traseira do deque
        Returns:
            any: o elemento removido da extremidade traseira do deque
        Raises:
            DequeError: exceção lançada quando o deque está vazio
        '''
        if self.estaVazia():
            raise DequeError("remove_cauda(): O Deque está vazio")
        carga = self.__items[self.__rear]
        if self.__rear == self.__front:
            self.__reset()
        elif self.__rear == 0:
            self.__rear = len(self.__items) - 1
        else:
            self.__rear -= 1
        self.__size -= 1
        return carga
    
    def remove_frente(self):
        '''
        Remove um elemento da extremidade frontal do deque
        Returns:
            any: o elemento removido da extremidade frontal do deque
        Raises:
            DequeError: exceção lançada quando o deque está vazio
        '''
        if self.estaVazia():
            raise DequeError("remove_frente(): O Deque está vazio")
        carga = self.__items[self.__front]
        self.__front = (self.__front + 1) % len(self.__items)
        self.__size -= 1
        return carga
    
    def cauda(self):
        '''
        Retorna o elemento da extremidade traseira do deque sem removê-lo
        Returns:
            any: o elemento da extremidade traseira do deque
        Raises:
            DequeError: exceção lançada quando o deque está vazio
        '''
        if self.estaVazia():
            raise DequeError("cauda(): O Deque está vazio")
        return self.__items[self.__rear]
    
    def frente(self):
        '''
        Retorna o elemento da extremidade frontal do deque sem removê-lo
        Returns:
            any: o elemento da extremidade frontal do deque
        Raises:
            DequeError: exceção lançada quando o deque está vazio
        '''
        if self.estaVazia():
            raise DequeError("frente(): O Deque está vazio")
        return self.__items[self.__front]

    def busca(self, key: any)->int:
        """ Método que recupera a posicao ordenada, dentro do deque, em que se
            encontra um valor chave passado como argumento. No caso de haver
            mais de uma ocorrência do valor, a primeira ocorrência será 
            retornada. O percurso é feito da frente para a cauda.

        Args:
            key: um item de dado que deseja procurar no deque
        
        Returns:
            int: um número inteiro representando a posição, no deque, em que foi
                 encontrada a "chave" de busca.

        Raises:
            KeyError: Exceção lançada quando o argumento "key"
                  não está presente na fila.

        Examples:
            d = Deque()
            ...   # considere que temos internamente a o deque  frente->[10,20,30,40]<-cauda
            print (d.busca(40)) # exibe 4
        """
        frente = self.__front
        for i in range(1,self.__size+1):
            if self.__items[frente] == key:
                return i
            frente = (frente + 1)% len(self.__items)
                
        raise KeyError(f'A chave {key} não foi encontrada')

    def get(self, posicao:int)->any:
        """ Recupera a carga armazenada em uma determinada posição
            no deque, sem removê-lo. O sentido de busca é da frente para a cauda.
        Args:
            posicao(int): um número inteiro entre 1 e n, onde n é o número
                          de elementos no deque.

        Returns:
            any: a carga armazenada na posição indicada.

        Raises:
            DequeError: Exceção lançada quando a posição não é válida 
        Examples:
            d = Deque()
            ...   # considere que temos internamente o deque  frente->[10,20,30,40]<-cauda
            print (f.get(3)) # retorna 30
        """
        try:
            assert posicao > 0 and posicao <= self.__size
            frente = self.__front
            for i in range(posicao-1):
                frente = (frente + 1) % len(self.__items)

            return self.__items[frente]
        except AssertionError:
            raise DequeError(f'get(): Posicao inválida para o deque atual com {self.__size} elementos')

        
    def __str__(self):
        '''
        Retorna uma representação do deque em forma de string
        Returns:
            str: uma representação do deque em forma de string
        '''
        s = 'frente->['
        next = self.__front
        for i in range(self.__size):
            s += str(self.__items[next]) + ','
            next = (next + 1) % len(self.__items)  
        s = s.rstrip(',') # remove a última vírgula
        s += ']<-cauda\n'
        # s += f'front {self.__front} | rear {self.__rear} | size {self.__size}   '
        return s

    def __iter__(self)->any:
        self.__index = 1
        self.__cursor = self.__front
        return self
    
    def __next__(self)->any:
        if (self.__index > self.__size):
            raise StopIteration
        else:
            carga = self.__items[self.__cursor]
            self.__cursor = (self.__cursor + 1) % len(self.__items)
            self.__index += 1
            return carga

    def __contains__(self, key:any)->bool:
        '''
        Método que verifica se uma chave está presente no deque.
        Acionado em situações de uso do operador "in": "if chave in deque".
        Argumentos:
            key(Any): chave do elemento a ser buscado.
        Retorna:
            bool: True se a chave estiver no deque e False caso contrário.
        '''
        try:
            self.busca(key)
            return True
        except KeyError:
            return False

    def __getitem__( self, posicao:int):
        return self.get(posicao)    
