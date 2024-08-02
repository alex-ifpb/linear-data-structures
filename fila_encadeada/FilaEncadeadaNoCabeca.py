class FilaError(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos
       da fila é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self)->any:
        return self.__carga
    
    @property
    def prox(self)->'No':
        return self.__prox

    @carga.setter
    def carga(self, novaCarga:any):
        self.__carga = novaCarga

    @prox.setter
    def prox(self, novoProx:'No'):
        self.__prox = novoProx
    
    def __str__(self):
        return f'{self.__carga}'

class Head:
    """Classe que representa o nó cabeça (controle) da fila encadeada

     Attributes:
        inicio (No): apontador para o primeiro elemento da fila
        fim (No): apontador para o último elemento da fila
        tamanho (int): tamanho da fila
    """
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
class Fila:
    """Classe que implementa a estrutura de dados "Fila"
       utilizando a técnica de encadeamento com nó cabeça
       A classe permite que qualquer tipo de dado seja armazenada na fila.

     Attributes:
        head (Head): apontador para o objeto Head (nó cabeça), com inicio e fim 
        iguais a None e tamanho igual a zero
    """
    def __init__(self):
        """ Construtor padrão da classe Fila sem argumentos. Ao instanciar
            um objeto do tipo Fila, esta iniciará vazia. 
        """
        self.__head = Head()


    def estaVazia(self)->bool:
        """ Método que verifica se a fila está vazia.

        Returns:
            boolean: True se a fila estiver vazia, False caso contrário

        Examples:
            f = Fila()
            ...   # considere que temos internamente na fila frente->[10,20,30,40]
            if(f.estaVazia()): #
               # instrucoes
        """
        return self.__head.tamanho == 0

    def __len__(self)->int:
        """ Método que consulta a quantidade de elementos existentes na fila

        Returns:
            int: um número inteiro que determina o número de elementos existentes na fila

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila frente->[10,20,30,40]
            print (len(f)) # exibe 4
        """        
        return self.__head.tamanho

    def elementoDaFrente(self)->any:
        """ Método que recupera o conteudo armazenado no elemento da frente da fila,
            sem removê-lo.

        Returns:
            any: o conteudo armazenado na frente da fila (tipo primitivo ou objeto).

        Raises:
            FilaError: Exceção lançada quando a fila não possui elementos
        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila frente->[10,20,30,40]
            print (f.elementoDaFrente()) # exibe 10
        """
        if self.estaVazia():
            raise FilaError(f'Fila Vazia. Não há elemento a recuperar.')
        return self.__head.inicio.carga

    def busca(self, chave:any)->int:
        """ Método que recupera a posicao ordenada, dentro da fila, em que se
            encontra um valor chave passado como argumento. No caso de haver
            mais de uma ocorrência do valor, a primeira ocorrência será 
            retornada

        Args:
            key(any): um item de dado que deseja procurar na fila
        
        Returns:
            int: um número inteiro representando a posição, na fila, em que foi
                 encontrada a "chave" de busca.

        Raises:
            FilaError: Exceção lançada quando o argumento "key"
                  não está presente na fila.

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente->[10,20,30,40]
            print (f.busca(40)) # exibe 4
        """
        cursor = self.__head.inicio
        contador = 1

        while( cursor != None):
            if cursor.carga == chave:
                return contador           
            cursor = cursor.prox
            contador += 1

        raise FilaError(f'Chave {chave} inexistente na fila')

    def elemento(self, posicao:int)->any:
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
            print (f.elemento(3)) # retorna 30
        """
        try:
            if self.estaVazia():
                raise FilaError('Fila Vazia.')
            assert posicao > 0 and posicao <= len(self)
            cursor = self.__head.inicio
            contador = 1
            while(cursor != None and contador < posicao ):
                contador += 1
                cursor = cursor.prox

            return cursor.carga
            
        except TypeError:
            raise FilaError(f'A posicao referente ao elemento deve ser do tipo inteiro')
        except AssertionError:
            raise FilaError(f'Posicao invalida. Forneça um valor entre 1 e {self.__head.tamanho}.')
        except:
            raise

    def enfileirar(self, carga:any ):
        """ Método que adiciona um novo elemento na frente da fila

        Args:
            valor(any): o conteúdo que deseja armazenar na fila.

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente-> [10,20,30,40]
            f.enfileirar(50)
            print(f)  # exibe [10,20,30,40,50]
        """
        novo = No(carga)
        if self.estaVazia():
            self.__head.inicio = self.__head.fim = novo
        else:
            self.__head.fim.prox = novo
            self.__head.fim = novo
        self.__head.tamanho += 1


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
        try:
            assert not self.estaVazia()

            carga = self.__head.inicio.carga

            if self.__head.tamanho ==1:
                self.__head.fim = None

            self.__head.inicio = self.__head.inicio.prox
            self.__head.tamanho -= 1
            return carga
            
        except AssertionError as ae:
            raise FilaError(f'A fila está vazia! Não é possivel remover elementos')
                    
    def __str__(self):
        """ Método que retorna uma string com a ordem dos elementos
            existentes na fila.
        """
        s = 'frente->[ '
        cursor = self.__head.inicio
        while(cursor != None):
            s += f'{cursor.carga}, ' 
            cursor = cursor.prox
        return s[:-2] + " ]" if not self.estaVazia() else  s + ' ]'
       

