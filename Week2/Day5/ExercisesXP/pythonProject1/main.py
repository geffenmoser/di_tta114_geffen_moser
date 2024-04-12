import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']
word = random.choice(wordslist)

### YOUR CODE STARTS FROM HERE ###
default_gallow = ["___________", "|        |", "|        |","|       ", "|       ", "|       ", "|       ","|___________"]
is_over = False

def print_hangman(int):
    global is_over
    global default_gallow
    gallow = default_gallow
    if int >= 1:
        gallow[3] = "|      O" #head
    if int >= 2:
        gallow[4] = "|      []"  #torso
    if int >= 3:
        gallow[4] = "|     ~[]"  #left arm
    if int >= 4:
        gallow[4] = "|     ~[]~"  #both arms
    if int >= 5:
        gallow[5] = "|      /"  #left leg
    if int >= 6:
        gallow[5] = "|      //"  #both legs
    for i in gallow:
        print(i)
    if int >= 7:
        is_over = True
        print("You're a loser and he's so dead and its your fault")

def hangman_play():
    global word
    global is_over
    body_part_counter = 0
    guess_list = []
    check = False
    current_right_letters = '*'*len(word)
    print_hangman(0)
    print(f"Mystery word is {len(word)} letters long")
    while is_over != True:
        guess = input("Guess a letter of the mystery word:")
        for char in guess_list:
            if guess == char:
                guess = input("You already guessed that letter, try again:")
            else:
                guess_list += guess
        for i in range(len(word)):
            if word[i] == guess:
                current_right_letters = current_right_letters[:i-1] + guess + current_right_letters[i+1:]
                print_hangman(body_part_counter)
                print(f"{current_right_letters}")
                check = True
        if check == False:
            print("That letter wasn't in the mystery word")
            print(f"{current_right_letters}")
            body_part_counter += 1
            print_hangman(body_part_counter)
        if current_right_letters == word:
            print(f"You guessed the word")
            is_over = True

hangman_play()