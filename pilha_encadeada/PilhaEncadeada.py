class PilhaError(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos
       da pilha é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class Node:
    '''
    Classe que implementa um nó de uma lista encadeada simples.
    Atributos:
        carga (any): a carga armazenada no nó
        prox (Node): o apontador para o próximo nó da lista
    '''
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self)->any:
        return self.__carga
    
    @carga.setter
    def carga(self, carga):
        self.__carga = carga

    @property
    def prox(self)->'Node':
        return self.__prox
    
    @prox.setter
    def prox(self, prox:'Node'):
        self.__prox = prox

    def temProximo(self)->bool:
        return self.__prox != None
    
    def __str__(self):
        return str(self.__carga)


class Pilha:
    """
    Classe que implementa a estrutura de dados "Pilha" utilizando a técnica
    simplesmente encadeada.

     Attributes:
        head (Node): apontador para o nó topo da pilha
        tamanho (int): quantidade de elementos existentes na pilha
    """

    def __init__(self):
        """ Construtor padrão da classe Pilha sem argumentos. 
            Ao instanciar um objeto do tipo Pilha, esta iniciará 
            sem elementos. 
        """
        self.__head = None
        self.__tamanho = 0        

    def estaVazia(self)->bool:
        """ Método que verifica se a pilha está vazia.

        Returns:
            boolean: True se a pilha estiver vazia, False caso contrário

        Examplo de uso:
            p = Pilha()
            if(p.estaVazia()): 
               <instrucoes>
        """
        return self.__head == None

    def __len__(self)->int:
        """ Método para obter a quantidade de elementos existentes na pilha

        Returns:
            int: um número inteiro que determina o número de elementos existentes na pilha

        Examplo de uso:
            p = Pilha()
            # considere que temos internamente a pilha topo->[10,20,30,40]
            print (len(p)) # exibe 4
        """        

        return self.__tamanho

    def elemento(self, posicao:int)->any:
        """ Método que recupera o valor armazenado em um determinado elemento da pilha

        Argumentos:
            posicao (int): a posicao do elemento que deseja obter a carga. 
            A ordem dos elementos é na direção da base até o topo da pilha.
            A base é o primeiro elemento (1) e o topo é o último (n).
        
        Returns:
            any: a carga armazenada na ordem indicada por posição.

        Raises:
            PilhaError: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos existentes na pilha.                      
        Examplo de uso:
            p = Pilha()
            print (p.elemento(3)) 
        """
        try:
            assert not self.estaVazia(), 'A pilha está vazia'
            assert  0 < posicao <= len(self), f'A posicao {posicao} NAO é válida para a pilha de tamanho {self.__tamanho}'
 
            cursor = self.__head
            for _ in range( len(self)-posicao):
                cursor = cursor.prox
            return cursor.carga
                
        except TypeError:
            raise PilhaError('o argumento "posicao" deve ser um número inteiro')
        except AssertionError as ae:
            raise PilhaError(ae.__str__())
        except:
            raise

    def busca(self, chave:any)->int:
        """ Método que recupera a posicao ordenada, dentro da pilha, em que se
            encontra a chave passada como argumento. No caso de haver mais 
            de uma da chave, será retornada apenas a primeira ocorrência.

        Argumentos:
            chave: um item de dado que deseja procurar na pilha
        
        Returns:
            int: um número inteiro representando a posição, na pilha, em que foi
                 encontrada a  "chave". A posição é contada a partir da base da
                 pilha (1), em direção ao topo (n)

        Raises:
            PilhaError: Exceção lançada quando a chave não 
                  estiver presente na pilha.

        Examplo de uso:
            p = Pilha()
            print (p.busca(10)) 
        """
        cursor = self.__head
        contador = len(self)

        while( cursor != None):
            if cursor.carga == chave:
                return contador
            cursor = cursor.prox
            contador -= 1

        raise PilhaError(f'Chave {chave} nao esta na pilha')
        
    def topo(self)->any:
        """ Método que devolve a carga que se encontra no topo da pilha, sem desempilhá-la
    
        Returns:
            any: o conteúdo referente ao elemento do topo

        Raises:
            PilhaError: Exceção lançada quando se tenta consultar o topo de uma
                   uma pilha vazia
                    
        Examplo de uso:
            p = Pilha()
            dado = p.topo()
            print(dado) 
        """
        if not self.estaVazia():
            return self.__head.carga
        raise PilhaError('A pilha está vazia')
    

    def empilha(self, carga:any):
        """ Método que adiciona um novo elemento ao topo da pilha

        Argumentos:
            carga(any): o conteúdo a ser inserido no topo da pilha.

        Examplo de uso:
            p = Pilha()
            # considere a pilha  topo->[10,20,30,40]
            p.empilha(50)
            print(p)  # exibe topo->[50,10,20,30,40]
        """
        novo = Node(carga)
        novo.prox = self.__head
        self.__head = novo
        self.__tamanho += 1


    def desempilha(self)->any:
        """ Método que remove um elemento do topo da pilha e devolve 
            a carga armazenada.
    
        Returns:
            any: a carga removida do topo da pilha

        Raises:
            PilhaError: Exceção lançada quando se tenta remover de uma pilha vazia
                    
        Examplo de uso:
            p = Pilha()
            dado = p.desemplha()
            print(p)
            print(dado) 
        """
        if not self.estaVazia():
            carga = self.__head.carga
            self.__head = self.__head.prox
            self.__tamanho -= 1
            return carga
        raise PilhaError('A pilha está vazia')
   
    def __str__(self):
        """ Método que devolve uma string contendo os elementos da pilha
            separados por vírgula e entre colchetes. A ordem de exibição é
            da base para o topo da pilha.   
        """
        cursor = self.__head
        s = 'topo->['
        while( cursor != None):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.strip(', ')
        s += ']'
        return s

 

