# Input: Array of buildings
#        { (1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25),
#          (19,18,22), (23,13,29), (24,4,28) }

# Output: Skyline (an array of rectangular strips)
#         A strip has x coordinate of left side and height 
#         (1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18),  
#         (22, 3), (25, 0)


def get_skyline(arr):
    skyline = []
    for startX, currY, endX in arr:
        skyline[-1]