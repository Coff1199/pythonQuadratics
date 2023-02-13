import math
#class declaration
class quadratics:
  #class variable declarations
  a = None
  b = None
  c = None
  x = None
  discriminant = None
  numZeros = 0
  y = None
  #class constructor
  def __init__(self,a,b,c): 
    self.a = a
    self.b = b
    self.c = c
    
    if self.a == 0:
      print('Error:Function is not quadratic')
      exit(1)
    #x val of vertex as well as first half of quadratic equation
    self.x = (-1*self.b)/(2*self.a) #-2
    #discriminant/second half of quadratic equation
    self.discriminant = (((self.b**2)-(4*self.a*self.c)))/(2*self.a) #1
    if self.discriminant < 0:
      print('Error: this program in its current state does not account for imaginary numbers')
      exit(1)
    else:
      self.discrimnant=math.sqrt(self.discriminant)
      
  #calculates the vertex of the function
  def calculateVertex(self):
    self.y = ((self.a*(self.x**2))+(self.b*self.x) +self.c)
    print('The vertex is at ({0},{1})'.format(self.x,str(self.y))) #-2,-2
    
  #calculates y intercept of function
  def calculateYInt(self):
    self.y = ((self.a*(0**2))+(self.b*0) +self.c)
    print('The y intercept is at {' + str(0) + ',' + str(self.y) + '}') # 6
  
    #calculates x intercepts of function
  def calculateZeros(self):
    print('Zeros: ')
    if self.numZeros==0:
      print('None')
    else:
      print (self.x - self.discriminant)
      print(self.x + self.discriminant)
    
  #determines end behavior of function
  def determineEndBehavior(self):
    #postcondition:returns if the graph goes up or down  based on val of a
    if self.a > 0:
      print('The graph goes up')
    else:
      print('The graph goes down')
  
  #postcondition:use discriminant check for amount of zeroes
  def numOfZeroes(self):
    #postcondition:returns how many zeros the quadratic formula has based on the discriminant value
    if self.discriminant > 0:
      print('There are two real zeros(x intercepts)')
      self.numZeros = 2
    elif self.discriminant == 0:
      print('There is one real zero(x intercept)')
      self.numZeros = 1
    else:
      print('There are no real zeroes(x intercepts)')
      
