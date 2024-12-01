from node import Node  # Importa a classe Node

class LinkedList:
    def __init__(self):  # Define a classe LinkedList
        self.head = None  # Define o nó inicial como vazio (lembre que Nó é um envelope)
        self.length = 0  # Define o tamanho da lista como 0

    def setHead(self, Node):
        self.head = Node
    
    def getHead(self):
        return self.head
    
    def insertAtBeginning(self, data):
        newNode = Node(data) # Cria um novo nó
        if self.length == 0: # Se o tamanho da lista for 0
            self.head = newNode
        else:
            newNode.next = self.head    # O campo next do novo nó recebe a cabeça da instância
            self.head = newNode         # A cabeça da instância, que estava vazia, recebe o novo nó.
        self.length += 1

    def insertAtEnd(self, data):        # Equivalente ao append
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
            self.length += 1
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        self.length += 1

    def insertAtGivenPosition(self, pos, data):     # Define a função insertAtGivenPosition
        if pos < 0 or pos > self.length + 1:                # Se a posição for menor que 0 ou maior que o tamanho da lista
            return "Posição inválida"                       # Retorna "Posição inválida"
        elif pos == 0:                              # Se a posição for 0
            self.insertAtBeginning(data)                # Chama a função insertAtBeginning
        elif pos == self.length - 1:                    # Se a posição for igual ao tamanho da lista
            self.insertAtEnd(data)                      # Chama a função insertAtEnd
        else:                                       # Se não
            newNode = Node(data)                        # Cria um novo nó com a data passada
            count = 0                                   # Define a variável count como 0
            current = self.head                         # Atribui a cabeça da lista à variável current
            while count < pos - 1:                      # Enquanto count for menor que a posição - 1
                current = current.next                      # O nó atual recebe o próximo nó
                count += 1                                  # Incrementa a variável count
            newNode.next = current.next                 # O próximo nó do novo nó recebe o próximo nó do nó atual
            current.next = newNode                      # O próximo nó do nó atual recebe o novo nó
            self.length += 1                            # Incrementa o tamanho da lista


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Fim da lista ligada")