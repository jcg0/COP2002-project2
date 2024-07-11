# Jefferson Griebel / jcg0
# COP2002.0M1: PROGRAM LOGIC
# 06/11/2024
# Project 4: User input and while loops
# Use inputs, lists and loops to create a cypher encryption program

# main function
def main():
    # user_input function takes the input from the user that will be encrypted
    user_input = input("Enter the text to encrypt: ")

    # normal_lettes and cypher_letters lists are holding the characters that will be taken and encrypted
    normal_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
                      "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cypher_letters = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                      "A", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",  "t", "u", "v", "w", "x", "y", "z", "a"]

    # final_msg will hold our final encrypted value
    final_msg = ""

    # to start this for loop we are looping through the user input
    for letter in user_input:
        letter_index = 0

        # checking to see where the index is in the normal letters list
        while letter_index < len(normal_letters) and letter != normal_letters[letter_index]:
            letter_index += 1

        # shifting our msg and recreating it using the cypher letters
        if letter_index < len(normal_letters):
            final_msg += cypher_letters[letter_index]
        else:
            final_msg += letter

    print(final_msg)


if __name__ == "__main__":
    main()
