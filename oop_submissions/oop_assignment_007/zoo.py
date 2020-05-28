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
        
    
#     # def make_sound(self):
#     #     print(self.sound)
    
#     # def breathe(self):
#     #     print(self.breathing)
    
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
    
#     #super().__init__(self,age_in_months,breed,required_food_in_kgs)
#     def __init__(self):
#         self._reserved_food_in_kgs=0
#         self._count_of_animals=[]
    
#     def add_food_to_reserve(self,quantity):
#         self._reserved_food_in_kgs += quantity

#     #@classmethod
#     def add_animal(self,item):
#         self._count_of_animals.append(item)
#         #self._reserved_food_in_kgs -= self.required_food_in_kgs
    
#     #@classmethod
#     def count_animals(self):
#         print(len(self._count_of_animals))
        
    
#     @property
#     def reserved_food_in_kgs(self):
#         return self._reserved_food_in_kgs
    
#     @property
#     def count_of_animals(self):
#         return self._count_of_animals   
 
# zoo = Zoo()
# print(zoo.reserved_food_in_kgs)
# zoo.add_food_to_reserve(10000000)
# print(zoo.reserved_food_in_kgs)
# print(zoo.count_animals())
# gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
# zoo.add_animal(gold_fish)
# zoo.count_animals()
# #print(zoo.count_of_animals)

    
    





class Deer:
    sound = "Buck Buck"
    breathing = "Breathe in air"
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        
        if age_in_months > 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:    
            self._age_in_months = age_in_months
        
        
        self._breed = breed
        #self.deer_count =0
        
        if required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs = required_food_in_kgs
    
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
    @classmethod
    def breathe(cls):
        print(cls.breathing)
    

    
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    def grow(self):
        self.age_in_months += 1
        self.required_food_in_kgs +=2
        
class Lion(Deer):
    sound = "Roar Roar"
    breathing = "Breathe in air"
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs +=4
    
class Shark(Deer):
    sound = "Shark Sound"
    breathing = "Breathe oxygen from water"
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs +=8

class GoldFish(Deer):
    sound = "Hum Hum"
    breathing = "Breathe oxygen from water"
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs +=0.2        
        
class Snake(Deer):
    sound = "Hiss Hiss"
    breathing = "Breathe in air"
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs +=0.5 
    


class Zoo:

    def __init__(self):
        self._reserved_food_in_kgs=0
        self._animal=[]
    
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    @property
    def animals(self):
        return self._animal  
    
    def add_food_to_reserve(self,quantity):
        self._reserved_food_in_kgs += quantity

    def add_animal(self,name):
        self._animal.append(name)

    
    def count_animals(self):
        return(len(self._animal))
        
    def feed(self,animal):
        if(self.reserved_food_in_kgs > 0):
            self._reserved_food_in_kgs -= animal._required_food_in_kgs
            animal.grow()


zoo = Zoo()
print(zoo.reserved_food_in_kgs)
zoo.add_food_to_reserve(10000000)
print(zoo.reserved_food_in_kgs)
print(zoo.count_animals())
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
zoo.count_animals()








































 