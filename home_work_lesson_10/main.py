from Pet import Pet
from Human import Human
from HumanWithPet import HumanWithPet

pet1 = Pet("Garfield", "cat", "lasagna")
pet2 = Pet("Kuzea", "Dog", "bones")
my_human = Human("John", "Doe", "01/01/1998")

new_person_with_pets = HumanWithPet(my_human)
print(new_person_with_pets)

new_person_with_pets.adopt_new_pet(pet1)
print(new_person_with_pets)

new_person_with_pets.adopt_new_pet(pet2)
print(new_person_with_pets)

new_person_with_pets.give_away_pet(pet1)
print(new_person_with_pets)

