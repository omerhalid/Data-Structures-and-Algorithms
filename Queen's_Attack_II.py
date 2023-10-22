#Queen's Attack II
#https://www.hackerrank.com/challenges/queens-attack-2/problem

#Problem statement:

#You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.


#High level solution:


def queensAttack(n, k, r_q, c_q, obstacles):
    dU = n - r_q
    dD = r_q - 1
    dL = c_q - 1
    dR = n - c_q
    dRU = min(dR, dU)
    dLU = min(dL, dU)
    dRD = min(dR, dD)
    dLD = min(dL, dD)
    
    for obs in obstacles:
        if obs[1] == c_q:  # Obstacle is vertical
            if obs[0] > r_q:  # Obstacle is above
                dU = min(dU, obs[0] - r_q - 1)
            else:  # Obstacle is below
                dD = min(dD, r_q - obs[0] - 1)
        elif obs[0] == r_q:  # Obstacle is horizontal
            if obs[1] > c_q:  # Obstacle is to the right
                dR = min(dR, obs[1] - c_q - 1)
            else:  # Obstacle is to the left
                dL = min(dL, c_q - obs[1] - 1)
        elif abs(obs[0] - r_q) == abs(obs[1] - c_q):  # Obstacle is diagonal
            if obs[0] > r_q:
                if obs[1] > c_q:  # Obstacle is right up
                    dRU = min(dRU, obs[1] - c_q - 1)
                else:  # Obstacle is left up
                    dLU = min(dLU, c_q - obs[1] - 1)
            else:
                if obs[1] > c_q:  # Obstacle is right down
                    dRD = min(dRD, obs[1] - c_q - 1)
                else:  # Obstacle is left down
                    dLD = min(dLD, c_q - obs[1] - 1)
    
    return dU + dD + dL + dR + dRU + dLU + dRD + dLD
