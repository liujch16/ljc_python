from survey import AnonymousSurvey

quetion = "What is your favorite language?"
my_survey = AnonymousSurvey(quetion)

my_survey.shoe_question()
print("Enter 'q' at any time to quit.\n")
while True:
    respone = input("Language: ")
    if respone == 'q':
        break
    my_survey.store_respone(respone)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()