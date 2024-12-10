class Node:
    """Classe que representa um nó de uma árvore binária."""
    def __init__(self, data):
        self.data = data        # Criar um nó com um valor.
        self.left = None        # Nó à esquerda.
        self.right = None       # Nó à direita.
        self.father = None      # Nó pai.
        self.isLeft = False     # Indica se é um nó à esquerda.

    def setLeft(self, data):
        """Adiciona um nó à esquerda do nó atual."""
        self.left = Node(data)
        self.left.isLeft = True
        self.left.father = self

    def setRight(self, data):
        """Adiciona um nó à direita do nó atual."""
        self.right = Node(data)
        self.right.isLeft = False
        self.right.father = self

# Executar o exemplo somente se o arquivo for executado diretamente
if __name__ == "__main__":
    # Cria o nó raiz
    root = Node(1)

    # Nível 2
    root.setLeft(2)     # Filho à esquerda do nó raiz
    root.setRight(3)    # Filho à direita do nó raiz

    # Nível 3
    root.left.setLeft(4)   # Filho à esquerda do nó com valor 2
    root.left.setRight(5)  # Filho à direita do nó com valor 2
    root.right.setLeft(6)  # Filho à esquerda do nó com valor 3
    root.right.setRight(7) # Filho à direita do nó com valor 3

    # Nível 4
    root.left.left.setLeft(8)    # Filho à esquerda do nó com valor 4
    root.left.left.setRight(9)   # Filho à direita do nó com valor 4
    root.left.right.setLeft(10)  # Filho à esquerda do nó com valor 5
    root.left.right.setRight(11) # Filho à direita do nó com valor 5
    root.right.left.setLeft(12)  # Filho à esquerda do nó com valor 6
    root.right.left.setRight(13) # Filho à direita do nó com valor 6
    root.right.right.setLeft(14) # Filho à esquerda do nó com valor 7
    root.right.right.setRight(15) # Filho à direita do nó com valor 7

    # Exemplo de navegação
    print(root.data)               # Saída: 1
    print(root.left.data)          # Saída: 2
    print(root.right.data)         # Saída: 3
    print(root.left.left.right.data)  # Saída: 9

