from car import Car
class Truck(Car):
    sound="Honk Honk"
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._max_cargo_weight=max_cargo_weight
        self._weight=0
    
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight

    @property
    def weight(self):
        return self._weight
       
    def load(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed==0:    
            if self._weight+cargo_weight >= self._max_cargo_weight:
                print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                self._weight += cargo_weight
        else:
            print("Cannot load cargo during motion")   
       
    
    def unload(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed == 0:
            self._weight -= cargo_weight
        else:
            print("Cannot unload cargo during motion")   
       
    # def sound_horn(self):
    #     if self.is_engine_started:
    #         print("Honk Honk")
    #     else:
    #         print("Start the engine to sound_horn")












































# class Truck:
#     def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        
#         if max_speed > 0:
#             self._max_speed = max_speed
#         else:
#             raise ValueError("Invalid value for max_speed")
    
#         if acceleration > 0:
#             self._acceleration=acceleration
#         else:
#             raise ValueError("Invalid value for acceleration")
            
#         if tyre_friction > 0:
#             self._tyre_friction = tyre_friction
#         else:
#             raise ValueError("Invalid value for tyre_friction")
            
#         if max_cargo_weight > 0:
#             self._max_cargo_weight = max_cargo_weight
#         else:
#             raise ValueError("Invalid value for max_cargo_weight")
#         self._color=color
#         self._current_speed = 0
#         self._is_engine_started = False
#         self._weight=0
     
#     @property
#     def color(self):
#         return self._color
    
#     @property
#     def max_speed(self):
#         return self._max_speed
    
#     @property
#     def current_speed(self):
#         return self._current_speed
    
#     @property
#     def tyre_friction(self):
#         return self._tyre_friction    
    
#     @property
#     def acceleration(self):
#         return self._acceleration 
    
#     @property
#     def is_engine_started(self):
#         return self._is_engine_started 
        
#     @property
#     def weight(self):
#         return self._weight
    

   
#     def start_engine(self):
#         self._is_engine_started = True   
   
#     def accelerate(self):
#         if self._is_engine_started == True:
#             if self._current_speed + self._acceleration <= self._max_speed:
#                 self._current_speed += self._acceleration
#             else:
#                 self._current_speed=self._max_speed
#         else:
#             print("Start the engine to accelerate")


   
#     def load(self,cargo_weight):
#         if cargo_weight < 0:
#             raise ValueError("Invalid value for cargo_weight")
#         #if self.is_engine_started == True:
#         if self._current_speed==0:    
#             if self._weight+cargo_weight >= self._max_cargo_weight:
#                 print("Cannot load cargo more than max limit: ",self._max_cargo_weight)
#             else:
#                 self._weight += cargo_weight
#         else:
#             print("Cannot load cargo during motion")
            
#     def unload(self,cargo_weight):
#         if cargo_weight < 0:
#             raise ValueError("Invalid value for cargo_weight")
#         if self.is_engine_started == False:
#             if self._current_speed == 0:
#                 self._weight -= cargo_weight
#                 #print("Cannot load cargo more than max limit: ",self._max_cargo_weight)
#             # else:
#             #     self.weight -= cargo_weight
#         else:
#             print("Cannot unload cargo during motion")        
            
    
    
    
    
    
   
   
#     def sound_horn(self): 
#         if self._is_engine_started == True:
#             print("Honk Honk")
#         else:
#             print("Start the engine to sound_horn")
    
    
#     def apply_brakes(self):
#         if  self._is_engine_started == True and self._current_speed-self._tyre_friction > 0:
#             self._current_speed -= self._tyre_friction
#         else:
#             self._current_speed =0    
    
#     def stop_engine(self):
#         if self._is_engine_started == True and self.current_speed == 0:
#             self._is_engine_started = False
#             self.current_speed = 0
#         # elif self._current_speed > 0:
#         # elif  self._is_engine_started == True and self.current_speed > 0:  
#         #      self._is_engine_started = False
#         #      self.current_speed = 0
            





# #truck=Truck(color="Red", max_speed = 250, acceleration = 10, tyre_friction = 3,max_cargo_weight=100)
# # #truck.start_engine()
# # print(truck._is_engine_started)
# # print(truck._current_speed)
# # truck.load(10)
# # print(truck.loaded)
# # truck.unload(20)
# # print(truck.loaded)
# #truck.load(50)
# #print(truck.weight)
# #truck.load(50)
# ##print(truck.weight)

    