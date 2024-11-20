import math

def calculate_distance(point):
    """محاسبه فاصله یک نقطه از مرکز (0, 0)"""
    return math.sqrt(point[0]**2 + point[1]**2)

def sort_points_by_distance(points):
    """مرتب کردن نقاط بر اساس فاصله آن‌ها از مرکز"""
    sorted_points = sorted(points, key=calculate_distance)
    return sorted_points

points = [(3, 4), (1, 1), (0, 2), (5, 5), (-1, -1)]
sorted_points = sort_points_by_distance(points)

print("نقاط مرتب شده بر اساس فاصله از مرکز:")
for point in sorted_points:
    distance = calculate_distance(point)
    print(f"نقطه: {point}, فاصله از مرکز: {distance:.2f}")
