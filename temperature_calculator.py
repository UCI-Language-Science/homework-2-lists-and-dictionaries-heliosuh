# Write a program that continuously prompts the user for a 
# temperture (in the scale of your choosing). Every time 
# the user inputs a temperature, the program should report 
# the mean of all the values entered so far. When the user
# types in 'quit' the program should terminate.
#
# An example interaction might look like
# Input a temperature
# >> 42
# The average temperature so far is 42
# Input a temperature
# >> 26
# The average temperature so far is 34.0
# Input a temperature
# >> 52
# The average temperature so far is 40.0
# >> quit
# Goodbye
#
# You can use the sum function to sum all the values in a list
# sum(<list>)

def temperature_calculator():
    # YOUR CODE GOES HERE
    temperatures = []
    while True:
        user_input = input("input a temperature (or type 'quit' to exit): ").strip()
        if user_input.lower() == 'quit':
            print('goodbye')
            break
        try:
            temperature = float(user_input)
            temperatures.append(temperature)
            #calculate average
            mean_temp = sum(temperatures) / len(temperatures)
            print(f"the average temprature so far is {mean_temp}")
        except ValueError:
            print("please enter a vlid temperature or 'quit'.")


if __name__ == "__main__":
    temperature_calculator()