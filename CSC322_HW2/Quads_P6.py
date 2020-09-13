import math

def quads(a, b, c): #insert coefficients

    d = b**2-4*a*c  #number of discriminant

    #d < 0: no roots
    #d = 0: 1 root
    #d > 0: 2 roots

    solution = []
    if d < 0:
        solution.append("0 solutions")
        print("No real solution")
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        print("One solution found: ", x)
        solution.append("1 solution")
        solution.append([x])
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        solution.append("2 solutions")
        if x1 > x2:
            solution.append([x2, x1])
            print ("Two solutions found: ", x2, " and", x1)
        else:
            solution.append([x1, x2])
            print ("Two solutions found: ", x1, " and", x2)

    return solution

#Example
print(quads(2, 6, 4))
