def checking_age_21():
    while True:
        try:
             age = input("insert your age bro/sis!(insert 'o' to out of program ): ")
             if age == 'o' :
                 print("good bye, come back when you already 21!")
                 break
             age = int(age)
        except ValueError:
            print("please just insert your age bruh ! -_- ")

        else:
            if age ==  21 or age > 21:
                print("welcome bruh you accepted, because you already {age} \n")

            else:
                print("unfortunately..,you cant join us :(  \n")


if __name__=="__main__":
    checking_age_21()

            
