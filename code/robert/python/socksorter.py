import random

# Create a function to bucket the socks/counter at random

def sock_counter():

    sock_list = [0,0,0,0]
    sock_counter = 0

    while sock_counter < 100:
            sock_list[:] = [item + random.randint(1,10) for item in sock_list]
            sock_counter = sum(sock_list)

    print(sock_list)
    print(f"The sum of the list ({sock_counter}) is above 100")

    max_sock = sock_list.index(max(sock_list))
    print(f"The index for the max sock is {max_sock}")

    if sock_counter > 100:
        sock_list[max_sock] = abs(sock_list[max_sock] - (sock_counter-100))
        sock_counter = sum(sock_list)

    print(f"Deleting the {max_sock} index by the difference between sum of the list and 100 brings the total socks to {sock_counter}")

    sock_types = {
        'ankle': sock_list[0],
        'crew' : sock_list[1],
        'calf' : sock_list[2],
        'thigh' : sock_list[3]
    }

    loners = 0
    sock_values = list(sock_types.values())
    print(sock_values)

    for item in sock_types.values():
        if item % 2 != 0:
            loners += 1

    matches = (50 - loners)

    print(matches)
    print(loners)


sock_counter()




#Use dictionary to keep track of sock types that match and loners for each group(Should only be 1 loner max for each group... right?)