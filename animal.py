
class Animal:

    def __init__(self):
        self.color = ""
        self.name = ""
        self.type = ""
        pass    

    def run(self):
        print("Animal can run")
        pass

class Iflyable:
    def is_flyable(self):
        print("This animal can fly")
    pass

class Bird(Animal):
    def run(self):
        print("Bird cant Run")
    pass



class dog(Animal):
    def run(self):
        print("Dog can run")
    pass

class elephant(Animal):
    def run(self):
        print("elephant can run slow")
    pass

class flamingo(Animal, Iflyable):
    def run(self):
        return super().run()
    
    def is_flyable(self):
        return super().is_flyable()


class shaktiman(Animal):
    def run(self):
        return super().run()
    
        
obj = shaktiman()
obj.run()





#SOLID

# S - Single Responsility principle - function or class should have only one responsiblity related code
# O - Open/Close principle - Class or function should be Open for extention and close for modification
    #  
# L - Liscove substitution principe - child class should impliment all functions of parent class if not then 
    #create interfec for functionality which are not cinsumed by ckield class


