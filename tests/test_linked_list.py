"""
Тесты с использованием unittest для модуля linked_list.
"""

import unittest

"""
Импорт модуля, содержащего функции для тестирования
"""
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
	'''
	Класс для тестирования класса по работе со связанным списком
	'''
	
	def setUp(self) -> None:
		self.ll = LinkedList()
	
	def test_str(self):
		'''
		Тестируем формирование строки из списка: пустого и с одним элементом
		'''
		self.assertEqual(str(self.ll), 'None')
		self.ll.insert_beginning({'id': 1})
		self.assertEqual(str(self.ll), "{'id': 1} -> None")
	
	def test_insert_beginning(self):
		'''
		Тестируем вставку данных в начало
		'''
		self.ll.insert_beginning({'id': 0})
		self.assertEqual(str(self.ll), "{'id': 0} -> None")
	
	def test_insert_at_end(self):
		'''
		Тестируем вставку данных в конец и формирование строки
		'''
		self.ll.insert_at_end({'id': 2})
		self.assertEqual(str(self.ll), "{'id': 2} -> None")
		self.ll.insert_at_end({'id': 3})
		self.assertEqual(str(self.ll), "{'id': 2} -> {'id': 3} -> None")
		self.ll.insert_at_end({'id': 4})
		self.assertEqual(str(self.ll), "{'id': 2} -> {'id': 3} -> {'id': 4} -> None")
	
	def test_to_list(self):
		'''
		Тестируем превращение данных в список
		'''
		
		self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
		self.assertEqual(self.ll.to_list(), [{'id': 1, 'username': 'lazzy508509'}])
		self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
		self.assertEqual(self.ll.to_list(), [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}])

	def test_get_data_by_id(self):
		'''
		Тестирование получения данных по id
		'''
		
		self.assertEqual(self.ll.get_data_by_id(2), None)
		
		self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
		self.ll.insert_at_end('idusername')
		self.ll.insert_at_end([1, 2, 3])
		self.ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
		
		self.assertEqual(self.ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
		# with self.assertRaises(TypeError):
		# 	self.ll.get_data_by_id(2)
		
		self.assertEqual(self.ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})
