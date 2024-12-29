import random

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"

class Dog(Pet):
    def __init__(self, name, age, breed, color):
        Pet.__init__(self, name, 'Dog', age)
        self.breed = breed
        self.color = color

    def display_info(self):
        return f"{Pet.display_info(self)}, Breed: {self.breed}, Color: {self.color}"

class Cat(Pet):
    def __init__(self, name, age, breed, color):
        Pet.__init__(self, name, 'Cat', age)
        self.breed = breed
        self.color = color

    def display_info(self):
        return f"{Pet.display_info(self)}, Breed: {self.breed}, Color: {self.color}"        
class PetAdoptionSystem:
    def __init__(self):
        self.pets = {} 
        self.pet_preferences = {
            'Dog': ("Bones", "Walk"),
            'Cat': ("Fish", "Nap")
        }

    def add_pet(self, pet):
        pet_id = random.randint(1000, 9999)
        while pet_id in self.pets:
            pet_id = random.randint(1000, 9999)
        self.pets[pet_id] = pet
        print(f"Pet added with ID: {pet_id}")

    def view_pets(self):
        if not self.pets:
            print("No pets available for adoption.")
        else:
            for pet_id, pet in self.pets.items():
                print(f"ID: {pet_id} - {pet.display_info()}")

    def adopt_pet(self, pet_id):
        if pet_id in self.pets:
            pet = self.pets.pop(pet_id)
            print(f"You have adopted {pet.name}.")
            print(f"Care Preferences: {self.pet_preferences[pet.species]}")
        else:
            print("Pet ID not found.")       
def main_menu():
    system = PetAdoptionSystem()
    
    while True:
        print("\nPet Adoption System ")
        print("1. Add Pet")
        print("2. View Pets")
        print("3. Adopt Pet")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            species = input("Enter species (Dog/Cat): ").capitalize()
            name = input("Enter name: ")
            age = input("Enter age: ")
            breed = input("Enter breed: ")
            color = input("Enter color: ")
            if species == 'Dog':
                pet = Dog(name, age, breed, color)
            elif species == 'Cat':
                pet = Cat(name, age, breed, color)
            else:
                print("Invalid species. Please enter 'Dog' or 'Cat'.")
                continue
            system.add_pet(pet)
        
        elif choice == '2':
            system.view_pets()
        
        elif choice == '3':
            pet_id = int(input("Enter pet ID to adopt: "))
            system.adopt_pet(pet_id)
        
        elif choice == '4':
            print("Thank you!")
            break
        
        else:
            print("Invalid choice.")

if name == "__main__":
    main_menu()