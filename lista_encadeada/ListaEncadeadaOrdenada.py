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
    Classe de objetos para armazenamento e gerenciamento de elementos
    de uma lista simplesmente encadeada ordenada.
    Nesse tipo de lista, os elementos são inseridos de forma ordenada
    de acordo com a chave de ordenação.
    '''
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self)->bool:
        '''
        Verifica se a lista está vazia
        Retorno:
          True se a lista estiver vazia e False caso contrário
        '''
        return self.__tamanho == 0 

    def get(self, posicao:int)->any:
        '''
        Retorna a carga armazenada em uma determinada posição da lista
        Parâmetros:
          posicao(int): a posição do elemento desejado
        Retorno:
          A carga armazenada na posição especificada
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
        indicada como parâmetro. A chave da carga tem que manter a lista ordenada.
        Parâmetros:
          posicao(int): a posição do elemento desejado
          carga(any): a nova carga do elemento
        Raises:
            ListaError: se a posição for inválida ou se a lista estiver vazia
            ou se a chave da carga não mantiver a lista ordenada
        ''' 
        try:
            assert not self.estaVazia(), 'Lista vazia'
            assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1

            while( contador <= posicao-1 ) :
                anterior = cursor
                cursor = cursor.next
                contador+=1
                
            if cursor.next == None:
                if contador == 1: # se a posicao for a primeira
                    pass # não faz nada, vai para a linha de atribuição de carga
                elif anterior.data > carga:
                    raise ListaError(f'A chave {carga} na posição {posicao} não mantém a lista ordenada')
                # se passar daqui, a carga é maior que a anterior e está no final da lista
            elif posicao == 1: # se a posicao for a primeira em uma lista com mais de um elemento
                if carga > cursor.next.data:
                    raise ListaError(f'A chave {carga} na posição {posicao} não mantém a lista ordenada')
            elif anterior.data > carga or carga > cursor.next.data:
                raise ListaError(f'A chave {carga} na posicao {posicao} não mantém a lista ordenada')

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
            KeyError: se a chave não for encontrada ou a lista estiver vazia
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
            
        raise KeyError(f'A chave {chave} não está armazenado na lista')

    def inserir(self, carga:any ):
        '''
        Insere um elemento na lista de forma ordenada.
        Parâmetros:
            carga(any): a carga do elemento a ser inserido
        '''
        # CONDICAO 1: insercao se a lista estiver vazia
        novoNo = Node(carga)
        if (self.estaVazia()):
            self.__head = novoNo
        elif (carga < self.__head.data):
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            novoNo.next = self.__head
            self.__head = novoNo
        else:
            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            while (cursor.next is not None and cursor.next.data < carga):
                cursor = cursor.next

            novoNo.next = cursor.next
            cursor.next = novoNo
        self.__tamanho += 1

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
      
    def remove_duplicatas(self):
        '''
        Remove duplicatas da lista
        '''
        if self.estaVazia():
            return

        cursor = self.__head
        while cursor.next != None:
            if cursor.data == cursor.next.data:
                cursor.next = cursor.next.next
                self.__tamanho -= 1
            else:
                cursor = cursor.next

    def __str__(self):
        '''
        Retorna uma representação em string da lista
        '''
        str = '[ '
        if self.estaVazia():
            str+= ']'
            return str

        cursor = self.__head

        while( cursor != None ):
            str += f'{cursor.data}, '
            cursor = cursor.next

        str = str.rstrip(', ') + " ]"
        return str

    def __len__(self)->int:
        '''
        Retorna o número de elementos armazenados na lista
        '''
        return self.__tamanho

    # Métodos para implementação do protocolo "Iterator"
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
        return self.get(posicao)
    
    def __setitem__( self, posicao, novaCarga):
        self.modificar(posicao, novaCarga)
    
    def __delitem__(self, posicao:int):
        '''
        Método mágico para permitir a remoção de um elemento da lista
        utilizando a notação de colchetes.
        '''
        self.remover(posicao)

    # Método mágico para emular o comportamento do objeto à chamada da
    # função reversed()
    def __reversed__(self):
        for i in range(self.__tamanho,0,-1):
            yield self.get( i ) 



