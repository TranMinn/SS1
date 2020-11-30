import math
def distance(firstPoint, secondPoint):
    lat1, long1 = firstPoint
    lat2, long2 = secondPoint
    radius = 6371

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    long1 = math.radians(long1)
    long2 = math.radians(long2)

    a = math.sin((lat2 - lat1)/2) * math.sin((lat2 - lat1)/2)+ math.cos(lat1) * math.cos(lat2) * math.sin((long2 - long1)/2) * math.sin((long2 - long1)/2)

    c = 2 * math.asin(math.sqrt(a))

    d = radius * c

    return d

if __name__ == '__main__':
    pointA = (35.28, -120.65)
    pointB = (46.60, -112.04)

    print("The distance is: ", distance(pointA, pointB))