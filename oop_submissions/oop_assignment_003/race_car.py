# from car import Car
# import math
# class RaceCar(Car):
#     def __init__(self,color,max_speed,acceleration,tyre_friction):
#         super().__init__(color,max_speed,acceleration,tyre_friction)
#         self._nitro=0
#         self.a=10
    
#     @property
#     def nitro(self):
#         return self._nitro
    
    
#     def sound_horn(self):
#         if self.is_engine_started == True:
#             print("Peep Peep\nBeep Beep")
#         else:
#             print("Start the engine to sound_horn")

#     def accelerate(self):
#         if self._nitro > 0: 
#             if self._nitro < self._max_speed:
#                 self._current_speed += math.ceil((self._acceleration*30)/100)
#                 self._nitro -= 10
#             else:
#                 self._current_speed = self._max_speed
        
#         if self._is_engine_started == True:
#             if self._current_speed + self._acceleration <= self.max_speed:
#                 self._current_speed += self._acceleration
#                 # if self._nitro>0:
#                 #     self._nitro -= 10
#                 # else:
#                 #     pass
#             else:
#                 self._current_speed=self._max_speed
#         else:
#             print("Start the engine to accelerate")
    
    
#     def apply_brakes(self):
#         if self._current_speed >= (self._max_speed//2):
#             self._nitro +=10
#         if  self._is_engine_started == True and self._current_speed-self._tyre_friction > 0:
#             self._current_speed -= self._tyre_friction
#         else:    
#             self._current_speed =0
       
       
            
# v=RaceCar("Red",250,50,30)
# v.start_engine()
# v.accelerate()
# v.accelerate()
# v.accelerate()
# print(v.current_speed)
# #v.accelerate()
# v.apply_brakes()
# print(v.current_speed)
# print(v.nitro)
# #print(v.nitro)
# v.accelerate()
# print(v.current_speed)
# print(v.nitro)

from car import Car
import math
class RaceCar(Car):
    sound="Peep Peep\nBeep Beep"
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro=0
    
    @property
    def nitro(self):
        return self._nitro
    
    # def sound_horn(self):
    #     if self.is_engine_started == True:
    #         print("Peep Peep\nBeep Beep")
    #     else:
    #         print("Start the engine to sound_horn")

    def accelerate(self):
        if self._nitro > 0: 
           if self._nitro < self._max_speed:
                self._current_speed += math.ceil((self._acceleration*30)/100)
                self._nitro -= 10
        super().accelerate()    
    
    def apply_brakes(self):
        if self._current_speed >= (self._max_speed//2):
            self._nitro +=10
        super().apply_brakes()
       
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
            
            
            
            