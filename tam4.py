import math

def euclidean_distance(a, b):
    """
    محاسبه فاصله اقلیدسی بین دو نقطه a و b در فضای دو بعدی.
    
    :param a: مختصات نقطه اول به صورت tuple (x1, y1)
    :param b: مختصات نقطه دوم به صورت tuple (x2, y2)
    :return: فاصله اقلیدسی بین دو نقطه
    """
    x1, y1 = a
    x2, y2 = b
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


point_a = (1, 2)
point_b = (4, 6)
print("فاصله اقلیدسی:", euclidean_distance(point_a, point_b))
