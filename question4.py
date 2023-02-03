# Check how many times a given number can be divided by 3 before it is less than or equal to 10

def count_divisions(num):
    count = 0
    while num >= 10:
        num = num / 3
        count += 1
    return count

num = int(input("Enter Number: "))
print(count_divisions(num))