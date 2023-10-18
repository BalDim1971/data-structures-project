class Node:
	"""Класс для узла односвязного списка"""
	
	def __init__(self, data, next_node):
		"""
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
		
		self.data = data
		self.next_node = next_node


class LinkedList:
	"""Класс для односвязного списка"""
	
	def __init__(self):
		'''
        Инициируем список
        '''
		self.head = None
	
	def insert_beginning(self, data: dict) -> None:
		"""Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
		
		node = Node(data, self.head)
		self.head = node
	
	def insert_at_end(self, data: dict) -> None:
		'''
		Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка
		'''
		
		if self.head is None:
			self.head = Node(data, None)
			return
		
		node = self.head
		while node.next_node:
			node = node.next_node
		node.next_node = Node(data, None)
	
	def __str__(self) -> str:
		'''
		Вывод данных односвязного списка в строковом представлении.
		'''
		
		node = self.head
		
		ll_string = ''
		while node:
			ll_string += f'{str(node.data)} -> '
			node = node.next_node
		
		ll_string += 'None'
		return ll_string
	
	def to_list(self) -> list:
		'''
		Возвращает список с данными, содержащимися в односвязном списке.
		'''
		
		my_list = []
		node = self.head
		
		while node:
			my_list.append(node.data)
			node = node.next_node
		
		return my_list
	
	def get_data_by_id(self, id: int):
		'''
		Возвращает первый найденный в `LinkedList` словарь с ключом 'id'.
		'''
		
		node = self.head
		while node:
			try:
				if int(node.data['id']) == id:
					return node.data
			except TypeError:
				print('Данные не являются словарем или в словаре нет id')
			
			node = node.next_node
		
		return None

