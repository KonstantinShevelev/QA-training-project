class Bird:
    def fly(self):
        print("I'm flying")

class Penguin(Bird):
    def fly(self):
        print("I can't fly, I only can swim")

    def action(self):
        super().fly()
        print("I can't fly, I only can swim")

pingvi = Penguin()

#pingvi.fly()
pingvi.action()

