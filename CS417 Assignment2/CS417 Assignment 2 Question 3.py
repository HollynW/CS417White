# Hollyn White
# CS417: Assignment 2
# Problem 3: 
# Write a function that counts the the characters in a string input by the user. 
# Write a main function that calls this function and displays the string and number of characters.

# main() function
def main():
    string = input("Type something in... ")
    number = count_characters(string)

    print("What you entered:", string)
    print("Number of characters:", number)

# count_characters(string) function
def count_characters(string):
    count = 0
    for character in string:
        count = count + 1
    return count

if __name__ == "__main__":
    main()

