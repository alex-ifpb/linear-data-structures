class FilaException(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos
       da fila é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


        
class Fila:
    """A classe Fila.py implementa a estrutura de dados "Fila".
       A classe permite que qualquer tipo de dado seja armazenada na fila.

     Attributes:
        dado (list): uma estrutura de armazenamento dinâmica dos elementos da
             fila
    """
    def __init__(self):
        """ Construtor padrão da classe Fila sem argumentos. Ao instanciar
            um objeto do tipo Fila, esta iniciará vazia. 
        """
        self.__dado = []



    def estaVazia(self):
        """ Método que verifica se a fila está vazia ou não

        Returns:
            boolean: True se a fila estiver vazia, False caso contrário

        Examples:
            f = Fila()
            ...   # considere que temos internamente na fila frente->[10,20,30,40]
            if(f.estaVazia()): #
               # instrucoes
        """
        return True if len(self.__dado)==0 else False

    def tamanho(self):
        """ Método que consulta a quantidade de elementos existentes na fila

        Returns:
            int: um número inteiro que determina o número de elementos existentes na fila

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila frente->[10,20,30,40]
            print (f.tamanho()) # exibe 4
        """        
        return len(self.__dado)


    def elemento(self, posicao):
        """ Método que recupera o valor armazenado em um determinado elemento da fila

        Args:
            posicao (int): um número correpondente à ordem do elemento existente,
                na direção da base até o topo
        
        Returns:
            int: o valor armazenado na ordem indicada por posição.

        Raises:
            FilaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.                      
        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila frente->[10,20,30,40]
            posicao = 5
            print (f.elemento(3)) # exibe 30
        """
        try:
            assert posicao > 0
            return self.__dado[posicao-1]
        except IndexError:
            raise FilaException(f'Posicao {posicao} invalida para a Fila')
        except TypeError:
            raise FilaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise FilaException(f'A posicao deve ser um número maior que zero')
        except:
            raise

    
    def busca(self, valor):
        """ Método que recupera a posicao ordenada, dentro da fila, em que se
            encontra um valor passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será retornada

        Args:
            valor: um item de dado que deseja procurar na fila
        
        Returns:
            int: um número inteiro representando a posição, na fila, em que foi
                 encontrado "valor".

        Raises:
            FilaException: Exceção lançada quando o argumento "valor"
                  não está presente na fila.

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente->[10,20,30,40]
            print (f.elemento(40)) # exibe 4
        """
        try:
            return self.__dado.index(valor) + 1
        except ValueError:
            raise FilaException(f'O valor {valor} não está armazenado na fila')
        except:
            raise

    def enfileirar(self, valor ):
        """ Método que adiciona um novo elemento na frente da fila

        Args:
            valor(qualquer tipo de dado): o conteúdo que deseja armazenar
                  na fila.

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente-> [10,20,30,40]
            f.enfileirar(50)
            print(f)  # exibe [10,20,30,40,50]
        """
        self.__dado.append(valor)


    def desenfileirar(self):
        """ Método que remove um elemento do final da fila e devolve o conteudo
            existente removido.
    
        Returns:
            qualquer tipo de dado: o conteúdo referente ao elemento removido

        Raises:
            FilaException: Exceção lançada quando se tenta remover algo de uma fila vazia
                    
        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente-> [10,20,30,40]
            dado = f.desenfileirar()
            print(f) # exibe [10,20,30]
            print(dado) # exibe 40
        """
        try:
            '''
            conteudo = self.__dado[0]
            del self.__dado[0]
            return conteudo
            '''

            return self.__dado.pop(0)
        except IndexError:
            raise FilaException(f'Fila Vazia. Não é possível efetuar a remoção')
        except:
            raise


    def imprimir(self):
        """ Método que exibe a sequência ordenada dos elementos da fila

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente->[10,20,30,40]
            f.imprimir()) # exibe fila: frente->[10,20,30,40]
        """  
        print('Frente-> ' + self.__dado.__str__() )


        
    def __str__(self):
        return self.__dado.__str__()
       


f = Fila()
try:
    for i in range(1,10):
        f.enfileirar(i*10)
    print(f.desenfileirar())

    print(f)
  
    #print(f.elemento(-8))
    #print(f.elemento(10))
    #print(f.elemento('a'))

    print(f.elemento(3))
    print(f.busca(80))
    #print(f.busca('joao'))
    f.imprimir()
    f.enfileirar(111)
    f.imprimir()
    f.desenfileirar()
    f.imprimir()

 
except FilaException as fe:
    print(fe)
except Exception as e:
    print('Nossos engenheiros vao analisar esse problema')
    
    

     

    
        


        
