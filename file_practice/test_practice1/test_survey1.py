import unittest
from survey import AnonymousSurvey

class TsetAnonymousSurvey(unittest.TestCase):
    '''针对Anonymous类的测试'''

    def setUp(self):
        '''创建一个调查对象和一组答案，供使用的测试方法使用'''
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)#使用steUp()方法时只用创建一次实例
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        '''测试单个答案是否会被存储'''
        self.my_survey.store_respone(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        '''测试三个答案是否会被存储'''
        for response in self.responses:
            self.my_survey.store_respone(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.respenses)

unittest.main()