class Stack:
    def __init__(self):
        self.stack = []

    # Добавить элемент в стек
    def push(self, element):
        self.stack.append(element)

    # Удалить и вернуть верхний элемент стека
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None  # Если стек пуст

    # Посмотреть верхний элемент стека
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    # Проверить, пуст ли стек
    def is_empty(self):
        return len(self.stack) == 0

    # Возвращает размер стека
    def size(self):
        return len(self.stack)


# Пример использования стека
stack = Stack()

stack.push(10)
stack.push(20)
print(stack.peek())  # 20
print(stack.pop())  # 20
print(stack.size())  # 1
