class Car:
    sound="Beep Beep"
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self._color = color
        if max_speed > 0:
            self._max_speed = max_speed
        else:
            raise ValueError("Invalid value for max_speed")
    
        if acceleration > 0:
            self._acceleration=acceleration
        else:
            raise ValueError("Invalid value for acceleration")
            
        if tyre_friction > 0:
            self._tyre_friction = tyre_friction
        else:
            raise ValueError("Invalid value for tyre_friction")
            
        self._current_speed = 0
        self._is_engine_started = False
        
        
        
    @property
    def color(self):
        return self._color
    
    @property
    def max_speed(self):
        return self._max_speed
    
    @property
    def current_speed(self):
        return self._current_speed
    
    @property
    def tyre_friction(self):
        return self._tyre_friction    
    
    @property
    def acceleration(self):
        return self._acceleration 
    
    @property
    def is_engine_started(self):
        return self._is_engine_started 

   
    def start_engine(self):
        self._is_engine_started = True
    
    def accelerate(self):
        if self._is_engine_started == True:
            if self._current_speed + self._acceleration <= self.max_speed:
                self._current_speed += self._acceleration
            else:
                self._current_speed=self._max_speed
        else:
            print("Start the engine to accelerate")
    
    def apply_brakes(self):
        if  self._is_engine_started == True and self._current_speed-self._tyre_friction > 0:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed =0
            
    def stop_engine(self):
        if self._is_engine_started == True:
            self._is_engine_started = False
    
   
   
   
    def sound_horn(self): 
        if self._is_engine_started == True:
            print(self.sound)
        else:
            print("Start the engine to sound_horn")
    
    
        
        
# car=Car(color="Red", max_speed = 250, acceleration = 10, tyre_friction = 3)
# car.start_engine()
# print(car.is_started)
# print(car.current_speed)
# car.accelerate()
# print(car.current_speed)
# car.apply_brakes()
# print(car.current_speed)
# car.horn()
# #print(car.sound_horn)
# car.stop_engine()
# print(car.is_started)
# car.current_speed=10
# print(car.current_speed)
