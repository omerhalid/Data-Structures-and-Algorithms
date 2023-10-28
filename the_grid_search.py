#COME BACK TO THIS PROBLEM

# The grid search hackerrank solution python
# Link: https://www.hackerrank.com/challenges/the-grid-search/problem

#High level solution for the below code:
# 1. Iterate through the main grid
# 2. For each cell, check if the pattern is found
    # The logic for checking if the pattern is found is as follows:
    # 1. Iterate through the pattern
    # 2. For each cell, check if the cell in the main grid matches
    # 3. If not, exit the inner loop
    # 4. If all cells in the pattern match, return True
# 3. If found, return "YES"
# 4. If not found, return "NO"


def gridSearch(G, P):
    # G is the 2D array for the main grid
    # P is the 2D array for the searched pattern
    
    for row_G in range(len(G) - len(P) + 1):
        for col_G in range(len(G[0]) - len(P[0]) + 1):
            
            pattern_found = True  # Assume pattern is found until proven otherwise
            
            for row_P in range(len(P)):
                for col_P in range(len(P[0])):
                    if G[row_G + row_P][col_G + col_P] != P[row_P][col_P]:
                        pattern_found = False
                        break
                if not pattern_found:  # If pattern not found in the inner loop, exit the outer loop
                    break

            if pattern_found:
                return "YES"

    return "NO"

