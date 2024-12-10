# <b>Respostas das questões 1, 2 e 3</b>

| **Tipo**           | **Descrição**                                                                                  |
|---------------------|----------------------------------------------------------------------------------------------|
| **Própria**         | Cada nó tem 0 ou exatamente 2 filhos.                                                        |
| **Cheia**           | Cada nó tem 0 ou 2 filhos, e todas as folhas estão no mesmo nível.                           |
| **Completa**        | Todos os níveis estão preenchidos (exceto possivelmente o último), e os nós no último nível estão alinhados da esquerda para a direita. |

<div style="text-align: center;">
    <img src="https://miro.medium.com/v2/resize:fit:4800/format:webp/1*CMGFtehu01ZEBgzHG71sMg.png" alt="Tipos de árvores binárias" />
</div>

# <b>4 - Qual é a altura máxima de uma árvore binária com n nós?</b>  
Isso ocorrerá quando tivermos uma árvore completamente degenerada e sua altur será (n-1).

# <b>5 - Qual é a altura mínima de uma árvore binária com n nós? Dica: procure sobre árvore perfeitamente balanceada.</b>


A altura mínima ocorre quando a árvore é **perfeitamente balanceada**. O número máximo de nós \( N \) para uma árvore de altura \( h \) é:

$$
N = 2^{h+1} - 1
$$

Para encontrar a altura \( h \) com base no número de nós \( n \):

$$
h_{\text{min}} = \lceil \log_2(n + 1) \rceil - 1
$$

### Exemplos

1. **Se \( n = 1 \):**

$$
h_{\text{min}} = \lceil \log_2(1 + 1) \rceil - 1 = \lceil \log_2(2) \rceil - 1 = 0
$$
Altura mínima: \( h = 0 \) (apenas a raiz).

2. **Se \( n = 7 \):**

$$
h_{\text{min}} = \lceil \log_2(7 + 1) \rceil - 1 = \lceil \log_2(8) \rceil - 1 = 3 - 1 = 2
$$

Árvore perfeitamente balanceada:
- Nível 0: 1 nó (raiz)
- Nível 1: 2 nós (filhos da raiz)
- Nível 2: 4 nós (folhas)  
Total de nós: \( 1 + 2 + 4 = 7 \).

3. **Se \( n = 15 \):**

$$
h_{\text{min}} = \lceil \log_2(15 + 1) \rceil - 1 = \lceil \log_2(16) \rceil - 1 = 4 - 1 = 3
$$
Altura mínima: \( h = 3 \).

#  6. Qual é o número máximo e mínimo de nós internos e externos de uma árvore binária imprópria?

Claro, aqui está a resposta resumida:

### Número Máximo e Mínimo de Nós Internos e Externos de uma Árvore Binária Imprópria

- **Número mínimo de nós internos**: \( n - 1 \) (onde \( n \) é o número total de nós, em uma árvore degenerada onde cada nó tem apenas um filho).
- **Número máximo de nós externos**: 1 (apenas uma folha, em uma árvore degenerada).

- **Número máximo de nós internos**: Aproximadamente n/2 (em uma árvore o mais balanceada possível, mas ainda imprópria).
- **Número mínimo de nós externos**: Aproximadamente n/2 (em uma árvore o mais balanceada possível, mas ainda imprópria).

# 7. Qual é o número mínimo de nós externos de uma árvore binária própria de altura h?

O número mínimo de nós externos (folhas) de uma árvore binária própria de altura \( h \) é 2. Isso ocorre quando a árvore é perfeitamente balanceada, ou seja, todos os níveis, exceto o último, estão completamente preenchidos, e o último nível tem o menor número possível de nós.

Para uma árvore binária própria de altura \( h \), o número mínimo de nós externos é dado por:

$$ \text{Número mínimo de nós externos} = 2 $$

Isso ocorre porque, em uma árvore binária própria, cada nó interno tem exatamente dois filhos, e a menor árvore própria possível com altura \( h \) terá dois nós externos no último nível.

# 8. Qual é o número máximo de nós externos de uma árvore binária própria de altura h?

