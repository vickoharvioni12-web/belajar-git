class Animal:
    def speak(self):
        return "suara serigala dan ayam"

class serigala(Animal):
    def speak(self):
        return "auuuuuuuuuuuuuuuuuuuuuuu!"

class ayam(Animal):
    def speak(self):
        return "aaaaaaaaaaaaaaaaaaaaaaaa!"

animals = [serigala(), ayam(), Animal()]

for a in animals:
    print(a.speak())