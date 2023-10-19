class PosicaoInvalidaException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)

class ValorInexistenteException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """

    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)

class ListaException(Exception):
    """Classe de exceção lançada quando uma violação de ordem genérica
       da lista é identificada.
    """

    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)

class Lista:
    """A classe Lista.py implementa a estrutura de dados Lista.
       Esta implementação usando a técnica sequencial está apta a manusear
       qualquer tipo de dado como carga, seja tipo primitivo ou objeto.
       A estrutura sequencial utilizada na implementação é um list de python
       que não é um array por natureza

     Attributes:
        dado (list): um array de tamanho finito
    """
    def __init__(self, size:int = 50):
        """ Construtor padrão da classe Lista. Ao instanciar
            um objeto do tipo Lista, este iniciará vazio. 
        """
        try:
            assert size > 0
        except AssertionError:
            raise  ListaException("Tamanho do array deve ser um número maior do que zero.")
        
        self.__dado = [None] * size
        self.__final = 0 # Indica o índice até onde se tem elementos no array
        self.__size = size


    def estaVazia(self):
        """ Método que verifica se a lista está vazia ou não

        Returns:
            boolean: True se a lista estiver vazia, False caso contrário

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]            
            if(lst.estaVazia()): #
               # instrucoes
        """
        return self.__final == 0

    def estaCheia(self):
        """ Método que verifica se a lista está cheia

        Returns:
            boolean: True se a lista estiver cheia, False caso contrário

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]            
            if(lst.estaCheia()): #
               # instrucoes
        """
        return self.__final == self.__size 


    def __len__(self):
        """ Método que retorna a quantidade de elementos existentes na lista

        Returns:
            int: um número inteiro que determina o número de elementos existentes na lista

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]            
            print (len(lst)) # exibe 4
        """        
        return self.__final


    def elemento(self, posicao):
        """ Método que recupera o valor armazenado em um determinado elemento da lista

        Args:
            posicao (int): um número correpondente à ordem do elemento existente na lista
        
        Returns:
            int: o valor armazenado na ordem indicada por posição.

        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.                      
        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            posicao = 5
            print (lst.elemento(3)) # exibe 30
        """
        try:
            if posicao > 0 and posicao > self.__len__():
                raise PosicaoInvalidaException(f"Posicao {posicao} invalida para recuperacao.")
            return self.__dado[posicao-1]
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')

    def modificar(self, posicao:int, carga:any):
        """ Método que altera o conteúdo armazenado em um elemento específico da lista

        Args:
            posicao (int): um número correpondente à ordem do elemento existente na lista
            valor (qualquer tipo primitivo): o novo valor que vai ser armazenado no elemento Ei
        
        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.                      
        Examplo de uso:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            posicao = 3
            lst.modificar( posicao, 55)
            print (lst.elemento( posicao )) # exibe 55
        """
        try:
            assert posicao > 0 and posicao <= self.__len__()
            self.__dado[posicao-1] = carga
        except TypeError:
            raise ListaException(f'O tipo de dado para posicao não é do tipo inteiro')
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo ou maior que a quantidade atual de elementos')
        except:
            raise

    
    def busca(self, chave:any)->int:
        """ Método que recupera a posicao ordenada, dentro da lista, em que se
            encontra um valor passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será levada em conta

        Args:
            chave (any): A chave de busca a procurar na lista
        
        Returns:
            int: um número inteiro representando a posição, na lista, em que foi
                 encontrado "valor".

        Raises:
            ValorInexistenteException: Exceção lançada quando o argumento "valor"
                  não está presente na lista.

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            print (lst.elemento(40)) # exibe 4
        """
        
        for i in range(self.__final):
            if (self.__dado[i] == chave):
                return i+1
        raise ValorInexistenteException(f'Chave {chave} nao esta na lista')


    def inserir(self, posicao:int, carga:any ):
        """ Método que adiciona um novo valor à lista

        Args:
            posicao (int): um número correpondente à posição em que se deseja
                  inserir um novo valor
            carga (any): o conteúdo que deseja armazenar
                  na lista.

        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            lst.insere(3,50)
            print(lst)  # exibe [10,20,50,30,40]
        """
        try:
            assert not self.estaCheia(),"Lista cheia. Nao é possivel inserir elementos"
            assert posicao > 0 and posicao <= self.__len__()+1,"Posicao invalida para insercao"

            for i in range(self.__final, posicao-1, -1):
                self.__dado[i] = self.__dado[i-1]
            
            self.__dado[posicao-1] = carga
            self.__final += 1
        except AssertionError as ae:
            raise ListaException(ae.__str__())
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')
        except:
            raise

    def remover(self, posicao:int)->any:
        """ Método que remove um elemento da lista e devolve o conteudo
            existente na ordem indicada.

        Args:
            posicao (int): um número correpondente à ordem do elemento na lista
        
        Returns:
            qualquer tipo primitivo: o valor encontrado no elemento removido

        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.                      
        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = lst.remover(2)
            print(lst) # exibe [10,30,40]
            print(dado) # exibe 20
        """
        if self.estaVazia():
            raise ListaException('Pilha vazia. Nao há elementos para remoção.')
        try:
            assert posicao > 0 and posicao <= self.__len__(),f'Posicao invalida para remocao. Informe um numero de 1 a {self.__len__()}'

            carga = self.__dado[posicao-1]
            # Iniciando o deslocamento à esquerda dos elementos
            for i in range(posicao, self.__final):
                self.__dado[i-1] = self.__dado[i]

            self.__final -= 1
            return carga
        except TypeError:
            raise ListaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError as ae:
            raise PosicaoInvalidaException(ae.__str__())
        except:
            raise


    def imprimir(self):
        """ Método que exibe a sequência ordenada dos elementos da lista

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]            
            lst.imprimir()) # exibe Lista: [10,20,30,40]
        """  
        print('Lista: ',end='')
        print(self.__str__())


        
    def __str__(self):
        s = '[ '
        if self.estaVazia():
            s+= ']'
            return s
        for i in range(self.__final):
            s += f'{self.__dado[i]}, '
        s = s[:-2] + " ]"
        return s
       

if __name__ == '__main__':
    lst = Lista()
    try:
        print('Vazia:', lst.estaVazia())
        print('Cheia:', lst.estaCheia())
        print(len(lst))
        lst.inserir(1,50)
        print(lst)
        lst.inserir(2,55)
        print(lst)
        lst.inserir(3,60)
        print(lst)
        lst.inserir(1,45)
        print(lst)
        lst.inserir(3, 53)
        print(lst)
        lst.inserir(5,57)
        print(lst)

        # print(lst.elemento(-8))
        #print(lst.elemento(10))
        #print(lst.elemento('a'))
        print(lst.elemento(3))
        print(lst.busca(45))
        #lst.busca(40)


        carga = lst.remover(3)
        print('carga:',carga)
        print(lst)
        carga = lst.remover(5)
        print('carga:', carga)
        print(lst)
        carga = lst.remover(1)
        print('carga:', carga)
        print(lst)

        valor = lst.remover(15)
        lst.imprimir()
    except ListaException as le:
        print(le)
    except PosicaoInvalidaException as pie:
        print(pie)
    except ValorInexistenteException as vie:
        print(vie)    
    except Exception as e:
        print('Nossos engenheiros vao analisar esse problema')
        print(e.__class__.__name__)