O número máximo de nós externos (folhas) de uma árvore binária própria de altura \( h \) ocorre quando todos os níveis da árvore estão completamente preenchidos. Em uma árvore binária própria, cada nó interno tem exatamente dois filhos.

Para uma árvore binária própria de altura \( h \), o número máximo de nós externos é dado por:

$$ \text{Número máximo de nós externos} = 2^h $$

Isso ocorre porque, em uma árvore binária completa, o último nível (nível \( h \)) pode ter até \( 2^h \) nós.

# 9. O que é uma árvore binária balanceada? Dê um exemplo.

Uma árvore binária balanceada é uma árvore binária em que, para qualquer nó, a diferença entre os níveis (ou alturas) das suas subárvores esquerda e direita é no máximo 1.

<div style="text-align: center;">
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20240805164549/balance-vs-unbalance-binnary-tree.webp" alt="Tipos de árvores binárias" />
</div>


# 10. O que é uma árvore binária perfeitamente balanceada? 

Uma árvore binária perfeitamente balanceada é uma árvore binária em que todos os nós têm duas subárvores com alturas exatamente iguais ou diferindo em, no máximo, um nível.


# 11. Escreva algoritmos recursivos e não -recursivos para determinar:

**a. Número de nós em uma árvore binária**


```python
# Recursiva
def count_nodes_recursive(node):
    if node is None:
        return 0
    return 1 + count_nodes_recursive(node.left) + count_nodes_recursive(node.right)

#Iterativa
def count_nodes_iterative(root):
    if root is None:
        return 0
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        count += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return count
```

**b. Soma do conteúdo de todos os nós**
```python
#Recursivo
def sum_nodes_recursive(node):
    if node is None:
        return 0
    return node.value + sum_nodes_recursive(node.left) + sum_nodes_recursive(node.right)

#Não-recursivo:
def sum_nodes_iterative(root):
    if root is None:
        return 0
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        total += node.value
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return total
```

**c. Nível com maior soma**

```python

from collections import defaultdict

def level_sums_recursive(node, level=0, level_sums=None):
    if level_sums is None:
        level_sums = defaultdict(int)
    if node is None:
        return level_sums
    level_sums[level] += node.value
    level_sums_recursive(node.left, level + 1, level_sums)
    level_sums_recursive(node.right, level + 1, level_sums)
    return level_sums

def max_sum_level_recursive(root):
    level_sums = level_sums_recursive(root)
    return max(level_sums.items(), key=lambda x: x[1])  # Retorna (nível, soma)

#Não-recursivo:
def max_sum_level_iterative(root):
    if root is None:
        return None
    from collections import deque
    queue = deque([(root, 0)])
    level_sums = defaultdict(int)
    while queue:
        node, level = queue.popleft()
        level_sums[level] += node.value
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return max(level_sums.items(), key=lambda x: x[1])  # Retorna (nível, soma)
```

**d. Altura de uma árvore binária**

```python
#Recursivo
def height_recursive(node):
    if node is None:
        return -1  # Altura de uma árvore vazia é -1
    return 1 + max(height_recursive(node.left), height_recursive(node.right))

#Não-recursivo:
def height_iterative(root):
    if root is None:
        return -1
    from collections import deque
    queue = deque([(root, 0)])
    max_height = 0
    while queue:
        node, height = queue.popleft()
        max_height = max(max_height, height)
        if node.left:
            queue.append((node.left, height + 1))
        if node.right:
            queue.append((node.right, height + 1))
    return max_height
```
**e. Profundidade de uma árvore binária**

```python
#Recursiva
def depth_recursive(node, target, current_depth=0):
    if node is None:
        return -1  # Nó não encontrado
    if node == target:
        return current_depth
    left_depth = depth_recursive(node.left, target, current_depth + 1)
    if left_depth != -1:
        return left_depth
    return depth_recursive(node.right, target, current_depth + 1)

#Não-recursivo:
def depth_iterative(root, target):
    if root is None:
        return -1
    from collections import deque
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        if node == target:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return -1  # Nó não encontrado
```
