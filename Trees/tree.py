from node import Node

class BinTree:
    """Classe que representa uma árvore binária."""
    def __init__(self, root=None):
        self.root = root

    def preOrder(self, root):
        """Realiza a travessia em pré-ordem (raiz, esquerda, direita)."""
        if root is None:
            return
        print(root.data, end=" --> ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        """Realiza a travessia em ordem (esquerda, raiz, direita)."""
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, end=" --> ")
        self.inOrder(root.right)

    def postOrder(self, root):
        """Realiza a travessia em pós-ordem (esquerda, direita, raiz)."""
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" --> ")


import random

def buildRandomTree(seed, size):
    """
    Constrói uma árvore binária aleatória com valores únicos.
    :param seed: Valor da raiz.
    :param size: Quantidade de nós na árvore.
    :return: Um objeto BinTree e o nó raiz.
    """
    root = Node(seed)
    bt = BinTree(root)
    i = 1

    while i < size:
        p = q = root
        number = random.randint(0, size * 40)
        # Busca pela posição para inserir o número.
        while number != p.data and q is not None:
            p = q
            q = p.left if number < p.data else p.right

        if number == p.data:  # Ignorar valores duplicados.
            continue
        elif number < p.data:
            p.setLeft(number)
        else:
            p.setRight(number)
        i += 1

    return bt, root


# EXEMPLO DE USO:
if __name__ == "__main__":
    # Construir uma árvore aleatória com 10 nós, raiz com valor 45.
    binary_tree, root = buildRandomTree(45, 10)

    print("\nTravessia em ordem (InOrder):")
    binary_tree.inOrder(root)

    print("\n\nTravessia em pré-ordem (PreOrder):")
    binary_tree.preOrder(root)

    print("\n\nTravessia em pós-ordem (PostOrder):")
    binary_tree.postOrder(root)
