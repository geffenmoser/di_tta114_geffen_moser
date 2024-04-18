#challenge 1
def alpha_sort_cs_list(comma_separated_string):
    word_list = []
    word = ""
    for char in comma_separated_string:
        if char == ",":
            word_list.append(word.strip())
            word = ""
        else:
            word += char
    print(sorted(word_list))

strangly = "apple, banana, hair, pants, airplane, words"
alpha_sort_cs_list(strangly)

# challenge 2
def longest_word(sentence):
    word = ""
    word_list = []
    shaved_string = sentence
    for char in shaved_string:
        if char == " ":
            word_list.append(word.strip())
            word = ""
        else:
            word+=char
    max = 0
    max_word = ""
    for word in word_list:
        if len(word) > max:
            max = len(word)
            max_word = word
    return max_word

sent = "I'm a stupid sentence filled with preposterous and unintelligible words."
print((longest_word(sent)))