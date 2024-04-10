#Exercise 1

# import random
# def get_random_temp(season):
#     if season == "winter":
#         x = random.randint(-10, 16)
#     elif season == "summer":
#         x = random.randint(17, 40)
#     return(x)
#
# def main():
#     season = input("what season is it now? Type in winter or summer:")
#     var = float(get_random_temp(season))
#     print(f"The temperature right now is randomly {var} degrees celsius")
#     if var < 0:
#         print("Brrr thats freezing, wear some extra layers today!")
#     elif var < 17:
#         print("Dont forget your coat!")
#     elif var < 24:
#         print("enjoy the brisk weather")
#     elif var < 33:
#         print("enjoy the balmy weather")
#     else:
#         print("enjoy the hot weather!")
# main()
#
# #Exercise 2
# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]
#
# def starwars_trivia():
#     user_answer = ""
#     user_answer_list = []
#     wrong_answers_list =[]
#     correct_counter = 0
#     for d in data:
#         question = d.get("question")
#         answer = d.get("answer")
#         user_answer = input(f"{question} :")
#         user_answer_list.append(user_answer)
#         if user_answer == answer:
#             print("Correct!")
#             correct_counter += 1
#         else:
#             wrong_answers_list.append(user_answer)
#             print(f"False! The correct answer is {answer}")
#     print(f"Thanks for playing \n"
#           f"You got {correct_counter} questions correct and {len(wrong_answers_list)} questions wrong. \n ")
#     if len(wrong_answers_list) > 3:
#         print(f"Since you got {len(wrong_answers_list)} questions wrong, try playing again!")
#
# starwars_trivia()
##Exercise 3
def get_age(year, month, day):
    current_year = 2024
    current_month = 4
    current_day = 10
    age = (current_year - year)
    if (month, day) > (current_month, current_day):
        age -= 1
    return age
print(get_age(1997,4,11))

def can_retire(gender, birth_year, birth_month, birth_day):
    age = get_age(birth_year, birth_month, birth_day)
    if gender == "male" and age >= 67:
        return True
    elif gender == "female" and age >= 62:
        return True
    else:
        return False

j = can_retire("male", 1964, 2, 25)
print(f"{j}")

#Exercise 4
def sum_weird_function(x):
    res = (x + (x*11) + (x*111) + (x*1111))
    return res

print(sum_weird_function(3))




