from random import choices
nrolls=10000
total=0
ndice=3
for i in range(nrolls):
    dice=choices(range(1,7),k=ndice)
    dice.sort(reverse=True)
    total=total+dice[0]+dice[1]
print("Average roll=",total/nrolls)

#When ndice=2, average roll=7.0489.  When ndice=3, average roll=8.4719.  Thus, the average sum increased by 1.423.  The game would not be fair if only 1 point was added to the 2 dice, since the difference of the averages is about 1.4.