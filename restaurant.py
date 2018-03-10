class Restaurant:
    """A simple attempt to model a restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type    = cuisine_type

    def describe_restaurant(self):
         """Describing the restaurant"""
         print("The restaurant name is {} and the cuisine type is {}".format(self.restaurant_name,self.cuisine_type))

    def open_restaurant(self):
        """Openning the restaurant"""
        print("The  restaurant is opened.")



restaurant = Restaurant('creamyinn','snacks')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)     
restaurant.describe_restaurant()
restaurant.open_restaurant()