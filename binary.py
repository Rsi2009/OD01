class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self):
        self.root = None

    # Вставка нового узла в дерево
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    # Рекурсивная вставка узла
    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    # Поиск узла
    def search(self, key):
        return self._search(self.root, key)

    # Рекурсивный поиск узла
    def _search(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # Прямой обход (Preorder Traversal)
    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    # Симметричный обход (Inorder Traversal)
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    # Обратный обход (Postorder Traversal)
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')


# Пример использования бинарного дерева
bt = BinaryTree()
bt.insert(10)
bt.insert(20)
bt.insert(5)
bt.insert(15)

print("Preorder Traversal:")
bt.preorder_traversal(bt.root)  # 10 5 20 15
print("\nInorder Traversal:")
bt.inorder_traversal(bt.root)  # 5 10 15 20
print("\nPostorder Traversal:")
bt.postorder_traversal(bt.root)  # 5 15 20 10
