#grade-pass system

grade = int(input("insert the student grade number to check your grade: "))

if grade >= 90 and  grade <=100:
    print ("Excelent!...you get A")
elif grade >=80 and grade <  90:
    print ("well grade!.. B it was close!")
elif grade >=70 and grade < 79:
    print ("keep UP!.. C its the beginning!")
elif grade >=60 and grade < 69:
    print ("learn harder get greater!.. D its small step!")
elif grade >=0 and grade <= 59:
    print ("dude, so sorry .. D GET BETTER SOON!")
else:
    print ("Invalid Grade Number. Please Enter a Value Between 0 - 100.")
    