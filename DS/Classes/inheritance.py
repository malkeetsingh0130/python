import random
class Person:
    def __init__(self, firstname, lastname, health, status):
        """initializes attributes to be used in/available for all
        class methods in the class, and for class objects created
        by this class."""
        
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status
        """these are all the characteristics that each person will have
        in our prgoram. The reason for assiginign each of the characteristics
        to a name that includes self is so that they are accessible inside the 
        init method and other methods as well. Every method we have in the class
        will have self as the first argument"""
    
    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))
    
    def emote(self):
        emotion = random.randrange(1,3)
        if emotion==1:
            print('{} is happy today'.format(self.firstname))
        elif emotion ==2:
            print('{} is sad right now'.format(self.firstname))
    
    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >=75:
            print("{} is feeling tired today".format(self.firstname))
        elif self.health >= 50:
            print('{} person needs to go to the doctor'.format(self.firstname))
        else:
            print('{} person is unconsious.'.format(self.firstname))

Maria = Person("Maria", "Smith", 100, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 49, status=True)

class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon= weapon
    
    def hurt(self, other):
        if self.weapon== 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 20
        print(other.health)
    
    def insult(self, other):
        if other.health <=80:
            print("{} you are weak and tired".format(other.firstname))
        else:
            print("{} you are a worthy competitor".format(other.firstname))
    
    def steal(self,other):
        print("{} i have you stuff".format(other.firstname))
        if other.status == True:
            other.status == False

Alex = Enemy('rock', "Alex", "Wane", 99, status =False)

Alex.hurt(Maria)
Alex.insult(Maria)
Alex.insult(Lee)
Alex.steal(Rey)
