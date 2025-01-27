# Write a program that asks the user to input a string and then
# prints out the counts of each character used in the string.
#
# For example, if the input string is 'hello, world!' the output
# should be something like
#
# 'h': 1
# 'e': 1
# 'l': 3
# 'o': 2
# ',': 1
# ' ': 1
# 'w': 1
# 'r': 1
# 'd': 1
# '!': 1
#
# You don't have to match this format exactly, but it's important
# for the autograder that the message you print contains
# each of the character/count pairs in the following format.
# 
# '<character>': <count>
#
# You should get input from the user using the input function. Your
# code should work for arbitrary strings, including the empty string.

def char_counter():
    # YOUR CODE GOES HERE
    user_input = input ("please enter a string: ")
    char_counts = {}

    for char in user_input:
        if char in char_counts:
            char_counts[char]+= 1
        else:
            char_counts[char] = 1
    for char, count in char_counts.items():
        print(f"'{char}': {count}")



if __name__ == "__main__":
    char_counter()