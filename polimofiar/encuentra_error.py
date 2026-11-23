class Animal:
    def hacer_sonido(self):
        return "Sonido general"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
    
perro = Perro()
print(perro. hacer_sonido())

