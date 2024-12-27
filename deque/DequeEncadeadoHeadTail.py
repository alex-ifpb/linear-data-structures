class DequeError(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos
       do Deque é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)

class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self)->any:
        return self.__carga
    
    @property
    def prox(self)->'No':
        return self.__prox

    @carga.setter
    def carga(self, novaCarga:any):
        self.__carga = novaCarga

    @prox.setter
    def prox(self, novoProx:'No'):
        self.__prox = novoProx
    
    def __str__(self):
        return f'{self.__carga}'

       
class Deque:
    """Classe que implementa a estrutura de dados "Deque"
       utilizando a técnica de encadeamento com ponteiros head and tail (cabeca e cauda)
       A classe permite que qualquer tipo de dado seja armazenada no Deque.

     Attributes:
        inicio (No): apontador para o primeiro nó do Deque
        fim (No): apontador para o último nó do Deque
        tamanho (int): tamanho do Deque
    """
    def __init__(self):
        """ Construtor padrão da classe Deque sem argumentos. Ao instanciar
            um objeto do tipo Deque, esta iniciará vazia. 
        """
        self.__front = None
        self.__rear = None
        self.__size = 0


    def estaVazia(self)->bool:
        """ Método que verifica se o Deque está vazio.

        Returns:
            boolean: True se o Deque estiver vazio, False caso contrário

        Examples:
            f = Deque()
            ...   # considere que temos internamente no Deque frente->[10,20,30,40]<-final
            if(f.estaVazia()): #
               # instrucoes
        """
        return self.__size == 0

    def __len__(self)->int:
        """ Método que consulta a quantidade de elementos existentes no Deque

        Returns:
            int: um número inteiro que determina o número de elementos existentes no Deque

        Examples:
            f = Deque()
            ...   # considere que temos internamente o Deque frente->[10,20,30,40]
            print (len(f)) # exibe 4
        """       
        return self.__size
    
    def add_cauda(self, carga:any):
        '''
        Adiciona um elemento na extremidade traseira do deque
        Args:
            carga (any): o valor a ser adicionado na extremidade traseira do deque
        '''
        novo = No(carga)
        if self.estaVazia(): # faz cauda e frente apontarem para o mesmo lugar
            self.__front = self.__rear = novo
        else:
            self.__rear.prox = novo
            self.__rear = novo
        self.__size += 1

    def add_frente(self, carga:any):
        '''
        Adiciona um elemento na extremidade frontal do deque
        Args:
            carga (any): o valor a ser adicionado na extremidade frontal do deque
        '''
        novo = No(carga)
        if self.estaVazia(): # faz cauda e frente apontarem para o mesmo lugar
            self.__front = self.__rear = novo
        else:
            novo.prox = self.__front
            self.__front = novo
        self.__size += 1

    def remove_cauda(self)->any:
        '''
        Remove um elemento da extremidade traseira do deque
        Returns:
            any: a carga da extremidade traseira do deque
        Raises:
            DequeError: exceção lançada quando o deque está vazio
        '''
        if self.estaVazia():
            raise DequeError("remove_cauda(): O Deque está vazio")
        carga = self.__rear.carga

        if self.__rear == self.__front:
            self.__front = self.__rear = None
        else:
            cursor = self.__front
            while(cursor.prox != self.__rear):
                cursor = cursor.prox
            cursor.prox = None
            self.__rear = cursor
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
        carga = self.__front.carga

        if self.__rear == self.__front:
            self.__front = self.__rear = None
        else:
            self.__front = self.__front.prox
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
        return self.__rear.carga
    
    def frente(self)->any:
        """ Método que recupera o conteudo armazenado no elemento da frente da Deque,
            sem removê-lo.

        Returns:
            any: o conteudo armazenado na frente da Deque (tipo primitivo ou objeto).

        Raises:
            DequeError: Exceção lançada quando a Deque não possui elementos
        Examples:
            f = Deque()
            ...   # considere que temos internamente o Deque frente->[10,20,30,40]
            print (f.frente()) # exibe 10
        """
        if self.estaVazia():
            raise DequeError(f'Deque Vazio. Não há elemento a recuperar.')
        return self.__front.carga

    def busca(self, chave:any)->int:
        """ Método que recupera a posicao ordenada, dentro do Deque, em que se
            encontra um valor chave passado como argumento. No caso de haver
            mais de uma ocorrência do valor, a primeira ocorrência será 
            retornada

        Args:
            key(any): um item de dado que deseja procurar no Deque
        
        Returns:
            int: um número inteiro representando a posição, na Deque, em que foi
                 encontrada a "chave" de busca.

        Raises:
            KeyError: Exceção lançada quando o argumento "key"
                  não está presente no Deque.

        Examples:
            f = Deque()
            ...   # considere que temos internamente o Deque  frente->[10,20,30,40]<-cauda
            print (f.busca(40)) # exibe 4
        """
        cursor = self.__front
        contador = 1

        while( cursor != None):
            if cursor.carga == chave:
                return contador           
            cursor = cursor.prox
            contador += 1

        raise KeyError(f'Chave {chave} inexistente no Deque')
  
    def get(self, posicao:int)->any:
        """ Método que recupera o conteudo armazenado em uma determinada posição
            do Deque, sem removê-lo.

        Args:
            posicao(int): um número inteiro que determina a posição do elemento
                          que se deseja recuperar. A posição 1 refere-se ao 
                          elemento da frente do Deque.

        Returns:
            any: o conteudo correspondente à posição indicada no Deque.

        Raises:
            DequeError: Exceção lançada quando a posição não é válida para o Deque atual
        Examples:
            f = Deque()
            ...   # considere que temos internamente o Deque  frente->[10,20,30,40]<-cauda
            print (f.get(3)) # retorna 30
        """
        try:
            if self.estaVazia():
                raise DequeError('Deque Vazio.')
            assert posicao > 0 and posicao <= self.__size
            cursor = self.__front
            contador = 1
            while(cursor != None and contador < posicao ):
                contador += 1
                cursor = cursor.prox

            return cursor.carga
        except AssertionError:
            raise DequeError(f'Posicao invalida. Forneça um valor entre 1 e {self.__size}.')
        except:
            raise

      
    def __str__(self):
        """ Método que retorna uma string com a ordem dos elementos
            existentes no Deque.
        """
        s = 'frente->[ '
        cursor = self.__front
        while(cursor != None):
            s += f'{cursor.carga}, ' 
            cursor = cursor.prox
        return s[:-2] + " ]<-cauda" if not self.estaVazia() else  s + ' ]<-cauda'

    def __iter__(self)->any:
        self.__cursor = self.__front
        return self
    
    def __next__(self)->any:
        if (self.__cursor is None):
            raise StopIteration
        else:
            carga = self.__cursor.carga
            self.__cursor = self.__cursor.prox
            return carga

    def __contains__(self, key:any)->bool:
        '''
        Método que verifica se uma chave está presente no Deque.
        Acionado em situações de uso do operador "in": "if chave in Deque".
        Argumentos:
            key(Any): chave a ser buscada.
        Retorna:
            bool: True se a chave estiver no Deque e False caso contrário.
        '''
        try:
            self.busca(key)
            return True
        except KeyError:
            return False

    def __getitem__( self, posicao:int):
        return self.get(posicao)    
       

