###########################################################
# Классы для работы с очередью
###########################################################

class Node:
	"""Класс для узла очереди"""
	
	def __init__(self, data, next_node):
		"""
		Конструктор класса Node

		:param data: данные, которые будут храниться в узле
		"""
		
		self.data = data
		self.next_node = next_node


class Queue:
	"""Класс для очереди"""
	
	def __init__(self):
		"""
		Конструктор класса Queue
		head - первый элемент
		tail - последний элемент
		"""
		
		self.head = None
		self.tail = None
	
	def enqueue(self, data):
		"""
		Метод для добавления элемента в очередь

		:param data: данные, которые будут добавлены в очередь
		"""
		node = Node(data, None)
		
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			if self.tail == self.head:
				self.tail = node
				self.head.next_node = self.tail
			else:
				self.tail.next_node = node
				self.tail = node
	
	def dequeue(self):
		"""
		Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

		:return: данные удаленного элемента
		"""
		
		if self.head is None:
			return None
		
		node = self.head
		self.head = self.head.next_node
		return node.data
	
	def __str__(self) -> str:
		"""Магический метод для строкового представления объекта"""
		
		if self.tail is None or self.head is None:
			return ''
		else:
			prom = self.head
			my_str = ''
			while prom is not None:
				my_str += prom.data
				prom = prom.next_node
				if prom is not None:
					my_str += '\n'
			
			return my_str
