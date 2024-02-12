import random



eng_words = ["Hello", "Bye", "Task", "Program"]
fr_words = ["Salut","Au revoir","Tâche", "Programme"]
score = 0

mode = input("Pick option: 0 - add new words, 1 - test your translation skills,  2 - allows you to change words : \n")
while ((mode != '0') and (mode != '1') and (mode != '2')):
    mode = input("Incorrect option! Pick 0 , 1 or 2 (0 allows to add a new word to list, a 1 allows you to test your translation skills and 2 allows you to change words within the list.\n")

if mode == "1":
    print("Translate as man words as you can! You have 10 tries!")
    for i in range(10):
        number = random.randint(0, len(eng_words)-1)
        print("How to translate this word: " + eng_words[number])
        if input() == fr_words[number]:
            print("Well done!!!")
            score += 1
        else:
            print("Close, the correct word was - " + fr_words[number])

elif mode == "2":
    print("Using this command you can change words")
    number = int(input("Enter valid number: \n"))
    if number >= 0 and number <= len(eng_words)-1:
        eng_words[number] = input("enter new word: ")
        translation = input("the french translation for new word: ")
        fr_words[number] = translation
        print("New word added.")
    else:
        print("error")

else:
    word = input("Enter english word: ")
    translate = input("Enter the translation of the word: ")
    if len(word) > 0 and len(translate) > 0:
        eng_words.append(word)
        fr_words.append(translate)
        print("New word has  been successfully added!")
    else:
        print("Words are too short")
        


if mode == "1":
    if score == 10 :
        print("Perfect score")
    else:
        print(f"Good try your score was: {score}")
