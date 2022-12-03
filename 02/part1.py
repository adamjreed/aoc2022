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
    round = line.strip().split(" ")
    round[1] = mapping[round[1]]

    total_score += moves[round[1]]["score"]

    #draw
    if round[0] == round[1]:
        total_score += 3
    #win
    elif round[0] in moves[round[1]]["wins"]:
        total_score += 6
    #lose is a no-op (0 points)

print(total_score)