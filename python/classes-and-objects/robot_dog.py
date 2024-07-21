class Robot_Dog:

    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val
    
    def bark(self):
        print('Woof Woof!')


# Main Program
my_dog = Robot_Dog('Odis', 'Pug')
print (my_dog.name)
print (my_dog.breed)
my_dog.bark()


        