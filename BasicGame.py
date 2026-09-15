name_list = [
    "Alice", 
    "Bob", 
    "Julie",
    "Rod"
    ]
questions = [
    "Where would you like to travel",
    "What is your favorite color?",
    "What program are you in?"
]

import random
chosen_name = random.choice(name_list)
chosen_question = random.choice(questions)


# Defining a function:
def rand_draw(n_list, q_list):
    chosen_name = random.choice(name_list)
    chosen_question = random.choice(questions)

    return (chosen_name , chosen_question)


while True: 
    chosen_name, chosen_question = rand_draw(name_list, questions)

    print(f"{chosen_name}, please answer: {chosen_question}")

    user_choice = input("Enter 'Y' to continue or any other key to quit")

    if user_choice == 'Y':
        continue
    else:
        break