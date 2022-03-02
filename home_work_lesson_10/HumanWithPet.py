from Human import Human
from Pet import Pet

class HumanWithPet:

    def __init__(self, person:Human):
        self.person = person
        self.pets_list = list()

    def adopt_new_pet(self, new_pet:Pet):
        self.pets_list.append(new_pet)

    def give_away_pet(self, away_pet:Pet):
        self.pets_list.remove(away_pet)

    def get_list_of_pets(self):
        return self.pets_list

    def __str__(self):
        if len(self.pets_list) == 0:
            return f"{self.person.get_full_name()}, age {self.person.get_age()} with no pets"
        elif len(self.pets_list) == 1:
            return f"{self.person.get_full_name()}, age {self.person.get_age()} with a pet: {self.pets_list[0]}"
        else:
            return f"{self.person.get_full_name()}, age {self.person.get_age()} with {len(self.pets_list)} pets: {', '.join([str(pet) for pet in self.pets_list])}  "
