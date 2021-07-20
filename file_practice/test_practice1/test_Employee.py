import unittest
from Employee import Employee

class EmployeeTset(unittest.TestCase):

    def setUp(self):
        self.my_enter = Employee('Liu', 'Jin', 145000)

    def test_give_default_raise(self):
        '''测试默认的年薪增加值'''
        self.my_enter.give_raise()
        self.assertEqual(self.my_enter.payment, 150000)

    def test_give_custom_raise(self):
        '''测试传递一个实参'''
        self.my_enter.give_raise(9000)
        self.assertEqual(self.my_enter.payment, 154000)

unittest.main()
