import math
fov = 50  # deg
# m_dist = 200 # m
dp = 37
width_of_object = 2.7  # m
image_height = 512
m_dist = width_of_object * image_height / 2 / math.tan(
    fov * math.pi / 180 / 2) / dp
print(m_dist)
