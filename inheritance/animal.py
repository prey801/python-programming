class Animal:
    def leg(self):
        print("I have 4 legs")
    def fur(self):
        print("my body is covered with fur")

class Dog(Animal):
    def bark(self):
        print("the dog bark")
class Cat(Animal):
    def meow(self):
        print("the cat meow")

#d=Dog()
#d.leg()
#d.fur()
#d.bark()
#cat metheod
c=Cat()
c.leg()
c.fur()
c.meow()

