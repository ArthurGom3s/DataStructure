
```python
class Node:
    """Classe que representa um nó de uma árvore binária."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.father = None
        self.isLeft = False

```

---
---
# <center>**Inserir nó à esquerda (setLeft)**


O método setLeft da classe Node é responsável por adicionar um novo nó como filho à esquerda do nó atual. Aqui está uma explicação detalhada do método:

```python
def setLeft(self, data):
    """Adiciona um nó à esquerda do nó atual."""
    self.left = Node(data)
    self.left.isLeft = True
    self.left.father = self
```

- **`def setLeft(self, data):`**: Define o método setLeft, que aceita um parâmetro data.
- **`self.left = Node(data)`**: Cria um novo nó com o valor data e o define como o filho à esquerda do nó atual (self).
- **`self.left.isLeft = True`**: Define o atributo isLeft do novo nó como `True`, indicando que este nó é um filho à esquerda.
- **`self.left.father = self`**: Define o atributo father do novo nó como o nó atual (self), estabelecendo a relação pai-filho.

Este método permite adicionar um novo nó à esquerda do nó atual, configurando corretamente as referências de pai e filho e indicando que o novo nó é um filho à esquerda.

---
---

    def setRight(self, data):
        """Adiciona um nó à direita do nó atual."""
        self.right = Node(data)
        self.right.isLeft = False
        self.right.father = self




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
