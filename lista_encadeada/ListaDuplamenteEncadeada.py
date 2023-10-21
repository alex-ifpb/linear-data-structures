class ListaException(Exception):
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

    def estaVazia(self):
        return self.__tamanho == 0

    def __len__(self):
        return self.__tamanho
    
    def inserir(self, posicao:int, carga:any):
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
            raise ListaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaException(f'A posicao deve ser um numero maior que zero e menor igual a {self.__tamanho+1}')
        except:
            raise

    def append(self, carga:any):
        self.inserir(self.__tamanho+1, carga)

    def remover(self, posicao:int)->any:
        try:
            assert posicao > 0 and posicao <= self.__tamanho

            if( self.estaVazia() ):
                raise ListaException(f'Não é possível remover de uma lista vazia')

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
            raise ListaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaException(f'A posicao não pode ser um número negativo')
        except:
            raise

    def busca(self, chave:any)->int:
        cont = 1
        cursor = self.__head
        while( cursor != None ):
            if cursor.carga == chave:
                return cont
            cont += 1
            cursor = cursor.prox

        raise ListaException(f'Chave {chave} não encontrada na Lista')        

    def elemento(self, posicao:int)->any:
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
            raise ListaException('Posicao invalida. Lista contém {self.__tamanho} elementos')        

    def modificar(self, posicao:int, novaCarga:any):
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
            raise ListaException(ae.__str__())
        
    def __str__(self):
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
    def __getitem__( self , index):
        return self.elemento(index)
    
    # Método mágico para permitir a iteração entre elementos
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.__tamanho:
            self.n += 1
            return self.elemento(self.n)
        else:
            raise StopIteration

    # Método mágico para emular o comportamento do objeto à chamada da
    # função reversed()
    def __reversed__(self):
        for i in range(self.__tamanho,0,-1):
            yield self.elemento( i ) 