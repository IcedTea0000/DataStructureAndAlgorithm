import math

def areas(r, a):
    """
    :param r: (float) The radius of the circle.
    :param a: (float) The angle of the segment.
    :returns: (list) (A list of two elements containing the area inside, and area outside the circle, in that order.)
    """
    circle_area = math.pi * r **2
    segment_area = (r**2)/2*(a * math.pi/180 - math.sin(a*math.pi/180))
    result = [circle_area, segment_area]
    return result

print(areas(10, 90))