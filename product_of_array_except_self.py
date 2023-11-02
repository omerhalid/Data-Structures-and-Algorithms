#Product of array except self
#Link: https://leetcode.com/problems/product-of-array-except-self/

#High level solution for the below code using postfix and prefix products:
# 1. Create an array of the same length as nums
# 2. Iterate through nums and set the current index to the product of all elements before it
# 3. Iterate through nums backwards and set the current index to the product of all elements after it
# 4. Return the array

