# Use nested while loop to print 3 different pattern.

'''
Pattern 1: 
*
* *
* * *
* * * *
* * * * *
'''
rows = 5
i = 1
while i <=rows:
    j = 1
    while j <= i:
        print("* ", end="")
        j = j+1
    print("")
    i = i+1
print("                            ")

#-----------------------------------------------------------------------

'''
Pattern 2: 
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

rows = 5
i = 1
while i <=rows:
    j = 1
    while j <= rows:
        print("* ", end="")
        j = j+1
    print("")
    i = i+1
print("                            ")

#-----------------------------------------------------------------------

'''
Pattern 3: 
* * * * *
*       *
*       *
*       *
* * * * *
'''

rows = 5
i = 1
while i <=rows:
    j = 1
    while j <= rows:
        if(j==1 or j==rows or i==1 or i==rows):
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j = j+1
    print("")
    i = i+1
print("                            ")

