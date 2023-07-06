string1 = "car"
string2 = "rac"


def validAnagram(string1, string2):
    sortedString1 = sorted(string1)
    sortedString2 = sorted(string2)

    print(sortedString1)
    print(sortedString2)

    if sortedString1 == sortedString2:
        print("True")
        
validAnagram(string1, string2)
