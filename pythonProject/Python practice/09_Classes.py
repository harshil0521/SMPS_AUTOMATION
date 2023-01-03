class Dog:
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title(), 'is now sitting.')

    def roll_over(self):
        print(self.name.title(), "rolled over.")


my_dog = Dog('tiger', 7)
print("My dog's name is "+my_dog.name.title()+'.')
print('My dog is '+str(my_dog.age)+' years old.')

my_cat = Dog('kitty', 9)

my_dog.sit()
my_dog.roll_over()
my_cat.sit()


class Pet_Dog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)


my_pet = Pet_Dog('toy', 6)
print(my_pet.sit())
