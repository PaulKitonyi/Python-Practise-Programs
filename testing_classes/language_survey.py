from survey import AnonymousSurvey

# Define a Question and make a survey
question = "What is your favourite programming language?"
my_survey = AnonymousSurvey(question)


# Show the question and Store responses to the question
print(my_survey.show_question())
print("Enter q to quit")
while True:
    inp = input("Enter your response:")
    if inp == "q":
        break
    my_survey.store_response(inp)

# Show the survey results
print("\n Thankyou for your response in the Survey!!!!")
my_survey.show_results()