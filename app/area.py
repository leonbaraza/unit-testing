from math import pi

def area_of_circle(r):

    if type(r) not in [int, float]:
        raise TypeError('Value should be integer or float')

    if r<0:
        raise ValueError('Radius cannot be negative')

    return pi *(r**2)


# # test functions
# radii = [2, 0, -3, 2+5j, True,'radius']
# message = "Area of with radius {radius} is {area}"

# for r in radii:
#     A = area_of_circle(r)
#     print(message.format(radius=r,area=A))