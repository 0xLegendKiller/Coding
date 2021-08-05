# Question:
'''
A 100m running match is played between 8 players and their time was noted in seconds.

Now if match is to be played between 3 players in one round, what will be sum of minimum times from all the rounds.

rules:-
1) Each match is having 6 rounds
2) first round will be played between 1st to 3rd position players, next round will be played beyween 2nd to 4th position players and so on.

Sample-

input: "11,13,12,9,10,9.5,10.2,10.8"
output: 57

explaination:

here '[]' suggests the players whose timing is considered for round.

round 1: [11   13   12]  9    10    9.5     10.2    10.8  => 11

round 2:  11  [13   12   9]    10    9.5    10.2    10.8  => 9

round 3:  11   13  [12   9    10]    9.5    10.2    10.8  => 9

round 4:  11   13   12   [9    10    9.5]   10.2    10.8  => 9

round 5:  11   13   12   9    [10    9.5    10.2]   10.8  => 9.5

round 6:  11   13   12   9    10    [9.5    10.2    10.8] => 9.5

sum of minimum time = 11 + 9 + 9 + 9 + 9.5 + 9.5 => 57
'''

inputs = input("[+] Enter the time separated by commas \n")
lister = inputs.split(",")
pipe = []
for i in range(0, len(lister)-2):
    pipe.append(min(float(lister[i]), float(lister[i + 1]), float(lister[i + 2])))
print(sum(pipe))
