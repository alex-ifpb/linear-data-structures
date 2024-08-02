class ListaError(Exception):
    """Classe de exceção lançada quando uma violação de ordem genérica
       da lista é identificada.
    """

    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)



class Node:
    '''
    Classe de objetos para criação de um nó dinâmico na memória
    '''
    def __init__(self,data):
        self.__data = data
        self.__next = None
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, newData):
        self.__data = newData

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, newNext):
        self.__next = newNext

    def hasNext(self):
        return self.__next != None
    
    def __str__(self):
        return str(self.__data)

   
	    
class Lista:
    '''
    Classe de objetos para uma lista simplesmente encadeada
    '''
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self)->bool:
        '''
        Verifica se a lista está vazia
        Retorno:
            True se a lista estiver vazia
            False caso contrário
        '''
        return self.__tamanho == 0 

    def __len__(self)->int:
        '''
        Retorna o número de elementos da lista
        '''
        return self.__tamanho

    def elemento(self, posicao:int)->any:
        '''
        Retorna o conteúdo armazenado em uma determinada posição da lista
        Parâmetros:
            posicao(int): um número inteiro positivo
        Retorno:
            o elemento armazenado na posição indicada
        Raises:
            ListaError: se a posição for inválida ou a lista estiver vazia
        '''
        try:
            assert not self.estaVazia(), 'Lista vazia'
            assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1
            while( cursor != None  and contador < posicao):
                cursor = cursor.next
                contador += 1

            return cursor.data

        except AssertionError as ae:
            raise ListaError(ae)

    def modificar(self, posicao:int, carga: any):
        '''
        Modifica a carga de um elemento especificado pela posição
        indicada como parâmetro.
        Parâmetros:
          posicao(int): a posição do elemento desejado
          carga(any): a nova carga do elemento
        Raises:
            ListaError: se a posição for inválida ou a lista estiver vazia
        ''' 
        try:
            assert posicao > 0, f'A posicao não pode ser 0 (zero) ou um número negativo'
            assert posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'
            assert not self.estaVazia(), 'Lista vazia'

            cursor = self.__head
            contador = 1
            while( cursor != None and contador < posicao ):
                cursor = cursor.next
                contador += 1

            cursor.data = carga
        except TypeError:
            raise ListaError(f'A posição deve ser um número do tipo inteiro')            
        except AssertionError as ae:
            raise ListaError(ae.__str__())
   
    
    def busca(self, chave:any)->int:
        '''
        Busca um elemento na lista a partir de uma chave fornecida 
        como argumento.
        Parâmetros:
            chave(any): a chave de busca 
        Retorno:
            a posição do elemento na lista
        Raises:
            ListaError: se a chave não for encontrada ou a lista estiver vazia
        '''        
        if (self.estaVazia()):
            raise ListaError(f'Lista vazia')

        cursor = self.__head
        contador = 1

        while( cursor != None ):
            if( cursor.data == chave):
                return contador
            cursor = cursor.next
            contador += 1
            
        raise ListaError(f'A chave {chave} não está armazenado na lista')

    def inserir(self, posicao:int, carga:any ):
        '''
        Insere um elemento em uma determinada posição da lista
        Parâmetros:
            posicao(int): a posição onde a nova chave será inserida
            carga(any): a chave (carga) a ser inserida
        Raises:
            ListaError: se a posição for inválida
        '''        
        try:
            assert posicao > 0 and posicao <= len(self)+1, f'Posicao invalida. Lista contém {self.__tamanho} elementos' 

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                if ( posicao != 1):
                    raise ListaError(f'A lista esta vazia. A posicao correta para insercao é 1.')

                self.__head = Node(carga)
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if ( posicao == 1):
                novo = Node(carga)
                novo.next = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while ( contador < posicao-1):
                cursor = cursor.next
                contador += 1

            novo = Node(carga)
            novo.next = cursor.next
            cursor.next = novo
            self.__tamanho += 1

        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaError(f'A posicao não pode ser um número negativo ou 0 (zero)')

    def append(self, carga:any):
        '''
        Insere um novo nó no final da lista, com a carga fornecida.
        Parâmetros:
            carga (any): a carga do nó
        '''
        self.inserir(len(self)+1, carga)

    def remover(self, posicao:int)->any:
        '''
        Remove um elemento da lista a partir de uma posição fornecida
        como argumento.
        Parâmetros:
            posicao(int): a posição do elemento a ser removido
        Retorno:
            a carga do elemento removido
        Raises:
            ListaError: se a posição for inválida ou a lista estiver vazia
        '''
        try:
            if( self.estaVazia() ):
                raise ListaError(f'Não é possível remover de uma lista vazia')
            
            assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1

            while( contador <= posicao-1 ) :
                anterior = cursor
                cursor = cursor.next
                contador+=1

            data = cursor.data

            if( posicao == 1):
                self.__head = cursor.next
            else:
                anterior.next = cursor.next

            self.__tamanho -= 1
            return data
        
        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaError(f'A posicao não pode ser um número negativo')
      
              
    def __str__(self)->str:
        '''
        Retorna uma representação em string da lista
        '''
        str = 'Lista: [ '
        if self.estaVazia():
            str+= ']'
            return str

        cursor = self.__head

        while( cursor != None ):
            str += f'{cursor.data}, '
            cursor = cursor.next

        str = str[:-2] + " ]"
        return str

    def __iter__(self)->any:
        self.__ponteiro = self.__head
        return self
    
    def __next__(self)->any:
        if (self.__ponteiro == None):
            raise StopIteration
        else:
            carga = self.__ponteiro.data
            self.__ponteiro = self.__ponteiro.next
            return carga
        
    def __getitem__( self, posicao:int):
        return self.elemento(posicao)
    
    def __setitem__( self, posicao, novaCarga):
        self.modificar(posicao, novaCarga)

    # Método mágico para emular o comportamento do objeto à chamada da
    # função reversed()
    def __reversed__(self):
        for i in range(self.__tamanho,0,-1):
            yield self.elemento( i ) 




