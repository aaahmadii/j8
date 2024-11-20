import math

def are_collinear(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    return area == 0

def triangle_type(point1, point2, point3):
    if are_collinear(point1, point2, point3):
        return "نقاط همراستا هستند."
    AB = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    BC = math.sqrt((point3[0] - point2[0])**2 + (point3[1] - point2[1])**2)
    CA = math.sqrt((point1[0] - point3[0])**2 + (point1[1] - point3[1])**2)
    
    
    if AB == BC == CA:
        return "مثلث متساوی الاضلاع"
    elif AB == BC or BC == CA or CA == AB:
        return "مثلث متساوی الساقین"
    elif math.isclose(AB**2 + BC**2, CA**2) or math.isclose(BC**2 + CA**2, AB**2) or math.isclose(CA**2 + AB**2, BC**2):
         return "مثلث قائم الزاویه"
   

point_A = (0, 0)
point_B = (4, 0)
point_C = (0, 3)

result = triangle_type(point_A, point_B, point_C)
print(result)
