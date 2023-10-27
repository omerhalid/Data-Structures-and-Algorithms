#Flatland space stations from hackerrank.com
#Link: https://www.hackerrank.com/challenges/flatland-space-stations/problem

# 2 different solutions: optimized and brute force
# 1. Optimized solution:
#     # If every city has a space station, the result is obviously 0.
#     # Sort the space stations.
#     # The maximum distance will be the maximum of:
#         # Distance from the first city to the first space station.
#         # Distance from the last city to the last space station.
#         # Half of the maximum distance between two consecutive space stations.
# 2. Brute force solution:
#     # This will store the maximum distance encountered
#     # Start with a large distance (maximum possible is n)
#     # Calculate the distance between the current planet and the station
#     # Update current_dist if a closer station is found
#     # If a space station exists in the current city, no need to check other space stations.
#     # Update maxDist if required


#Optimized solution
def flatlandSpaceStations(n, c):
    # If every city has a space station, the result is obviously 0.
    if n == len(c):
        return 0

    # Sort the space stations.
    c.sort()

    # The maximum distance will be the maximum of:
    # 1. Distance from the first city to the first space station.
    # 2. Distance from the last city to the last space station.
    # 3. Half of the maximum distance between two consecutive space stations.
    maxDist = max(c[0], n - 1 - c[-1])

    for i in range(1, len(c)):
        maxDist = max(maxDist, (c[i] - c[i-1]) // 2)

    return maxDist

# Test the function
print(flatlandSpaceStations(5, [0, 4]))  # Expected output: 2



#Brute force solution
def flatlandSpaceStations(n, c):
    
    if n == len(c):
        return 0
        
    maxDist = 0  # This will store the maximum distance encountered
    
    for planet in range(n):
        current_dist = n  # Start with a large distance (maximum possible is n)

        for station in c:
            # Calculate the distance between the current planet and the station
            difference = abs(planet - station)

            # Update current_dist if a closer station is found
            if difference < current_dist:
                current_dist = difference

            # If a space station exists in the current city, no need to check other space stations.
            if difference == 0:
                break

        # Update maxDist if required
        if current_dist > maxDist:
            maxDist = current_dist

    return maxDist