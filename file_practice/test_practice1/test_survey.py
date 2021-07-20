import unittest
from survey import AnonymousSurvey

class TestAnonymousSUrvey(unittest.TestCase):
    '''针对Anonymous类的测试'''

    def test_store_single_response(self):
        '''测试单个答案会被存储'''
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)#创建实例
        my_survey.store_respone('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        '''测试三个答案会被妥善地存储'''
        question = "What is your favorite language?"
        my_survey = AnonymousSurvey(question)#创建实例
        responses = ['English', 'Spanish', 'Manarin']
        for respponse in responses:
            my_survey.store_respone(respponse)#调用store方法向my_survey实例的respone属性传递参数

        for respponse in responses:
            self.assertIn(respponse, my_survey.responses)#检查列表中是否有相应参数

unittest.main()
