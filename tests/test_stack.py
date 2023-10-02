"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest

"""
Импорт модуля, содержащего функции для тестирования
"""
from src.stack import Stack

class TestStack(unittest.TestCase):
	'''
	Класс для тестирования класса по работе со стеком Stack
	'''
	
	def setUp(self) -> None:
		self.my_stack = Stack()
	def test_push(self):
		'''
		Проверяем добавление элемента
		'''
		self.my_stack.push('data1')
		self.assertEqual(self.my_stack.top.data, 'data1')
		self.my_stack.push('data2')
		self.assertEqual(self.my_stack.top.data, 'data2')
		self.assertEqual(self.my_stack.size, 2)
	
	def test_pop(self):
		'''
		Проверяем возврат и удаление элемента
		'''
		self.my_stack.push('data1')
		self.my_stack.push('data2')
		self.assertEqual(self.my_stack.pop(), 'data2')
		self.assertEqual(self.my_stack.size, 1)
		self.assertEqual(self.my_stack.pop(), 'data1')
		self.assertEqual(self.my_stack.size, 0)
		self.assertEqual(self.my_stack.pop(), None)
		
