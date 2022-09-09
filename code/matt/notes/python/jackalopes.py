
"""
The goal is to calculate how many years it will take for two age 0 jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.
"""


jacks = [0, 0]

years = 0


while len(jacks) < 1000:
    years += 1

    # age jacks
    for index in range(len(jacks)):
        jacks[index] += 1

    # Number of jacks who can have babies
    frisky_jacks = 0
    for index in range(len(jacks)):
        age = jacks[index]
        if age > 3 and age < 9:
            frisky_jacks += 1
    

    print(f'Year {years}: frisky: {frisky_jacks} ')

    if frisky_jacks % 2 != 0:
        frisky_jacks -=1
    
    baby_jacks = frisky_jacks
    # print('baby jacks', baby_jacks)

    for num in range(baby_jacks):
        jacks.append(0)


    # Kills Jacks
    new_jacks = []
    for item in jacks:
        if item <= 9:
            new_jacks.append(item)

    jacks = new_jacks

print(years, len(jacks))