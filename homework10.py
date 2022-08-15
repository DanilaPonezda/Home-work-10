class Myself():
    def __init__(self, name, age, marry):
        self.name = name
        self.age = age
        self.marry = marry

    def myname(self, name):
        print(f"My name is {name}")

    def myage(self, age):
        print(f"I'm {age} y.o")

    def mymarry(self, marry):
        print(f"I am {marry}")

I = Myself("Danila", 15, "No merried")
I.myname("Danil")
I.myage("15")
I.mymarry("no merried")
