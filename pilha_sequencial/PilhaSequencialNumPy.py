import numpy as np

class PilhaError(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos
       da pilha é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


        
class Pilha:
    """Classe que implementa a estrutura de dados "Pilha" utilizando a técnica sequencial.
       A classe permite que qualquer tipo de dado seja armazenada na pilha.

     Atributos:
        dado (numpy.ndarray): array de armazenamento dos dados da pilha
        topo (int): um número inteiro que representa o índice do elemento
             que está no topo da pilha
    """
    def __init__(self, size:int=50):
        """ Construtor padrão da classe Pilha sem argumentos. Ao instanciar
            um objeto do tipo Pilha, esta iniciará vazia. 

        Args:
        ---------------------
            size (int, opcional): tamanho da pilha. Default é 10.

        """
        self.__dado = np.full(size,None)
        self.__topo = -1

    def estaVazia(self)->bool:
        """ Método que verifica se a pilha está vazia ou não

        Returns:
            boolean: True se a pilha estiver vazia, False caso contrário

        Examples:
            p = Pilha()
            if(p.estaVazia()): 
               <instruções>
        """
        return self.__topo == -1 
    
    def estaCheia(self)->bool:
        """ Método que verifica se a pilha está cheia

        Returns:
            boolean: True se a pilha estiver cheia, False caso contrário

        Examples:
            p = Pilha()
            if(p.estaCheia()): 
               <instruções>
        """
        return self.__topo == len(self.__dado) - 1 

    def __len__(self)->int:
        """ Método que consulta a quantidade de elementos existentes na pilha

        Returns:
            int: um número inteiro que determina o número de elementos existentes na pilha

        Examples:
            p = Pilha()
            print (len(p))
        """        
        return self.__topo + 1


    def get(self, posicao:int)->any:
        """ Método que recupera o valor armazenado em um determinado elemento da pilha

        Argumentos:
            posicao (int): o elemento que deseja obter a carga.
            A ordem dos elementos é na direção da base até o topo da pilha.
        
        Returns:
            any: a carga armazenada na ordem indicada por posição.

        Raises:
            PilhaError: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos existentes na pilha.                      
        Examples:
            p = Pilha()
            print (p.get(3))
        """
        try:
            if self.estaVazia():
                raise PilhaError(f'Pilha está Vazia.')
            assert posicao > 0 and posicao <= self.__topo + 1
            return self.__dado[posicao-1]
        except TypeError:
            raise PilhaError(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PilhaError(f'A posicao deve ser um número maior que zero e menor igual a {self.__topo+1}')
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
                 pilha, em direção ao topo

        Raises:
            KeyError: Exceção lançada quando a chave não 
                  estiver presente na pilha.

        Examples:
            p = Pilha()
            print (p.get(40)) 
        """        
        for i in range(self.__topo+1):
            if (self.__dado[i] == chave):
                return i+1
        raise KeyError(f'Chave {chave} nao esta na lista')
        #    não dá pra fazer com o np.where, pois ele vai procurar no array todo
        #    resultado = np.where(self.__dado == valor)
        #    return resultado[0][0]

    def topo(self)->any:
        """ Método que devolve o elemento localizado no topo, sem desempilhá-lo
    
        Returns:
            any: o conteúdo referente ao elemento do topo

        Raises:
            PilhaError: Exceção lançada quando se tenta consultar o topo de uma
                   uma pilha vazia
                    
        Examples:
            p = Pilha()
            dado = p.topo()
            print(dado) 
        """
        try:
            return self.__dado[self.__topo]
        except IndexError:
            raise PilhaError(f'Pilha Vazia. Não há elemento no topo')
        except:
            raise


    def empilha(self, carga:any):
        """ Método que adiciona um novo elemento ao topo da pilha

        Argumentos:
            carga(any): o conteúdo a ser inserido no topo da pilha.

        Examples:
            p = Pilha()
            p.empilha(50)
            print(p)  
        """
        if self.__topo == len(self.__dado) - 1:
            raise PilhaError(f'Pilha Cheia. Não é possível efetuar a inserção')
        self.__topo += 1
        self.__dado[self.__topo] = carga


    def desempilha(self)->any:
        """ Método que remove um elemento do topo da pilha e devolve 
            a carga correspondente a esse elemento removido.
    
        Returns:
            any: a carga removida do topo da pilha

        Raises:
            PilhaError: Exceção lançada quando se tenta remover de uma pilha vazia
                    
        Examples:
            p = Pilha()
            dado = p.desemplha()
            print(p) 
            print(dado) 
        """
        if self.estaVazia():
            raise PilhaError(f'Pilha Vazia. Não é possível efetuar a remoção')
        carga = self.__dado[self.__topo]
        self.__topo -= 1
        return carga
    
    def __str__(self):
        """ Método que devolve uma string contendo os elementos da pilha
            separados por vírgula e entre colchetes. A ordem de exibição é
            da base para o topo da pilha.   
        """
        s = '['
        for i in range(self.__topo+1):
            s += str(self.__dado[i]) + ','
        s = s.rstrip(',') # remove a última vírgula
        s += ']<-topo'
        return s

    def __iter__(self)->any:
        self.__index = 0
        return self
    
    def __next__(self)->any:
        if (self.__index > self.__topo):
            raise StopIteration
        else:
            carga = self.__dado[self.__index]
            self.__index += 1
            return carga

    def __contains__(self, key:any)->bool:
        '''
        Método que verifica se uma chave está presente na pilha.
        Acionado em situações de uso do operador "in": "if chave in pilha".
        Argumentos:
            key(Any): chave do elemento a ser buscado.
        Retorna:
            bool: True se a chave estiver na pilha e False caso contrário.
        '''
        try:
            self.busca(key)
            return True
        except KeyError:
            return False

    def __getitem__( self, posicao:int):
        return self.get(posicao)
    
      