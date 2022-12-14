import random
import json
import questions

	
with open('students.json') as f:
   students = json.load(f)


def choose_student():
    student_dictionary = random.choice(students)
    student_dictionary['turns'] += 1
    student_name = student_dictionary['name']
    save()

    return student_name


def least_called_on():
    lowest_number = 10000
    for student in students:
        if student['turns'] < lowest_number:
            lowest_number = student['turns']
    
    possible_students = []
    for student in students:
        if student['turns'] == lowest_number:
            possible_students.append(student)
    
    selection = random.choice(possible_students)
    selection['turns'] += 1 
    save()

    return selection

def list_students():
    message = "Name\t\tCalled On\n-------------------------\n"
    for student in students:
        message += student['name'] + '\t\t' + str(student['turns']) + '\n'
    return message


def update_turn_counter():
    student = input("Student Name: ").title()
    number = int(input("Number of turns: "))
    changed = False

    for item in students:
        if item['name'] == student:
            item['turns'] = number
            changed = True
    if not changed:
        print(f"\nError, no student by the name of {student}")
    save()

    return f'{student} now has taken {number} turns ✔️'

def save():
    with open("students.json", "w") as outfile:
        json.dump(students, outfile)


def quizz():
    print("\n\t⏰ ⏰ ⏰\033[1;31;40m Quizz time\033[1;37;40m ⏰ ⏰ ⏰\n")
    while True:
        for question in questions.terms:
            print(f"\n\t\033[1;32;40m-------------------------------------------- {least_called_on()['name']}'s turn ----------------------------------------------\033[1;37;40m \n")
            print(f"\t\033[1;33;40mDefine: {question['topic']}\033[1;37;40m")
            again = input("\n\t\033[1;30;40mPress Enter or type 'back'\033[1;37;40m")
            print(f"\n\t{question['definition']}\n\n")

            if again == 'back':
                print(f"\n\t...Just because you asked here is the definition: {question['definition']}\n")
                break
        break

def main():

    while True:
        menu = input("""\n\n
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 \033[1;31;40m Welcome to the Wheel of Terror!\033[1;37;40m 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

1: Choose random student
2: Choose least called on
3: List all students
4: Update turn counter
5: Terminology Quizz
6: Quit

==> """)
        

        if menu == '1':
            print("\n" + "It is " + "\033[1;32;40m" + choose_student() + "'s\033[1;37;40m turn 😊")

        elif menu == '2':
            print("\n" + "It is " + least_called_on()['name'] + "'s turn 😊")

        elif menu == '3':
            print("\n\n" + list_students())

        elif menu == '4':
              print("\n" + update_turn_counter())

        elif menu == '5':
              quizz()

        elif menu == '6':
            print('\nLater! 👋' )
            break
        else:
            print('\n🚨🚨 Invalid selection 🚨🚨')
main()



