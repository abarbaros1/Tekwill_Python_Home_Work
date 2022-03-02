class Pet:

    def __init__(self,name:str, type:str, favourite_food:str):
        self.name = name
        self.type = type
        self.favourite_food = favourite_food

    def __str__(self):
        return f"{self.type} called {self.name} that loves {self.favourite_food}"
