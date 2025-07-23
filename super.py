class Animal:
    def _init_(self, name):
        self.name = name
        print(f"Animal created: {name}")

class Dog(Animal):
    def _init_(self, name, breed):
        super()._init_(name)
        print(f"Dog created: {name}, son of {breed}")

# Creating a Dog object
d = Dog("Sheru", "Dogesh")
