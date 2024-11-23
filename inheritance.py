class Mammal:
    def walk(self):
        print("Walk")
class Dog(Mammal):
    def bark(self):
        print("Bark")
class Cat(Mammal):
    #Below line is to make an empty class not-empty
    pass  

dog1 = Dog()
dog1.bark()
dog1.walk()

cat1 = Cat()
cat1.walk()

