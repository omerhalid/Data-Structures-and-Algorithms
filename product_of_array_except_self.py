#Product of array except self
#Link: https://leetcode.com/problems/product-of-array-except-self/

#High level solution for the below code using postfix and prefix products:
# 1. Create an array of 1s with the same length as the input array
# 2. Set a prefix variable to 1
# 3. Iterate through the input array and set the current index of the answers array to the prefix variable
# 4. Multiply the prefix variable by the current element in the input array
# 5. Set a postfix variable to 1
# 6. Iterate through the input array backwards and multiply the current index of the answers array by the postfix variable
# 7. Multiply the postfix variable by the current element in the input array
# 8. Return the answers array


def productExceptSelf(nums):
    
    answers = [1] * len(nums)
    
    prefix = 1
    
    for i in range(len(nums)):
        answers[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    
    for i in range(len(nums) - 1, -1, -1):
        answers[i] *= postfix # we are multiplying the current answer(prefix values) by the postfix product
        postfix *= nums[i]
    
    return answers
    