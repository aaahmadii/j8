def are_collinear(point1, point2, point3):
    """
    Determine if three points are collinear in a 2D space.
    
    :param point1: Coordinates of the first point as a tuple (x1, y1)
    :param point2: Coordinates of the second point as a tuple (x2, y2)
    :param point3: Coordinates of the third point as a tuple (x3, y3)
    :return: True if the points are collinear, False otherwise
    """
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    
    
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    return area == 0


point_A = (1, 2)
point_B = (2, 4)
point_C = (3, 6)

if are_collinear(point_A, point_B, point_C):
    print("نقاط همراستا هستند.")
else:
    print("نقاط همراستا نیستند.")
