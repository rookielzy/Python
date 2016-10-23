
def score(s):
    if (s >= 90 and s <= 100):
        return 'A'
    elif (s >= 80 and s <= 89):
        return 'B'
    elif (s >= 70 and s <= 79):
        return 'C'
    elif (s >= 60 and s <= 69):
        return 'D'
    elif (s < 60):
        return 'E'

while True:
    x = raw_input("Enter your Score: ")
    if x == 0:
        break
    else:
        score(x)