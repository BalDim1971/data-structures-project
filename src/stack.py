class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        
        self.size = 0
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        
        new_node = Node(data, self.top)
        
        self.top = new_node
        self.size += 1
       
    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        
        if self.size == 0 or self.top is None:
            return None
        
        result = self.top.data
        self.top = self.top.next_node
        self.size -= 1
        
        return result
        
