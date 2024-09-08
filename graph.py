class Graph:
    def __init__(self):
        self.graph = {}

    # Добавить вершину
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Добавить ребро между вершинами
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        # Если граф ненаправленный, добавить ребро в обратную сторону
        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)
        else:
            self.graph[vertex2] = [vertex1]

    # Обход графа в глубину (DFS)
    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Обход графа в ширину (BFS)
    def bfs(self, vertex):
        visited = set()
        queue = [vertex]
        visited.add(vertex)
        while queue:
            current = queue.pop(0)
            print(current, end=' ')
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# Пример использования графа
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print("DFS Traversal:")
g.dfs(1)  # 1 2 3
print("\nBFS Traversal:")
g.bfs(1)  # 1 2 3
