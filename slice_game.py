#program to take user's input, slice it and add it to another string to form a word
# if word in the fruits list, print user has won, else try again

help = input("Press H for Help: ")
if help.upper() == "H":
    print("Help:\n"
        "This program takes only 7 letter words"
      "You are supposed to enter the first three letters of a word\n"
          "from the list.\n"
          "And also try enter the last 4 letters.\n"
          "The program only prints from the 4th letter of the\n"
          "second word")
else:
    print("Continue")
list =["BANTAMA","CHICAGO","GEORGIA","TAKORADI","CONAKRY","NAIROBI", "JAKARTA", "STANLEY", "LINCOLN", "KANESHIE", "TESANO", "OBUASI"]
print("The words are listed below")
for word in list:
    print(f"Try to form {word} ")
print("\n")
while True:
    word = input("Enter your first 3 letters: ")
    first_slice = word[0:3] #returns first 3 letters
    print(f"{first_slice} is your first word")

    word2 = input("Enter last 4 letters.: ")
    second_slice = word2[3:8] #returns 4rd to 7th letter
    print(f"{second_slice} is your second word")


    #print your word
    your_word = first_slice + second_slice
    print(f"{first_slice} + {second_slice} = {your_word} is your word\n")


    if your_word.upper() in list:
        print("HURRAYYY!,You formed a valid word")
        print("Take your reward from Sadique")
        break
    else:
        print(f"Your sliced word is {your_word}")
        print("Try again \n")