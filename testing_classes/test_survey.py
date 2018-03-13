import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testing AnonymousSurvey class"""

    # def setUp(self):
    #     """Instantiate the class"""
    #     my_survey = AnonymousSurvey("What is your favourite progamming Lang?")

    # def test_show_question(self):
    #     """Testing the show question method"""
    #     result = AnonymousSurvey.show_question(my_survey)
    #     self.assertEqual(result,'What is your favourite progamming Lang?')

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question  = 'what is your favourite Computer language?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Python')

        self.assertIn('Python',my_survey.responses)

    def test_three_responses(self):
        """Test whether the function can correctly store 3 responses"""
        question  = 'What is your best editor?'
        my_survey = AnonymousSurvey(question)
        responses = ['VScode','Atom','Subl']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)

# unittest.main()