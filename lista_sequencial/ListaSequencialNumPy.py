import numpy as np


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
        
        self.__dado = np.full(size,None)
        self.__final = 0 # Indica o índice até onde se tem elementos no array


    def estaVazia(self)->bool:
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

    def estaCheia(self)->bool:
        """ Método que verifica se a lista está cheia

        Returns:
            boolean: True se a lista estiver cheia, False caso contrário

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]            
            if(lst.estaCheia()): #
               # instrucoes
        """
        return self.__final == len(self.__dado) 


    def __len__(self)->int:
        """ Método que retorna a quantidade de elementos existentes na lista

        Returns:
            int: um número inteiro que determina o número de elementos existentes na lista

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]            
            print (len(lst)) # exibe 4
        """        
        return self.__final


    def elemento(self, posicao:int)->any:
        """ Método que recupera o valor armazenado em um determinado elemento da lista

        Args:
            posicao (int): um número correpondente à ordem do elemento existente na lista
        
        Returns:
            any: a carga armazenada na ordem indicada por posição.

        Raises:
            ListaException: Exceção lançada quando uma posição inválida é
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
            if posicao > 0 and posicao > len(self):
                raise ListaException(f"Posicao {posicao} invalida para recuperacao.")
            return self.__dado[posicao-1]
        except TypeError:
            raise ListaException(f'O tipo de dado para posicao não é um número inteiro')

    def modificar(self, posicao:int, carga:any):
        """ Método que altera o conteúdo armazenado em um elemento específico da lista

        Args:
            posicao (int): um número correpondente à ordem do elemento existente na lista
            valor (qualquer tipo primitivo): o novo valor que vai ser armazenado no elemento Ei
        
        Raises:
            ListaException: Exceção lançada quando uma posição inválida é
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
            assert posicao > 0 and posicao <= len(self)
            self.__dado[posicao-1] = carga
        except TypeError:
            raise ListaException(f'O tipo de dado para posicao não é do tipo inteiro')
        except AssertionError:
            raise ListaException(f'A posicao não pode ser um número negativo ou maior que a quantidade atual de elementos')
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
            ListaException: Exceção lançada quando o argumento "chave"
                  não está presente na lista.

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            print (lst.elemento(40)) # exibe 4
        """
        
        for i in range(self.__final):
            if (self.__dado[i] == chave):
                return i+1
        raise ListaException(f'Chave {chave} nao esta na lista')


    def inserir(self, posicao:int, carga:any ):
        """ Método que adiciona um novo elemento à lista

        Args:
            posicao (int): um número correpondente à posição em que se deseja
                  inserir um novo valor
            carga (any): o conteúdo que deseja armazenar
                  na lista.

        Raises:
            ListaException: Exceção lançada quando uma posição inválida é
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
            assert posicao > 0 and posicao <= len(self)+1,"Posicao invalida para insercao"

            for i in range(self.__final, posicao-1, -1):
                self.__dado[i] = self.__dado[i-1]
            
            self.__dado[posicao-1] = carga
            self.__final += 1
        except AssertionError as ae:
            raise ListaException(ae.__str__())
        except TypeError:
            raise ListaException(f'O tipo de dado para posicao não é um número inteiro')
 

    def remover(self, posicao:int)->any:
        """ Método que remove um elemento da lista e devolve o conteudo
            existente na ordem indicada.

        Args:
            posicao (int): um número correpondente à ordem do elemento na lista
        
        Returns:
            qualquer tipo primitivo: o valor encontrado no elemento removido

        Raises:
            ListaException: Exceção lançada quando uma posição inválida é
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
            assert posicao > 0 and posicao <= len(self),f'Posicao invalida para remocao. Informe um numero de 1 a {self.__len__()}'

            carga = self.__dado[posicao-1]
            # Iniciando o deslocamento à esquerda dos elementos
            for i in range(posicao, self.__final):
                self.__dado[i-1] = self.__dado[i]

            self.__final -= 1
            return carga
        except TypeError:
            raise ListaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError as ae:
            raise ListaException(ae)
   

        
    def __str__(self)->str:
        s = '[ '
        if self.estaVazia():
            s+= ']'
            return s
        for i in range(self.__final):
            s += f'{self.__dado[i]}, '
        s = s[:-2] + " ]"
        return s
       

