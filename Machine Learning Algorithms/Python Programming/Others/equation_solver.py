import math

def solve_equation(a, b, c):
    """
    Solves a second degree equation of the form:
        
        a * x^2 + b * x + c = 0
    
    Returns the two possible solutions an equation may have.
    """
    # Your solution here
    # To compute a square root use math.sqrt(number)
    # To return two values from a function, you can separate them using a comma: return x1, x2
    if (b**2 - 4*a*c) > 0:
        if a != 0:
            print('Real and unique roots:')
            x1 = (-b + math.sqrt((b**2) - (4*a*c)))/(2*a)
            x2 = (-b - math.sqrt((b**2) - (4*a*c)))/(2*a)
            return x1,x2
        else:
            if b != 0:
                print("It's a linear equation with 1 root:")
                x = -c/b
                return x 
    elif (b^2 - 4*a*c) == 0:
        if a != 0:
            print('Real and equal roots:')
            x = -b/(2*a)
            return x
        else:
            print("It's a linear equation with 1 root:")
            x = -c/b
            return x            
    else:
        if b == 0 and c == 0:
            print('Real and equal roots:')
            return 0
        elif b == 0 and a == 0:
            print('Only constant value inserted')
            return
        else:
            print('Imaginary roots')
            return
 
# You can use the following examples to test your implementation
print(solve_equation(1, -1, -6))
print(solve_equation(3, 42, 39))
print(solve_equation(1,  0, -4))
print(solve_equation(1,  0,  0))
print(solve_equation(0,  1, -5))
print(solve_equation(1,  1,  1))
print(solve_equation(1, -4,  4))
print(solve_equation(0,  0,  4))
print(solve_equation(0,  4,  0))
print(solve_equation(4,  0,  0))
print(solve_equation(0,  0,  0))

    
