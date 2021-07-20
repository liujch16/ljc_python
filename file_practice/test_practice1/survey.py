class AnonymousSurvey():
    '''收集调查问卷'''
    def __init__(self, question):
        self.question = question
        self.responses = []

    def shoe_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_respone(self, new_response):
        '''存储单份调查问卷'''
        self.responses.append(new_response)

    def show_results(self):
        '''显示收到的所有问卷'''
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
            