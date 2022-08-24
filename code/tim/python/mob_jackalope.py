# Mob Programming: Jackalope Simulator
# Version 1
# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

# Jackalopes are reproductive from ages 4-8 and die at age 10.
# Gestation is instantaneous. Each gestation produces two offspring.
# Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
# With these conditions in mind, we can represent our population as a list of ints.

jackalopes = [0, 0]

population = len(jackalopes)

print(jackalopes)

year = 0
while len(jackalopes) <= 1000:        
    year += 1
    bachelopes = 0
    
    # age jacks
    for index in range(len(jackalopes)):
        jackalopes[index] +=  1
        
    # print('jacks age', jackalopes)

    young_jackalopes = []
    # find out it jacks are mating age
    for index, value in enumerate(jackalopes):
        if jackalopes[index] >= 4 and jackalopes[index] <= 8:
            bachelopes += 1

        if jackalopes[index] < 10:
            young_jackalopes.append(jackalopes[index])
            # print(jackalopes)    
 
    jackalopes = young_jackalopes

    # If 2 jackalopes are between 4-8, add 2 to population
    # if bachelopes % 2 == 0:
    #     print(bachelopes % 2)
    #     jackalopes.append(0)
    #     jackalopes.append(0)
    # # break
    # print(len(jackalopes))

    for x in range(bachelopes):
        if x % 2 == 0:
            jackalopes.append(0)
            jackalopes.append(0)    


print(year) # years it took to get 1000 jackalopes

# TO DO
# Handle deaths 


# Figure out modulus   