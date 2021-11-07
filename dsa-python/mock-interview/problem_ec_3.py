"""
Problem
Given two rectangles, determine if they overlap. The rectangles are defined as a Dictionary, for example:

In [2]:
r1 = {

         # x and y coordinates of the bottom-left corner of the rectangle
         'x': 2 , 'y': 4,

         # Width and Height of rectangle
         'w':5,'h':12}
If the rectangles do overlap, return the dictionary which describes the overlapping section

Requirements
Make sure the dictionary you output is in the same form as the input.

Feel free to use an IDE for the code, but make sure you use paper/pencil or whiteboard to draw out your plan and logic
"""


def solution(r1, r2):
    r3 = None

    # check bottom left corner of r2 against r1
    if r2["x"] < r1["x"] + r1["w"] and r2["y"] < r1["y"] + r1["h"]:
        r3 = {
            "x": r2["x"],
            "y": r2["y"],
            "w": (r1["x"] + r1["w"]) - r2["x"],
            "h": (r1["y"] + r1["h"]) - r2["y"]
        }

    # check top left corner of r2 against r1

    # check top right corner of r2 against r1

    # check top bottom corner of r2 against r1

    # done
    return r3


r1 = {
     # x and y coordinates of the bottom-left corner of the rectangle
     'x': 2 , 'y': 4,
     # Width and Height of rectangle
     'w':5, 'h':12
}

r2 = {
     # x and y coordinates of the bottom-left corner of the rectangle
     'x': 5 , 'y': 14,
     # Width and Height of rectangle
     'w':5, 'h':6
}

result = solution(r1, r2)
print(result)
assert result["x"] == 5
assert result["y"] == 14
assert result["w"] == 2
assert result["h"] == 2
