import unittest

class MyStack():

    stack = []

    def clear(self):
        self.stack = []

    def contains(self, element):
        return element in self.stack

    def push(self, element):
        return self.stack.append(element)

    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return self.stack == []


class TestMyStack(unittest.TestCase):

    def test_clear(self):
        my_stack = MyStack()
        my_stack.clear()
        self.assertEqual(my_stack.stack, [])

    def test_contain(self):
        my_stack = MyStack()
        my_stack.push(2)
        my_stack.push(3)
        my_stack.push(4)
        my_stack.push(5)
        self.assertTrue(my_stack.contains(4))
    
    def test_push(self):
        my_stack = MyStack()
        my_stack.push(2)
        self.assertEqual(my_stack.peek(), 2)

    def test_pop(self):
        my_stack = MyStack()
        my_stack.push(3)
        my_stack.push(4)
        my_stack.push(5)
        my_stack.pop()
        self.assertEqual(my_stack.peek(), 4)

    def test_peek(self):
        my_stack = MyStack()
        my_stack.push(6)
        my_stack.push(7)
        self.assertEqual(my_stack.peek(), 7)

    def test_isEmpty(self):
        my_stack = MyStack()
        self.assertEqual(my_stack.is_empty(), False)

if __name__ == '__main__':
    unittest.main()
