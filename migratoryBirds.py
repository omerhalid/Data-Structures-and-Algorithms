#Migratory birds challenge from HackerRank
#https://www.hackerrank.com/challenges/migratory-birds/problem

#High level solution:
# 1. Count the birds with a list of size 6, where each index represents a bird type initially set to 0
# 2. Iterate through the array and increment the count of each bird type
# 3. Find the bird with maximum sightings
# 4. Return the index of the bird with maximum sightings


def migratoryBirds(arr):
    
    # Step 1: Count the birds
    counts = [0] * 6  # 0th index won't be used, as bird types start from 1.
    for bird in arr:
        counts[bird] += 1
        
    # Step 2: Find the bird with maximum sightings
    maxSightings = max(counts)
    return counts.index(maxSightings)