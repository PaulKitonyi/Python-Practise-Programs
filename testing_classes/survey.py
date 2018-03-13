class AnonymousSurvey():
    """A class to collect anonymous answers to a survey Question"""

    def __init__(self, question):
        """Store a Question and prepare to store reponses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Display the Question"""
        return self.question

    def store_response(self, new_response):
        """Stores responses to Question"""
        self.responses.append(new_response)

    def show_results(self):
        """Displays the stored responses"""
        print('*'*5+ " printing responses in a while........ "+'*'*5 )
        for response in self.responses:
            print('*' + response)
