class User:
    """Model a user of a certain account"""
    def __init__(self, first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name  = last_name
        self.email      = email
        self.password   = password

    def describe_user(self):
        """Describing the user according to his/her details"""
        print("Your first name is {},your last name {},your email {} and your password {}Please keep them safe".format(self.first_name,self.last_name,self.email,self.password))

    def greet_user(self):
        """A method to greet the user"""
        print("Hello {} it was nice meeeting you....".format(self.first_name.title()))
        
user1 = User("paul","kitonyi","paulmucimah@gmail.com","password")
user1.describe_user()
user1.greet_user()