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


class ListaException(Exception):
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
                

    # Métodos para implementação do protocolo "Iterator"
    def __iter__(self)->any:
        self.__ponteiro = self.__head
        return self
    
    def __next__(self)->any:
        if (self.__ponteiro == None):
            raise StopIteration
        else:
            carga = self.__ponteiro.carga
            self.__ponteiro = self.__ponteiro.next
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



    def estaVazia(self):
        return self.__tamanho == 0

    def __len__(self):
        return self.__tamanho

    def elemento(self, posicao:int):

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
            raise ListaException(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListaException(ae)


    def modificar(self, posicao:int, carga: any):
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
            raise ListaException(f'A posição deve ser um número do tipo inteiro')            
        except AssertionError as ae:
            raise ListaException(ae.__str__())

    def busca(self, key:any)->int:
        if (self.estaVazia()):
            raise ListaException(f'Lista vazia')

        cursor = self.__head
        contador = 0
        
        while(True):
            contador+=1
            if( cursor.carga == key):
                return contador 
        
            cursor = cursor.next
            if (cursor == self.__head):
                break
          
        raise ListaException(f'A chave {key} não está armazenado na lista')


    def inserir(self, posicao:int, carga:any ):

        try:
            assert posicao > 0 and posicao <= len(self)+1, f'Posicao invalida. Lista contém {self.__tamanho} elementos' 

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                if ( posicao != 1):
                    raise ListaException(f'A lista esta vazia. A posicao correta para insercao é 1.')
                
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
            raise ListaException(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListaException(ae)


    def remover(self, posicao:int)->any:
        try:
            if( self.estaVazia() ):
                raise ListaException(f'Não é possível remover de uma lista vazia')            
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
            raise ListaException(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListaException(ae)
        
    def __str__(self):
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










