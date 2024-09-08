class Queue:
    def __init__(self):
        self.queue = []

    # Добавить элемент в очередь
    def enqueue(self, element):
        self.queue.append(element)

    # Удалить и вернуть первый элемент очереди
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None  # Если очередь пуста

    # Посмотреть первый элемент очереди
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    # Проверить, пуста ли очередь
    def is_empty(self):
        return len(self.queue) == 0

    # Возвращает размер очереди
    def size(self):
        return len(self.queue)


# Пример использования очереди
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.peek())  # 10
print(queue.dequeue())  # 10
print(queue.size())  # 1
