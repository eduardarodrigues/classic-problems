# Eduarda Oliveira
# 2019-11-08
# the pi number

# the pi number is... well, you know, 3.14159265..., a constant 
# that is the ratio of the circumference of a circle and its 
# diameter. It can be calculated, for example, by using polygons 
# to approximate pi, as Archimedes did in ancient Greece. 
# Or we can just use infinite series - since mathematicians discovered 
# that there are exact formulas for calculating pi.  
# the most well-known way of calculating it is by using the
# Gregory-Leibniz Series:
# \pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13...

def calculate_pi(terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    sign: float = 1.0
    pi: float = 0
    for _ in range(terms):
        pi = pi + sign * (numerator/denominator)
        denominator = 2.0 + denominator
        sign = (-1.0) * sign 
    return pi

# and then we can just set how many terms we want to use for the
# calculation of pi. The highest the number of terms, the longer
# it will take, but the more precise our estimation of pi will be!
# take this fun fact: in March 2019, Emma Haruka Iwao, a
# computer scientist at Google, calculated the most accurate 
# value of pi ever calculated (with 31.4 trillion digits), using 
# 170 TB of data!

print(calculate_pi(100000))
