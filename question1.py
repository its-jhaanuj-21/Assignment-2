# Write a program accept percentage from the user and display the grade

marks = float(input("Enter your percentage: "))
if marks < 60:
    print("Grade: D")
elif 60 <= marks <= 80:
    print("Grade: C")
elif 80 < marks <=90:
    print("Grade: B")
else:
    print("Grade: A")

