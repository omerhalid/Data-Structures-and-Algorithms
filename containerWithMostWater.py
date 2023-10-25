#Container with most water
#Link: https://leetcode.com/problems/container-with-most-water/

# Description: Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
#              n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
#              Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

#              Notice that you may not slant the container.

#High level solution with 2 pointers:
# 1. Initialize two pointers, one at the beginning and one at the end of the array
# 2. Calculate the area between the two pointers
# 3. Move the pointer with the smaller height inwards
# 4. Repeat steps 2-3 until the pointers meet
# 5. Return the maximum area


def maxArea(height):
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = len(height) - 1
    # Initialize the max area
    max_area = 0
    # Iterate until the pointers meet
    while left < right:
        # Calculate the area between the two pointers
        area = min(height[left], height[right]) * (right - left)
        # Update the max area
        max_area = max(max_area, area)
        # Move the pointer with the smaller height inwards
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area
    