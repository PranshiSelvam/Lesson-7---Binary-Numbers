one = int(input("Grade 1 = "))
two = int(input("Grade 2 = "))
three = int(input("Grade 3 = "))
four = int(input("Grade 4 = "))
five = int(input("Grade 5 = "))

total = one + two + three + four + five 
print("Your total grade is ", total)

average = total/5
print("You average grade is ", average)

if (average >= 95 and average<=100):
    print("You receive A+. Well done")
elif (average >=90 and average<=94):
    print("You receive A. Well done")
elif (average >=85 and average<=89):
    print("You receive B+. Not bad")
elif (average >=80 and average<=84):
    print("You receive B. Not bad")
elif (average >=75 and average<=79):
    print("You receive C+. Could do better")
elif (average >=70 and average<=74):
    print("You receive C. Could do better")
elif (average >=65 and average<=69):
    print("You receive D. Improve")
else:
    print("You have reveived E. You should work harder.")
