#find a way to graph
#test vals 2 8 6
print('Note: program does not work with decimals/rational values yet, only integers...')
s = input('Enter the quadratic formula(standard form ax^2+bx+c): ')
idx = s.index('x')
a = int(s[0:idx])
idx = s.find('x',idx+1)
b = int(s[s.index('x')+4:idx])
c = int(s[idx+2:])
#print(a,b,c)

#importing quadratics class from file
from quadratics import quadratics

#precondition:user has entered a,b, and c values of a quadratic equation
#postcondition:object of class quadratics created with values of abc and x as well as the discriminant value
q = quadratics(a,b,c)
#precondition:decared object of quadratics class and it was accepted as a quadratic equation, discriminant created
#postcondition:will determine how many zeros graph has
q.numOfZeroes()
#precondition:decared object of quadratics class and it was accepted as a quadratic equation
#postcondition:will calculate the x values of the equation
q.calculateZeros()
#precondition:decared object of quadratics class and it was accepted as a quadratic equation
#postcondition:will calculate the vertex of the equation
q.calculateVertex()
#precondition:decared object of quadratics class and it was accepted as a quadratic equation
#postcondition:will calculate the Y interecept of the equation
q.calculateYInt()
#precondition:decared object of quadratics class and it was accepted as a quadratic equation
#postcondition:will determine the end behavior of the graph
q.determineEndBehavior()
