#Product of array except self
#Link: https://leetcode.com/problems/product-of-array-except-self/

#High level solution for the below code using postfix and prefix products:


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
    