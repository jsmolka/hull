import math


def knn(dataset, p, k):
    """Calculates k nearest neighbours for a given point"""
    return sorted(dataset, key=lambda x: math.sqrt((x[0] - p[0]) ** 2 + (x[1] - p[1]) ** 2))[0:k]


def intersects(p1, p2, p3, p4):
    """Checks if lines p1, p2 and p3, p4 intersect"""
    p0_x, p0_y = p1
    p1_x, p1_y = p2
    p2_x, p2_y = p3
    p3_x, p3_y = p4

    s10_x = p1_x - p0_x
    s10_y = p1_y - p0_y
    s32_x = p3_x - p2_x
    s32_y = p3_y - p2_y

    denom = s10_x * s32_y - s32_x * s10_y
    if denom == 0:
        return False

    denom_positive = denom > 0
    s02_x = p0_x - p2_x
    s02_y = p0_y - p2_y
    s_numer = s10_x * s02_y - s10_y * s02_x
    if (s_numer < 0) == denom_positive:
        return False

    t_numer = s32_x * s02_y - s32_y * s02_x
    if (t_numer < 0) == denom_positive:
        return False

    if ((s_numer > denom) == denom_positive) or ((t_numer > denom) == denom_positive):
        return False

    t = t_numer / denom
    x = p0_x + (t * s10_x)
    y = p0_y + (t * s10_y)

    if (x, y) in [p1, p2, p3, p4]:
        return False

    return True


def angle(p1, p2, previous_angle=0):
    """Calculates angle between two points and previous angle"""
    return (math.atan2(p1[1] - p2[1], p1[0] - p2[0]) - previous_angle) % (math.pi * 2) - math.pi


def point_in_polygon(point, polygon):
    """Checks if point is in polygon"""
    inside = False
    size = len(polygon)
    for i in range(0, size):
        min_ = min([polygon[i][0], polygon[(i + 1) % size][0]])
        max_ = max([polygon[i][0], polygon[(i + 1) % size][0]])
        if min_ < point[0] <= max_:
            p = polygon[i][1] - polygon[(i + 1) % size][1]
            q = polygon[i][0] - polygon[(i + 1) % size][0]
            point_y = (point[0] - polygon[i][0]) * p / q + polygon[i][1]
            if point_y < point[1]:
                inside = True
    return inside


def concave_hull(vector, k):
    """Calculates the concave hull for given points
    The dataset contains a list of points [(x, y), ...]
    k defines the number of of considered neighbours"""
    k = max(k, 3)  # Make sure k >= 3
    dataset = vector[:]
    if len(dataset) < 3:
        raise Exception("Dataset length cannot be smaller than 3")
    elif len(dataset) == 3:
        return dataset  # Points are a polygon already
    k = min(k, len(dataset) - 1)  # Make sure k neighbours can be found

    first_point = current_point = min(dataset, key=lambda x: x[1])
    hull = [first_point]  # Initialize hull with first point
    dataset.remove(first_point)  # Remove first point from dataset
    previous_angle = 0

    while (current_point != first_point or len(hull) == 1) and len(dataset) > 0:
        if len(hull) == 3:
            dataset.append(first_point)  # Add first point again
        kn_points = knn(dataset, current_point, k)  # Find nearest neighbours
        c_points = sorted(kn_points, key=lambda x: -angle(x, current_point, previous_angle))

        its = True
        i = -1
        while its and i < len(c_points) - 1:
            i += 1
            last_point = 1 if c_points[i] == first_point else 0
            j = 1
            its = False
            while not its and j < len(hull) - last_point:
                its = intersects(hull[-1], c_points[i], hull[-j - 1], hull[-j])
                j += 1
        if its:  # All points intersect, try again with higher number of neighbours
            return concave_hull(vector, k + 1)
        previous_angle = angle(c_points[i], current_point)
        current_point = c_points[i]
        hull.append(current_point)  # Valid candidate was found
        dataset.remove(current_point)

    for point in dataset:
        if not point_in_polygon(point, hull):
            return concave_hull(vector, k + 1)

    return hull
