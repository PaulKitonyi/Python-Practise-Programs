import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testing AnonymousSurvey class"""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question  = 'What is your best editor?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['VScode','Atom','Subl']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()