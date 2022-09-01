import requests, json, time

ending_symbols = ['.', '!', '?']

url = "https://icanhazdadjoke.com/"
search_url = "https://icanhazdadjoke.com/search?term="

first_loop = True

while(True):
    searching = False
    if first_loop:
        choice = input("Do you want a random joke or search a topic? Type '1' for random. Type '2' to search. Type '3' to quit. ")
    else:
        choice = input("Do you want a random joke or search a topic? Type '1' for random. Type '2' to search. Type '3' to quit. Type '4' to continue your last search. ")
    if choice == '1':
        response = requests.get(url, headers={"Accept":"application/json"})
    elif choice == '2':
        counter = 0
        search_term = input("What do you want to search for? ")
        response = requests.get(search_url + search_term, headers={"Accept":"application/json"})
        searching = True
        first_loop = False
    elif choice == '3':
        print("Goodbye")
        break
    elif choice == '4':
        response = requests.get(search_url + search_term, headers={"Accept":"application/json"})
        searching = True
        counter += 1
    else:
        print("There was an error.")
        continue

    data = json.loads(response.text)
    if searching:
        if len(data['results']) > 0 and counter < data['total_jokes']:
            joke_words = data['results'][counter]['joke'].split(' ')
        else:
            print("No result")
            continue
    else:
        joke_words = data['joke'].split(' ')

    question = ''
    answer = ''
    last_word_index = 0

    for index in range(len(joke_words)):
        question += f"{joke_words[index]} "
        if joke_words[index][-1] in ending_symbols:
            last_word_index = index
            break

    for index in range(len(joke_words) - last_word_index):
        if index == 0:
            continue
        answer += f"{joke_words[index + last_word_index]} "

    print(question)
    if len(answer) > 0:
        time.sleep(2)
        print(answer)

