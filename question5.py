# Why and when to use while loop in Python? Give a detailed description with example.

'''
In Python, a while loop is used to repeat a block of code as long as a certain condition is true. It continues to execute the code block until the condition becomes false.
The syntax for a while loop is as follows:

while condition: 
    # block of code 

The condition is evaluated before each iteration of the loop. If the condition is true, the code block is executed. If the condition is false, the loop terminates and the program continues with the next line of code after the loop.

'''
'''Example of while loop: '''

# Print the numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

'''In this example, the variable i is initialized to 1. The while loop continues to execute as long as i is less than or equal to 5. The code inside the loop prints the value of i and increments i by 1. This continues until i is greater than 10, at which point the loop terminates.'''