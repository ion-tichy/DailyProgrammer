import math

class Complex:
    def __init__(self,r,i):
        self.Real = r
        self.Imaginary = i
    
    def GetModulus(self):
        return math.sqrt(self.Real**2 + self.Imaginary**2) 
        
    def GetConjugate(self):
        return Complex(self.Real,-self.Imaginary)
        
    def GetArgument(self):
        return math.atan2(self.Imaginary,self.Real)
        
    @staticmethod
    def Add(x,y):
        return Complex(x.Real + y.Real, x.Imaginary + y.Imaginary)
    
    @staticmethod
    def Subtract(x,y):
        return Complex(x.Real - y.Real,x.Imaginary - y.Imaginary)
    
    @staticmethod    
    def Multiply(x,y):
        return Complex.Add( Complex(x.Real*y.Real,x.Real*y.Imaginary),
                            Complex(-x.Imaginary*y.Imaginary, x.Imaginary*y.Real) ) 
                            
    @staticmethod
    def Div(x,y):
       pass
        
    def __str__(self):
       return str(self.Real)+("+"if self.Imaginary >= 0 else "")+str(self.Imaginary)+"i"




if __name__ == "__main__":
    c1 = Complex(1,3)
    c2 = Complex(3,-2)
    
    print(c1,c2)
    
    c3 = Complex.Add(c1,c2)
    
    print(c3)
    
    print(c3.GetArgument())
    
    print("Complex modulus:",c3.GetModulus())
    print("Test: ", Complex.Multiply(c1,c2))