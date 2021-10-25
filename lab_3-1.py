# Author: MOG 10/25/21

import math
import time

thyme1_start = time.perf_counter()
math_pow = math.pow(2, 2)
thyme1_end = time.perf_counter()

thyme2_start = time.perf_counter()
math_reg = 2 ** 2
thyme2_end = time.perf_counter()

speed1 = thyme1_end - thyme1_start
speed2 = thyme2_end - thyme2_start

print(speed1)
print(speed2)
print(speed1 - speed2)