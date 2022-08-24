

def jackalope_dies(key_count, jack_dict):
    new_dict = {}
    for index, age in enumerate(jack_dict.values()):
        if age < 10:

            new_dict[key_count] = age
            key_count += 1
            
    list_return = [new_dict, key_count]
    return list_return





        


years = 0
key_count = 3

jackalope_dict = {
    1:0,
    2:0
}
while len(jackalope_dict) < 100:

    make_jackalope_counter = 0

    # Age Jackalope
    for key in jackalope_dict:
        jackalope_dict[key] += 1 


    
        


    # If ages 4-8, make 2 jackalope
    for key in jackalope_dict:
        if jackalope_dict[key] > 3 and jackalope_dict[key] < 9:
            make_jackalope_counter += 1

    # Makem
    for x in range(make_jackalope_counter):
        jackalope_dict[key] = 0
        

    

    # returned_list = jackalope_dies(key_count, jackalope_dict)
    # jackalope_dict = returned_list[0]
    # key_count = returned_list[1]



   
    years += 1
    print(jackalope_dict)

# print(jackalope_dict, years)
