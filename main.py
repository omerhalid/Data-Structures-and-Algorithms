def linear_search(list, target):
    for num in range(0, len(list)):
        if target == list[num]:
            return num
    return None

list = [1,2,3,4,5,6]
target = 3

result = linear_search(list, target)

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target is not found in the list!")

verify(result)