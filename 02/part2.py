import random

input = open('input.txt', 'r')
lines = input.readlines()

mapping = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

moves = {
    "A": {
        "wins": [
            "C"
        ],
        "loses": [
            "B"
        ],
        "score": 1
    },
    "B": {
        "wins": [
            "A"
        ],
        "loses": [
            "C"
        ],
        "score": 2
    },
    "C": {
        "wins": [
            "B"
        ],
        "loses": [
            "A"
        ],
        "score": 3
    }
}

total_score = 0

for line in lines:
    random.seed()
    round = line.strip().split(" ")

    #draw
    if round[1] == "Y":
        total_score += moves[round[0]]["score"] + 3
    #win
    elif round[1] == "Z":
        total_score += moves[moves[round[0]]["loses"][random.randrange(0, len(moves[round[0]]["loses"]))]]["score"] + 6
    #lose
    elif round[1] == "X":
        total_score += moves[moves[round[0]]["wins"][random.randrange(0, len(moves[round[0]]["wins"]))]]["score"]


print(total_score)