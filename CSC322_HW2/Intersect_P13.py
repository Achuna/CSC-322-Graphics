import math

#a0 = (x1, y1)
#a1 = (x2, y2)
#b0 = (x3, y3)
#b1 = (x4, y4)

#If intersection cannot be computed the lines are parallel or do not touch
def testIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    try:
        intersectX = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                    (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        intersectY = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                    (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        result = "Intersection Exists at: ({x}, {y}) ".format(x=intersectX, y=intersectY)
        print(result)
        return True
    except:
        print("Lines do not intersect")
        return False

#test
print(testIntersect(0, 0, 5, 0, 2, 0, 2, 10))

print(testIntersect(0, 0, 5, 0, -1, 0, -2, 0))
