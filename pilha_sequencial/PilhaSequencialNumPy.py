import numpy as np

class PilhaException(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos
       da pilha é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


        
class Pilha:
    """A classe Pilha.py implementa a estrutura de dados "Pilha".
       A classe permite que qualquer tipo de dado seja armazenada na pilha.

     Attributes:
        dado (list): uma estrutura de armazenamento dinâmica dos elementos da
             pilha
        topo (int): um número inteiro que representa o índice do elemento
             que está no topo da pilha
    """
    def __init__(self, size:int=10):
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
            ...   # considere que temos internamente na pilha [10,20,30,40]<- topo
            if(p.estaVazia()): #
               # instrucoes
        """
        return True if self.__topo==-1 else False
    


    def __len__(self)->int:
        """ Método que consulta a quantidade de elementos existentes na pilha

        Returns:
            int: um número inteiro que determina o número de elementos existentes na pilha

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<- p
            print (p.tamanho()) # exibe 4
        """        
        return self.__topo + 1


    def elemento(self, posicao:int)->any:
        """ Método que recupera o valor armazenado em um determinado elemento da pilha

        Argumentos:
            posicao (int): o elemento que deseja obter a carga.
            A ordem dos elementos é na direção da base até o topo da pilha.
        
        Returns:
            any: a carga armazenada na ordem indicada por posição.

        Raises:
            PilhaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos existentes na pilha.                      
        Examples:
            p = Pilha()
            # considere que temos internamente a pilha [10,20,30,40]<-topo
            print (p.elemento(3)) # exibe 30
        """
        try:
            if self.estaVazia():
                raise PilhaException(f'Pilha está Vazia.')
            assert posicao > 0 and posicao <= self.__topo + 1
            return self.__dado[posicao-1]
        except TypeError:
            raise PilhaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PilhaException(f'A posicao deve ser um número maior que zero e menor igual a {self.__topo+1}')
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
            PilhaException: Exceção lançada quando a chave não 
                  estiver presente na pilha.

        Examples:
            p = Pilha()
            # considere que temos internamente a pilha [10,20,30,40]<-topo
            print (p.elemento(40)) # exibe 4
        """        
        for i in range(self.__topo+1):
            if (self.__dado[i] == chave):
                return i+1
        raise PilhaException(f'Chave {chave} nao esta na lista')
        #    não dá pra fazer com o np.where, pois ele vai procurar no array todo
        #    resultado = np.where(self.__dado == valor)
        #    return resultado[0][0]

    def topo(self)->any:
        """ Método que devolve o elemento localizado no topo, sem desempilhá-lo
    
        Returns:
            any: o conteúdo referente ao elemento do topo

        Raises:
            PilhaException: Exceção lançada quando se tenta consultar o topo de uma
                   uma pilha vazia
                    
        Examples:
            p = Pilha()
            # considere que temos internamente a pilha [10,20,30,40]
            dado = p.topo()
            print(dado) # exibe 40
        """
        try:
            return self.__dado[-1]
        except IndexError:
            raise PilhaException(f'Pilha Vazia. Não há elemento no topo')
        except:
            raise


    def empilha(self, carga:any):
        """ Método que adiciona um novo elemento ao topo da pilha

        Argumentoss:
            carga(any): o conteúdo a ser inserido no topo da pilha.

        Examples:
            p = Pilha()
            # considere a pilha [10,20,30,40]<-topo
            p.empilha(50)
            print(p)  # exibe [10,20,30,40,50]
        """
        if self.__topo == len(self.__dado) - 1:
            raise PilhaException(f'Pilha Cheia. Não é possível efetuar a inserção')
        self.__topo += 1
        self.__dado[self.__topo] = carga



    def desempilha(self)->any:
        """ Método que remove um elemento do topo da pilha e devolve 
            a carga correspondente a esse elemento removido.
    
        Returns:
            any: a carga removida do topo da pilha

        Raises:
            PilhaException: Exceção lançada quando se tenta remover de uma pilha vazia
                    
        Examples:
            p = Pilha()
            # considere que temos internamente a pilha [10,20,30,40]<-topo
            dado = p.desemplha()
            print(p) # exibe [10,20,30]
            print(dado) # exibe 40
        """
        if self.estaVazia():
            raise PilhaException(f'Pilha Vazia. Não é possível efetuar a remoção')
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




if __name__ == '__main__':
       

    def imprimeInvertido(str):
        p = Pilha()
        for s in str:
            if (s==' '):
                try:
                    while(True):
                        print(p.desempilha(),end='')
                except:
                    print(' ',end='')
            else:
                p.empilha(s)
        if not p.estaVazia():
            try:
                while(True):
                    print(p.desempilha(),end='')
            except:
                pass
        
    
    p = Pilha()
    try:
        for i in range(1,10):
            p.empilha(i*10)
        print(p.desempilha())
        p.empilha('alex')
        #p.imprimir()
        print(p)
  
        #print(p.elemento(-8))
        #print(p.elemento(10))
        #print(p.elemento('a'))

        print(p.elemento(3))
        print(p.busca(80))
        #print(p.busca('joao'))
        print(p)

        '''
        #lst.busca(40)
        print('Inserindo o valor 50 na 2a posicao')
        lst.inserir(2,50)
        print('Valor inserido com sucesso!')
        print(lst)
        valor = lst.remover(4)
        print('valor:',valor)
        print(lst)
        #valor = lst.remover(10)
        lst.imprimir()
        '''

        imprimeInvertido('Estrutura de Dados')
    except PilhaException as pe:
        print(pe)
    except Exception as e:
        print('Nossos engenheiros vao analisar esse problema')
    except:
        print('FIM')

     

    
        


        
