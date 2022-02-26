totalScore1, totalScore2, maxLead = 0, 0, 0
player = None
for _ in range(int(input())):
    score1, score2 = list(map(int, input().split(' ')))
    totalScore1 += score1
    totalScore2 += score2

    if totalScore1 > totalScore2:
        if maxLead < totalScore1 - totalScore2:
            maxLead = totalScore1 - totalScore2
            player = 1
    elif totalScore1 < totalScore2:
        if maxLead < totalScore2 - totalScore1:
            maxLead = totalScore2 - totalScore1
            player = 2
print(player, maxLead)
