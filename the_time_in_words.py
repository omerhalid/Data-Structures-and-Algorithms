#The time in words challenge from HackerRank
#https://www.hackerrank.com/challenges/the-time-in-words/problem

#High level solution:
# 1. Create a dictionary to map numbers to words
# 2. If the minutes are 0, return the hour + o'clock
# 3. If the minutes are 15, return quarter past + hour
# 4. If the minutes are 30, return half past + hour
# 5. If the minutes are 45, return quarter to + next hour
# 6. If the minutes are less than 30, return minutes + past + hour
# 7. If the minutes are more than 30, return minutes + to + next hour

def timeInWords(h, m):
    
    
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
               11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
               20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three',
               24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven',
               28: 'twenty eight', 29: 'twenty nine'}
               
    if m == 0:
        return numbers[h] + " o' clock"
    elif m == 15:
        return "quarter past " + numbers[h]
    elif m == 30:
        return "half past " + numbers[h]
    elif m == 45:
        return "quarter to " + numbers[(h % 12) + 1]  # Use modulo to handle hour rollover
    elif m == 1:
        return "one minute past " + numbers[h]
    elif m < 30:
        return numbers[m] + " minutes past " + numbers[h]
    elif m == 59:
        return "one minute to " + numbers[(h % 12) + 1]
    elif m > 30:
        return numbers[60 - m] + " minutes to " + numbers[(h % 12) + 1]  # Use modulo to handle hour rollover