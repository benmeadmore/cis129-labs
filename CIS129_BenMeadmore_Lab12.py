# CIS129_BenMeadmore_Lab12.py

class Pet:
    # Constructor with default values
    def __init__(self, name="", type="", age=0):
        self.__name = name
        self.__type = type
        self.__age = age

    # Mutator methods
    def setName(self, name):
        self.__name = name

    def setType(self, type):
        self.__type = type

    def setAge(self, age):
        self.__age = age

    # Accessor methods
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age

# Main function
def main():
    # Prompt user input
    inputName = input("Enter your pet's name: ")
    inputType = input("Enter your pet's type: ")
    inputAge = int(input("Enter your pet's age: "))

    # Create Pet object
    Animal = Pet()
    Animal.setName(inputName)
    Animal.setType(inputType)
    Animal.setAge(inputAge)

    # Display pet data
    print("\nYour pet name:", Animal.getName())
    print("Your pet type:", Animal.getType())
    print("Your pet age:", Animal.getAge())

# Call main function
if __name__ == "__main__":
    main()
