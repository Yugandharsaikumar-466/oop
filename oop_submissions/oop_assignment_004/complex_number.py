import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        
        if (type(real_part) == str and type(imaginary_part) == str):
             raise ValueError("Invalid value for real and imaginary part")            
        else:
             self.real_part=real_part
        
        if (type(real_part) != str):
            self.real_part=real_part
        else:
            raise ValueError("Invalid value for real part")
        
        if (type(imaginary_part) != str):
            self.imaginary_part=imaginary_part
        else:
            raise ValueError("Invalid value for imaginary part")
        
    # def __add__(self,other):
    #     return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
        
    def __add__(self,other):
        self.real_part=self.real_part+other.real_part
        self.imaginary_part=self.imaginary_part+other.imaginary_part
        return self     
    
    def __sub__(self,other):
        return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
        #self.real_part=abs(self.real_part-other.real_part)
        #self.imaginary_part=abs(self.imaginary_part-other.imaginary_part)
        #return self     
    
        
    def conjugate(self):
        
        return ComplexNumber(self.real_part,-self.imaginary_part)
    
    
    def __mul__(self,other):
        a=self.real_part*other.real_part-self.imaginary_part*other.imaginary_part
        
        b=self.imaginary_part*other.real_part+self.real_part*other.imaginary_part
        return ComplexNumber(a,b)
    
    def __eq__(self,other):
         return self.real_part==other.real_part and self.imaginary_part==other.imaginary_part

     
    def __abs__(self):
        
        a=math.sqrt(self.real_part**2 + self.imaginary_part**2)
        return (round(a,3))
    
    def __truediv__(self, other):
        sr, si, oim, oi = self.real_part, self.imaginary_part,other.real_part, other.imaginary_part 
        r = float(oim**2 + oi**2)
        return ComplexNumber((sr*oim+si*oi)/r, (si*oim-sr*oi)/r)

    
    def __str__(self):
        if self.imaginary_part>=0:
            return str(self.real_part)+'+'+str(self.imaginary_part)+'i'
        else:
            return str(self.real_part)+str(self.imaginary_part)+'i'



























# one_plus_two_i=ComplexNumber(1,2)    
# print(one_plus_two_i.real_part)
# print(one_plus_two_i.imaginary_part)
# one=ComplexNumber(1)
# print(one.real_part)
# print(one.imaginary_part)
# zero=ComplexNumber()
# print(zero.real_part)
#print(four_plus_six_i)
# one_plus_two_i = ComplexNumber(1,2)
# three_plus_four_i = ComplexNumber(3,4)
# four_plus_six_i = one_plus_two_i - three_plus_four_i
# print(four_plus_six_i)
# one_plus_two_i = ComplexNumber(1,2)
# one_minus_two_i = one_plus_two_i.conjugate()
# print(one_plus_two_i)
# one_plus_two_i = ComplexNumber(1,2)
# absolute_value = abs(one_plus_two_i)
# print(round(absolute_value,3))
one_plus_two_i = ComplexNumber(1,2)
three_plus_four_i = ComplexNumber(3,4)
point_four_four_plus_point_zero_eight_i = one_plus_two_i / three_plus_four_i
print(point_four_four_plus_point_zero_eight_i)