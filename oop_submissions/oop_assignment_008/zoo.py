class Animal:
    sound = "some sound"
    feed=0
    hunt_animal=""
    for_animal=""
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        
        if age_in_months > 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:    
            self._age_in_months = age_in_months
        
        self._breed = breed
        
        if required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs = required_food_in_kgs
    
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.feed


    def hunt(self,zoo):
        if self.hunt_animal in zoo.animal_list:
            zoo.animal_list.remove(self.hunt_animal)
            zoo.count_animals()
        else:
            print("No {} to hunt".format(self.for_animal))
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs


class LandAnimal:
    breathing = "Breathe in air"
    @classmethod
    def breathe(cls):
        print(cls.breathing)

class WaterAnimal:
    breathing = "Breathe oxygen from water"
    @classmethod
    def breathe(cls):
        print(cls.breathing)

class Deer(Animal,LandAnimal):
    sound = "Buck Buck"
    feed = 2
    name="Deer"

class Lion(Animal,LandAnimal):
    sound = "Roar Roar"
    feed = 4
    hunt_animal = "Deer"
    name= "Lion"
    for_animal="deers"
    

class Shark(Animal,WaterAnimal):
    sound = "Shark Sound"
    feed = 8 
    hunt_animal = "GoldFish"
    name= "Shark"
    for_animal="GoldFish"
    
class GoldFish(Animal,WaterAnimal):
    sound ="Hum Hum"
    feed = 0.2
    name="GoldFish"
    

class Snake(Animal,LandAnimal):
    sound = "Hiss Hiss"
    feed = 0.5 
    hunt_animal = "Deer"
    name= "Snake"
    for_animal="deers"

class Zoo:

    list_all=[]
    def __init__(self):
        self._reserved_food_in_kgs=0
        self.animal_list=[]
    
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    
    def add_food_to_reserve(self,quantity):
        self._reserved_food_in_kgs += quantity

    def add_animal(self,animal1):
        self.animal_list.append(animal1.name)
        self.list_all.append(animal1)

    
    def count_animals(self):
        return(len(self.animal_list))
        
    def feed(self,animal):
        if(self.reserved_food_in_kgs > 0):
            self._reserved_food_in_kgs -= animal._required_food_in_kgs
            animal.grow()

    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.list_all)
    
    @staticmethod
    def count_animals_in_given_zoos(zoo):
        count=0
        for park in zoo:
               count+=park.count_animals()
        return count











# shark = Shark(age_in_months=1, breed="ELK", required_food_in_kgs=10)
# print(shark.age_in_months)
# print(shark.breed)
# print(shark.required_food_in_kgs)
# shark.grow()
# print(shark.required_food_in_kgs)
# print(shark.age_in_months)
# shark.make_sound()
# shark.breathe()

    
    

























































# class Deer:
#     sound = "Buck Buck"
#     breathing = "Breathe in air"
#     def __init__(self,age_in_months, breed, required_food_in_kgs):
        
#         if age_in_months > 1:
#             raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
#         else:    
#             self._age_in_months = age_in_months
        
        
#         self._breed = breed
#         #self.deer_count =0
        
#         if required_food_in_kgs <= 0:
#             raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
#         else:
#             self._required_food_in_kgs = required_food_in_kgs
    
    
#     @classmethod
#     def make_sound(cls):
#         print(cls.sound)
    
#     @classmethod
#     def breathe(cls):
#         print(cls.breathing)
    

    
#     @property
#     def age_in_months(self):
#         return self._age_in_months
    
#     @property
#     def breed(self):
#         return self._breed
    
#     @property
#     def required_food_in_kgs(self):
#         return self._required_food_in_kgs
    
#     def grow(self):
#         self.age_in_months += 1
#         self.required_food_in_kgs +=2
        
# class Lion(Deer):
#     sound = "Roar Roar"
#     breathing = "Breathe in air"
        
#     def grow(self):
#         self._age_in_months += 1
#         self._required_food_in_kgs +=4
    
# class Shark(Deer):
#     sound = "Shark Sound"
#     breathing = "Breathe oxygen from water"
        
#     def grow(self):
#         self._age_in_months += 1
#         self._required_food_in_kgs +=8

# class GoldFish(Deer):
#     sound = "Hum Hum"
#     breathing = "Breathe oxygen from water"
        
#     def grow(self):
#         self._age_in_months += 1
#         self._required_food_in_kgs +=0.2        
        
# class Snake(Deer):
#     sound = "Hiss Hiss"
#     breathing = "Breathe in air"
        
#     def grow(self):
#         self._age_in_months += 1
#         self._required_food_in_kgs +=0.5 
    


# class Zoo:

#     def __init__(self):
#         self._reserved_food_in_kgs=0
#         self._animal=[]
    
    
#     @property
#     def reserved_food_in_kgs(self):
#         return self._reserved_food_in_kgs
    
#     @property
#     def animals(self):
#         return self._animal  
    
#     def add_food_to_reserve(self,quantity):
#         self._reserved_food_in_kgs += quantity

#     def add_animal(self,name):
#         self._animal.append(name)

    
#     def count_animals(self):
#         return(len(self._animal))
        
#     def feed(self,animal):
#         if(self.reserved_food_in_kgs > 0):
#             self._reserved_food_in_kgs -= animal._required_food_in_kgs
#             animal.grow()


# zoo = Zoo()
# print(zoo.reserved_food_in_kgs)
# zoo.add_food_to_reserve(10000000)
# print(zoo.reserved_food_in_kgs)
# print(zoo.count_animals())
# gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
# zoo.add_animal(gold_fish)
# zoo.count_animals()


