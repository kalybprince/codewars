"""
You are given the length and width of a 
4-sided polygon. The polygon can either 
be a rectangle or a square.

If it is a square, return its area. 
If it is a rectangle, return its perimeter.

TEST:
Test.assert_equals(area_or_perimeter(4, 4), 16)
Test.assert_equals(area_or_perimeter(6, 10), 32)
"""

def area_or_perimeter(l , w):
    return l * w if l == w else (l + w) * 2
