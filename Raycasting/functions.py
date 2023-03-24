import math

def calc_dist(frm, to):
    '''Function to calculate distance from one point to another'''
    return math.sqrt((frm[0] - to[0]) ** 2 + (frm[1] - to[1]) ** 2)

def rotate(origin, point, angle):
    '''Function to rotate a point around an origin (returns point x, y)'''
    length = calc_dist(origin, point)
    x = origin[0] + math.cos(math.radians(angle)) * length
    y = origin[1] + math.sin(math.radians(angle)) * length
    return (x, y)

def point_to_mouse(origin, mouse):
    '''Function to return angle from an origin point to mouse'''
    x = mouse[0] - origin[0]
    y = mouse[1] - origin[1]
    angle = (180 / math.pi) * math.atan2(y, x)
    return angle

def line_intersect(P0, P1, Q0, Q1):
    '''Function to check wheather line intersects with another line, returns x, y of intersection'''
    d = (P1[0]-P0[0]) * (Q1[1]-Q0[1]) + (P1[1]-P0[1]) * (Q0[0]-Q1[0]) 
    if d == 0:
        return None
    t = ((Q0[0]-P0[0]) * (Q1[1]-Q0[1]) + (Q0[1]-P0[1]) * (Q0[0]-Q1[0])) / d
    u = ((Q0[0]-P0[0]) * (P1[1]-P0[1]) + (Q0[1]-P0[1]) * (P0[0]-P1[0])) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        return round(P1[0] * t + P0[0] * (1-t)), round(P1[1] * t + P0[1] * (1-t))
    return None

def difference(n0, n1):
    return abs(n0-n1)

def limit(num, minimum, maximum):
    '''Function to limit a number between a minimum and maximum value'''
    return max(min(num, maximum), minimum)

def get_range(distance, angle):
    return distance * math.cos(angle)
