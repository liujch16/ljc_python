import unittest
from name_function import get_formmateed_name

class NameTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):#测试方法名必须以test大头，这样才会在运行test_name_function时自动运行
        '''能够正确处理像Janis Joplin这样的姓名吗'''
        formatted_name = get_formmateed_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        '''能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗'''
        formatted_name = get_formmateed_name('Wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()