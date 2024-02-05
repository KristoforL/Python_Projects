#Creating a class for restaurants which will be used as the base for creating restaurants
class restaurant:
    """Creates restaurant"""

    def __init__(self, name, cuisine):
        """Initializes attributes"""
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    #Sets actions(functions) that can be done at a restaurant
    def describe(self):
        """Describes restaurant"""
        print(f"{self.name} serves {self.cuisine} cuisine")

    def open(self):
        """Opens restaurant"""
        print(f"{self.name} is open")

    def set_served(self, served):
        """Sets number served"""
        self.served = served

    def increment_served(self, served):
        """Increments number served"""
        self.served += served

#Inherits from the restaurant class and can also do wha the restaurant does along with the showing flavors
class icecream(restaurant):
    """Ice cream stand child of restaurant"""

    def __init__(self, name, cuisine='Ice Cream'):
        """inits attributes"""
        super().__init__(name, cuisine)
        self.flavors = []

    def show_flavors(self):
        """Shows all flavors"""
        print("Flavors available are:")
        for flavor in self.flavors:
            print(flavor)
