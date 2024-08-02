class ListaError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None
        self.__ant = None

    @property
    def carga(self):
        return self.__carga

    @property
    def prox(self):
        return self.__prox

    @property
    def ant(self):
        return self.__ant

    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx

    @ant.setter
    def ant(self, novoAnt):
        self.__ant = novoAnt
    
    def __str__(self):
        return f'{self.__carga}'


class Lista:
    '''
    Implementação de uma lista duplamente encadeada.
    Nesta classe, são empregados os métodos mágicos:
    __len__(), __str__(), __getitem__(), __iter__() e __next__()
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
            assert posicao > 0 and posicao <= len(self)
            cont = 1
            cursor = self.__head
            while( cursor != None ):
                if cont == posicao:
                    break
                cont += 1
                cursor = cursor.prox
            
            return cursor.carga
        except AssertionError:
            raise ListaError('Posicao invalida. Lista contém {self.__tamanho} elementos')        

    def busca(self, chave:any)->int:
        '''
        Verifica a existência da chave de busca na lista e retorna a posição do nó que a contém.
        Parâmetros:
            key (any): a chave de busca
        Retorno:
            a posição do nó que contém a chave de busca
        Raises:
            ListaError: caso a chave não seja encontrada ou a lista esteja vazia
        '''        
        cont = 1
        cursor = self.__head
        while( cursor != None ):
            if cursor.carga == chave:
                return cont
            cont += 1
            cursor = cursor.prox

        raise ListaError(f'Chave {chave} não encontrada na Lista')        

    def modificar(self, posicao:int, novaCarga:any):
        '''
        Modifica a carga do nó correspondente à posicao indicada.
        Parâmetros:
            posicao (int): posição do nó cuja carga se deseja modificar
            carga (any): a nova carga do nó
        Raises:
            ListaError: caso a posicao indicada seja inválida ou a lista esteja vazia
        '''        
        try:
            assert posicao > 0 and posicao <= len(self),f'Posicao invalida. Lista contém {self.__tamanho} elementos'
            assert not self.estaVazia(),'Lista vazia'
            cont = 1
            cursor = self.__head
            while( cursor != None ):
                if cont == posicao:
                    break
                cont += 1
                cursor = cursor.prox
            
            cursor.carga = novaCarga

        except AssertionError as ae:
            raise ListaError(ae.__str__())
        
    def inserir(self, posicao:int, carga:any):
        '''
        Insere um novo nó na lista, na posicao indicada, contendo a carga fornecida.
        Parâmetros:
            posicao (int): a posição do nó na lista
            carga (any): a carga do nó
        Raises:
            ListaError: caso a posicao indicada seja inválida
        '''
        try:
            assert posicao > 0 and posicao <= self.__tamanho + 1

            novo = No(carga)
            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                self.__head = novo
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if ( posicao == 1):
                novo.prox = self.__head
                self.__head.ant = novo
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while ( contador < posicao -1 ):
                cursor = cursor.prox
                contador += 1

            novo.prox = cursor.prox
            novo.ant = cursor
            # Teste apenas para uma insercao entre dois elementos já existentes.
            if cursor.prox != None:
                cursor.prox.ant = novo
            cursor.prox = novo 

            self.__tamanho += 1

        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaError(f'A posicao deve ser um numero maior que zero e menor igual a {self.__tamanho+1}')
        except:
            raise

    def append(self, carga:any):
        '''
        Insere um novo nó no final da lista, com a carga fornecida.
        Parâmetros:
            carga (any): a carga do nó
        '''
        self.inserir(self.__tamanho+1, carga)

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
            assert not self.estaVazia(),'Lista vazia'
            assert posicao > 0 and posicao <= self.__tamanho, f'A posicao deve ser maior que zero e menor igual a {self.__tamanho}'

            if( self.estaVazia() ):
                raise ListaError(f'Não é possível remover de uma lista vazia')

            cursor = self.__head
            contador = 1

            while( contador < posicao ) :
                cursor = cursor.prox
                contador+=1

            carga = cursor.carga
            # Remoção do primeiro elemento: mexe com o "head"
            if( posicao == 1):
                self.__head = cursor.prox
                if self.__head != None:
                    self.__head.ant = None
            else:
                cursor.ant.prox = cursor.prox
                if cursor.prox != None:
                    cursor.prox.ant = cursor.ant

            self.__tamanho -= 1
            return carga
        
        except TypeError:
            raise ListaError(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListaError(ae.__str__() )
        except:
            raise

    def __str__(self):
        '''
        Retorna uma representação em string da lista
        '''
        s = '[ '
        # código base para percorrer qualquer estrutura linear
        cursor = self.__head
        while( cursor != None ):
            s += f'{cursor.carga}, '
            # incremento do cursor
            cursor = cursor.prox
        s += ' ]'
        return s

    # Método mágico em Python, que quando usado em uma classe, permite que
    # a instância da classe utilize a sintaxe do operador  [] para indexar
    # seus elementos
    def __getitem__( self, posicao:int):
        return self.elemento(posicao)
    
    def __setitem__( self, posicao, novaCarga):
        self.modificar(posicao, novaCarga)

    def __iter__(self)->any:
        self.__ponteiro = self.__head
        return self
    
    def __next__(self)->any:
        if (self.__ponteiro == None):
            raise StopIteration
        else:
            carga = self.__ponteiro.carga
            self.__ponteiro = self.__ponteiro.prox
            return carga
    
    def __len__(self):
        return self.__tamanho


    # Método mágico para emular o comportamento do objeto à chamada da
    # função reversed()
    # def __reversed__(self):
    #     for i in range(self.__tamanho,0,-1):
    #         yield self.elemento( i ) 
    
    def __reversed__(self):
        self.__ponteiro = self.__head
        #posiciona no último elemento
        while(self.__ponteiro.prox is not None):
            self.__ponteiro = self.__ponteiro.prox
        #percorre a lista de trás para frente
        while(self.__ponteiro is not None):
            yield self.__ponteiro.carga
            self.__ponteiro = self.__ponteiro.ant
        