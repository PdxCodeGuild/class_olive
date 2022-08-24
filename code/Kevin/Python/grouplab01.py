'''
Program of seeing how many years it takes to make 100 Jackalopes
'''

        


years = 0
key_count = 3


jackalope_dict = {
    1:0,
    2:0
}

jackalopes = 0


while jackalopes < 100:

    #Make AND clear this variable to determine the of-age deer this year.
    of_age_jackalopes = 0

    #Clear this variable! It will be added to at the end before it returns to the while loop.
    jackalopes = 0

    # Age Jackalope
    for key in jackalope_dict:
        jackalope_dict[key] += 1


    
        


    # If ages 4-8, add how many of-age jackalopes we got
    for key in jackalope_dict:
        if jackalope_dict[key] > 3 and jackalope_dict[key] < 9:
            of_age_jackalopes += 1


    # Make more deer based on the numbers of of-age deer. 2 deer are needed to make 2 deer. 
    for x in range((of_age_jackalopes//2)*2):
        jackalope_dict[key_count] = 0
        key_count += 1                      #Key count starts at 3 for recording the first of the new deer in the dictionary, 
                                            # then counts up for every new deer in the dict so that we have new unique keys every time.
        
    print(jackalopes)
    #Loop through all the deer and count how many deer you have that aren't dead.
    for key in jackalope_dict:
        if jackalope_dict[key] < 10:
            jackalopes += 1



    years += 1
    print(years, jackalopes, jackalope_dict)

print(f'It took {years} years to make {jackalopes} Jackalopes.')
