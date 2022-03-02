class Pet:

    def __init__(self,name:str, type:str, favourite_food:str):
        pet_types_list = ['Dog', 'Cat', 'Bird']
        self.name = name
        self.favourite_food = favourite_food

        if type in pet_types_list:
            self.type = type
        else:
            self.type = 'Unknown type'

    def __str__(self):
        return f"{self.type} called {self.name} that loves {self.favourite_food}"

