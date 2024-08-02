class Node:
    def __init__(self, carga):
        self.__carga = carga
        self.__next = None
        self.__ponteiro = None

    @property
    def next(self):
        return self.__next
       
    @next.setter
    def next(self, novoProx):
        self.__next = novoProx

    @property
    def carga(self):
        return self.__carga
        
    @carga.setter
    def carga(self, novoConteudo):
        self.__carga = novoConteudo

    def hasNext(self):
        return self.__next != None

    def __str__(self):
        return str(self.__carga)


class ListaError(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class Lista:
    # constructor that initializes an empty round linked list
    def __init__(self):
        self.__head = None
        self.__tamanho = 0
        self.__ponteiro = None

    def estaVazia(self)->bool:
        '''
        Verifica se a lista está vazia
        Retorno:
            True se a lista estiver vazia
            False caso contrário'''
        return self.__tamanho == 0

    def elemento(self, posicao:int)->any:
        '''
        Retorna a carga armazenada no nó correspondente à posicao indicada.
        Parâmetros:
            posicao (int): posição do nó cuja carga se deseja obter
        Retorno:
            a carga do nó correspondente à posicao indicada
        Raises:
            ListaError: caso a posicao indicada seja inválida ou a lista esteja vazia
        '''
        try:
            assert not self.estaVazia(), 'Lista vazia'
            assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1
            while( contador < posicao ):
                cursor = cursor.next
                contador += 1

            return cursor.carga            

        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListaError(ae)


    def modificar(self, posicao:int, carga: any):
        '''
        Modifica a carga do nó correspondente à posicao indicada.
        Parâmetros:
            posicao (int): posição do nó cuja carga se deseja modificar
            carga (any): a nova carga do nó
        Raises:
            ListaError: caso a posicao indicada seja inválida ou a lista esteja vazia
        '''
        try:
            assert not self.estaVazia(), 'Lista vazia'
            assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1
            while( contador < posicao ):
                cursor = cursor.next
                contador += 1

            cursor.carga = carga
        except TypeError:
            raise ListaError(f'A posição deve ser um número do tipo inteiro')            
        except AssertionError as ae:
            raise ListaError(ae.__str__())

    def busca(self, key:any)->int:
        '''
        Verifica a existência da chave de busca na lista e retorna a posição do nó que a contém.
        Parâmetros:
            key (any): a chave de busca
        Retorno:
            a posição do nó que contém a chave de busca
        Raises:
            ListaError: caso a chave não seja encontrada ou a lista esteja vazia
        '''
        if (self.estaVazia()):
            raise ListaError(f'Lista vazia')

        cursor = self.__head
        contador = 0
        
        while(True):
            contador+=1
            if( cursor.carga == key):
                return contador 
        
            cursor = cursor.next
            if (cursor == self.__head):
                break
          
        raise ListaError(f'A chave {key} não está armazenado na lista')


    def inserir(self, posicao:int, carga:any ):
        '''
        Insere um novo nó na lista, na posicao indicada, contendo a carga fornecida.
        Parâmetros:
            posicao (int): a posição do nó na lista
            carga (any): a carga do nó
        Raises:
            ListaError: caso a posicao indicada seja inválida
        '''
        try:
            assert posicao > 0 and posicao <= len(self)+1, f'Posicao invalida. Lista contém {self.__tamanho} elementos' 

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                if ( posicao != 1):
                    raise ListaError(f'A lista esta vazia. A posicao correta para insercao é 1.')
                
                novo = Node(carga)
                self.__head = novo
                novo.next = novo
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if ( posicao == 1):
                # Mover o cursor para o ultimo nó para ajustar o "prox"
                cursor = self.__head
                while(cursor.next != self.__head):
                    cursor = cursor.next
                # Criando o nó para inserção
                novo = Node(carga)
                novo.next = self.__head
                self.__head = novo
                # ajustando o link do ultimo no para novo
                cursor.next = novo
                self.__tamanho += 1
                return


            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while (contador < posicao-1):
                cursor = cursor.next
                contador += 1

            novo = Node(carga)
            novo.next = cursor.next
            cursor.next = novo
            self.__tamanho += 1

        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListaError(ae)

    def append(self, carga:any):
        '''
        Insere um novo nó no final da lista, com a carga fornecida.
        Parâmetros:
            carga (any): a carga do nó
        '''
        self.inserir(len(self)+1, carga)

    def remover(self, posicao:int)->any:
        '''
        Remove o nó da lista correspondnete à posicao indicada, e retorna a sua carga.
        Parâmetros:
            posicao (int): a posição do nó na lista
        Retorno:
            a carga do nó removido
        Raises:
            ListaError: se a posição for inválida ou a lista estiver vazia
        '''
        try:
            if( self.estaVazia() ):
                raise ListaError(f'Não é possível remover de uma lista vazia')            
            assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'


            cursor = self.__head            
            # CONDICAO 1: A lista só tem 1 elemento
            if self.__tamanho == 1:
                carga = self.__head.carga
                self.__head = None
            # CONDICAO 2: remover o primeiro elemento
            elif posicao == 1: 
                # posicionar o cursor no último elemento da lista circular
                while (cursor.next != self.__head):
                    cursor = cursor.next
                
                carga = self.__head.carga
                self.__head = self.__head.next
                cursor.next = self.__head
            else:
                # demais condições
                contador = 1
                while (contador < posicao - 1):
                    cursor = cursor.next
                    contador+=1
                apaga = cursor.next
                carga = apaga.carga
                cursor.next = apaga.next
                
            self.__tamanho -= 1
            return carga
        
        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListaError(ae)
        
    def __str__(self)->str:
        '''
        Retorna uma representação em string da lista
        '''
        str = 'Lista: [ '
        if self.estaVazia():
            str+= ']'
            return str

        cursor = self.__head

        while( True ):
            str += f'{cursor.carga}, '
            cursor = cursor.next
            if (cursor == self.__head):
                break

        str = str[:-2] + " ]"
        return str

    def __len__(self)->int:
        '''
        Retorna a quantidade de elementos existentes na lista
        '''
        return self.__tamanho

    # Métodos para implementação do protocolo "Iterator"
    def __iter__(self)->any:
        self.__ponteiro = self.__head
        self.__start = False
        return self
    
    def __next__(self)->any:
        if (self.__ponteiro == self.__head and self.__start):
            raise StopIteration
        else:
            carga = self.__ponteiro.carga
            self.__ponteiro = self.__ponteiro.next
            self.__start = True
            return carga

    def preparaPercurso(self, posicao:int):
        '''
        Prepara o ponteiro para percorrer a lista a partir do nó correspondente
        à  posicao indicada.
        '''
        # getNo() retorna o nó correspondente à posicao indicada. 
        # self.__ponteiro = self.__getNo(posicao)
        self.__ponteiro = self.__head

    def temProximo(self):
        return self.__ponteiro != None

    def pedirProximo(self):
        '''
        obtem a carga do nó apontado pelo ponteiro e avança o ponteiro para o
        próximo nó da lista.
        '''
        carga = self.__ponteiro.carga
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







