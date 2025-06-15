from django.test import TestCase

import unittest
from shop.queue import UniqueQueue

class TestQueue(TestCase):
    def test_init(self):
        queue = UniqueQueue()

    def test_add(self):
        queue = UniqueQueue()
        value = 1
        queue.add(value)

    def test_last(self):
        queue = UniqueQueue()
        value1 = 1
        value2 = 2
        queue.add(value1)
        queue.add(value2)
        self.assertEqual(queue.last(), value2)

    def test_length(self):
        queue = UniqueQueue()
        value1 = 1
        value2 = 1
        value3 = 2
        queue.add(value1)
        queue.add(value2)
        queue.add(value3)
        right_answer = 2
        self.assertEqual(queue.length(), right_answer)

    def test_empty(self):
        queue = UniqueQueue()
        empty = None
        self.assertEqual(queue.last(), empty)
