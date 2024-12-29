# Pet Adoption System

This Python application simulates a simple pet adoption system where users can add pets, view available pets, and adopt a pet based on a unique ID. The system supports two types of pets: Dogs and Cats.

## Features

1. **Add Pets**: Add new pets to the system by specifying details like name, species, age, breed, and color.
2. **View Pets**: Display a list of all available pets with their details and unique IDs.
3. **Adopt Pets**: Adopt a pet using its unique ID and receive care preferences for the adopted pet.

## Classes

### `Pet`
Base class representing a general pet.
- **Attributes**:
  - `name`: Name of the pet
  - `species`: Species of the pet (e.g., Dog, Cat)
  - `age`: Age of the pet
- **Method**:
  - `display_info()`: Returns a formatted string with pet details.

### `Dog` (inherits from `Pet`)
Represents a dog with additional attributes.
- **Additional Attributes**:
  - `breed`: Breed of the dog
  - `color`: Color of the dog

### `Cat` (inherits from `Pet`)
Represents a cat with additional attributes.
- **Additional Attributes**:
  - `breed`: Breed of the cat
  - `color`: Color of the cat

### `PetAdoptionSystem`
Manages the pet adoption process.
- **Attributes**:
  - `pets`: Dictionary to store pets with unique IDs
  - `pet_preferences`: Dictionary of care preferences for each species
- **Methods**:
  - `add_pet(pet)`: Adds a pet to the system with a unique ID
  - `view_pets()`: Displays all available pets
  - `adopt_pet(pet_id)`: Removes a pet from the system by ID and provides care preferences

## Usage

### Prerequisites
- Python 3.x installed on your system

### Running the Application
1. Save the code in a file named `pet_adoption_system.py`.
2. Run the application:
   ```bash
   python pet_adoption_system.py
   ```

### Menu Options
1. **Add Pet**: Enter details for a new pet to add it to the system.
2. **View Pets**: View a list of all available pets with their details.
3. **Adopt Pet**: Enter the unique ID of the pet you wish to adopt.
4. **Exit**: Close the application.

## Example Interaction
```
Pet Adoption System
1. Add Pet
2. View Pets
3. Adopt Pet
4. Exit
Enter your choice: 1
Enter species (Dog/Cat): Dog
Enter name: Max
Enter age: 3
Enter breed: Labrador
Enter color: Yellow
Pet added with ID: 1234

Pet Adoption System
1. Add Pet
2. View Pets
3. Adopt Pet
4. Exit
Enter your choice: 2
ID: 1234 - Name: Max, Species: Dog, Age: 3, Breed: Labrador, Color: Yellow

Pet Adoption System
1. Add Pet
2. View Pets
3. Adopt Pet
4. Exit
Enter your choice: 3
Enter pet ID to adopt: 1234
You have adopted Max.
Care Preferences: ('Bones', 'Walk')
