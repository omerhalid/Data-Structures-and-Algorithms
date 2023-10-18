#Climbing the Leaderboard from HackerRank
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

# input example:
# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120

# output example:
# 6
# 4
# 2
# 1

# High level solution with stack and reverse sorted set:
# 1. Create a stack of scores
# 2. Create a reverse sorted set of scores
# 3. Iterate through the list of alice's scores
# 4. While the alice's score is greater than the top of the stack, pop the stack and the sorted set
# 5. Append the length of the sorted set + 1 to the result list
# 6. Return the result list

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    # we will use stack
    
    # we need a sorted set because set consists unique numbers
    
    sorted_set_ranked = sorted(set(ranked), reverse=True)
    
    result = []
    
    for player_score in player:
        while len(sorted_set_ranked) != 0 and player_score >= sorted_set_ranked[-1]:
            sorted_set_ranked.pop()
        
        result.append(len(sorted_set_ranked)+1)
    
    return result