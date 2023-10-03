"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import unittest

"""
Импорт модуля, содержащего функции для тестирования
"""
from src.queue import Queue


class TestQueue(unittest.TestCase):
	'''
	Класс для тестирования класса по работе с очередью Queue
	'''
	
	def setUp(self) -> None:
		self.queue = Queue()
	
	def test_str(self):
		self.assertEqual(str(self.queue), '')
		self.queue.enqueue('data1')
		self.assertEqual(str(self.queue), 'data1')
		self.queue.enqueue('data2')
		self.assertEqual(str(self.queue), 'data1\ndata2')
		self.queue.enqueue('data3')
		self.assertEqual(str(self.queue), 'data1\ndata2\ndata3')

	def test_enqueue(self):
		self.queue.enqueue('data1')
		self.assertEqual(self.queue.tail.data, 'data1')
		self.assertEqual(self.queue.head.data, 'data1')
		self.queue.enqueue('data2')
		self.assertEqual(self.queue.tail.data, 'data2')
		self.assertEqual(self.queue.head.data, 'data1')
	
	def test_dequeue(self):
		self.assertEqual(self.queue.dequeue(), '')

