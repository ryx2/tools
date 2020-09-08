import math
fov = 50 # deg
m_dist = 100 # m
width_of_object = 2.7 # m
image_height = 512
dp = width_of_object * image_height / 2 / math.tan(fov * math.pi / 180 / 2) / m_dist
print(dp)
