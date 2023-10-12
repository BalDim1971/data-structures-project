"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""

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
		self.assertEqual(str(self.ll), 'None')
		self.ll.insert_beginning({'id': 1})
		self.assertEqual(str(self.ll), "{'id': 1} -> None")
	
	def test_insert_beginning(self):
		self.ll.insert_beginning({'id': 0})
		self.assertEqual(str(self.ll), "{'id': 0} -> None")
	
	def test_insert_at_end(self):
		self.ll.insert_at_end({'id': 2})
		self.assertEqual(str(self.ll), "{'id': 2} -> None")
		self.ll.insert_at_end({'id': 3})
		self.assertEqual(str(self.ll), "{'id': 2} -> {'id': 3} -> None")
		self.ll.insert_at_end({'id': 4})
		self.assertEqual(str(self.ll), "{'id': 2} -> {'id': 3} -> {'id': 4} -> None")
