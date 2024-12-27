import numpy as np

class FilaError(Exception):
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
        dado (np.ndaary): um array para armazenamento sequencial dos elementos da
             fila
    """
    def __init__(self, tamanho = 10):
        """ Construtor padrão da classe Fila sem argumentos. Ao instanciar
            um objeto do tipo Fila, esta iniciará vazia. 
            Args:
            tamanho (int): um número inteiro que determina o tamanho máximo da fila. 
                           Se não for informado, o tamanho padrão será 10.
        """
        self.__dado = np.full(tamanho, None)
        self.__frente = 0
        self.__final = -1
        self.__tam = 0
 
    def estaVazia(self)->bool:
        """ Método que verifica se a fila está vazia ou não

        Returns:
            boolean: True se a fila estiver vazia, False caso contrário

        Examples:
            f = Fila()
            ...   # considere que temos internamente na fila frente->[10,20,30,40]
            if(f.estaVazia()): #
               # instrucoes
        """
        return self.__tam == 0 

    def estaCheia(self)->bool:
        """ Método que verifica se a fila está cheia ou não

        Returns:
            boolean: True se a fila estiver cheia, False caso contrário

        Examples:
            f = Fila()
            ...   # considere que temos internamente na fila frente->[10,20,30,40]
            if(f.estaCheia()): #
               # instrucoes
        """
        return self.__tam == len(self.__dado)

    def __len__(self)->int:
        """ Método que consulta a quantidade de elementos existentes na fila

        Returns:
            int: um número inteiro que determina o número de elementos existentes na fila

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila frente->[10,20,30,40]
            print (len(f)) # exibe 4
        """        
        return self.__tam


    def frente(self)->any:
        """ Método que recupera o conteudo armazenado no elemento da frente da fila,
            sem removê-lo.

        Returns:
            any: o conteudo armazenado na frente da fila (tipo primitivo ou objeto).

        Raises:
            FilaError: Exceção lançada quando a fila não possui elementos
        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila frente->[10,20,30,40]
            print (f.frente()) # exibe 10
        """
        if self.estaVazia():
            raise FilaError(f'Fila Vazia. Não há elemento a recuperar.')

        return self.__dado[self.__frente]

    
    def busca(self, key: any)->int:
        """ Método que recupera a posicao ordenada, dentro da fila, em que se
            encontra um valor chave passado como argumento. No caso de haver
            mais de uma ocorrência do valor, a primeira ocorrência será 
            retornada

        Args:
            key: um item de dado que deseja procurar na fila
        
        Returns:
            int: um número inteiro representando a posição, na fila, em que foi
                 encontrada a "chave" de busca.

        Raises:
            KeyError: Exceção lançada quando o argumento "key"
                  não está presente na fila.

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente->[10,20,30,40]
            print (f.busca(40)) # exibe 4
        """
        frente = self.__frente
        for i in range(1,self.__tam+1):
            if self.__dado[frente] == key:
                return i
            frente = (frente + 1)% len(self.__dado)
                
        raise KeyError(f'A chave {key} não está armazenado na fila')

    def get(self, posicao:int)->any:
        """ Método que recupera o conteudo armazenado em uma determinada posição
            da fila, sem removê-lo.

        Args:
            posicao(int): um número inteiro que determina a posição do elemento
                          que se deseja recuperar. A posição 1 refere-se ao 
                          elemento da frente da fila.

        Returns:
            any: o conteudo correspondente à posição indicada na fila.

        Raises:
            FilaError: Exceção lançada quando a posição não é válida para a fila atual
        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente->[10,20,30,40]
            print (f.get(3)) # retorna 30
        """
        try:
            assert posicao > 0 and posicao <= self.__tam
            frente = self.__frente
            for i in range(posicao-1):
                frente = (frente + 1) % len(self.__dado)

            return self.__dado[frente]
        except AssertionError:
            raise FilaError(f'Posicao inválida para a fila atual com {self.__tam} elementos')

    def enfileirar(self, valor:any ):
        """ Método que adiciona um novo elemento na frente da fila

        Args:
            valor(any): o conteúdo que deseja armazenar na fila.

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente-> [10,20,30,40]
            f.enfileirar(50)
            print(f)  # exibe [10,20,30,40,50]
        """
        if self.estaCheia():
            raise FilaError(f'Fila cheia. Não é possível inserir elementos')

        self.__tam +=1
        self.__final = (self.__final + 1) % len(self.__dado)
        self.__dado[ self.__final ] = valor
        


    def desenfileirar(self)->any:
        """ Método que remove um elemento da frente da fila e devolve o conteudo
            existente removido.
    
        Returns:
            qualquer tipo de dado: o conteúdo referente ao elemento removido

        Raises:
            FilaError: Exceção lançada quando se tenta remover algo de uma fila vazia
                    
        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente-> [10,20,30,40]
            dado = f.desenfileirar()
            print(f) # exibe [20,30,40]
            print(dado) # exibe 10
        """
        if self.estaVazia():
            raise FilaError(f'Fila Vazia. Não há elemento a remover.')

        carga = self.frente()
        self.__tam -= 1
        self.__frente = (self.__frente + 1)% len(self.__dado)

        return carga

        
    def __str__(self):
        """ Método que retorna uma string com a ordem dos elementos
            existentes na fila.
        """
        str = 'Frente-> [ '

        frente = self.__frente
        for _ in range(self.__tam):
            str += f'{self.__dado[frente]}, '
            frente = (frente + 1) % len(self.__dado)
        str = str.rstrip(', ')
        str += ' ]'
        return str

    def __iter__(self)->any:
        self.__index = 1
        self.__cursor = self.__frente
        return self
    
    def __next__(self)->any:
        if (self.__index > self.__tam):
            raise StopIteration
        else:
            carga = self.__dado[self.__cursor]
            self.__cursor = (self.__cursor + 1) % len(self.__dado)
            self.__index += 1
            return carga

    def __contains__(self, key:any)->bool:
        '''
        Método que verifica se uma chave está presente na fila.
        Acionado em situações de uso do operador "in": "if chave in fila".
        Argumentos:
            key(Any): chave do elemento a ser buscado.
        Retorna:
            bool: True se a chave estiver na fila e False caso contrário.
        '''
        try:
            self.busca(key)
            return True
        except KeyError:
            return False

    def __getitem__( self, posicao:int):
        return self.get(posicao)    