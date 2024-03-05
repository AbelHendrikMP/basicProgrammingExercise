def reverse_word(word):
    return  word[::-1] 

while True:
        try:
            word = str(input("insert your word(insert 'e' to end program) :"))
            if word == 'e':
                print("see you next time boy!")
                break
            result = reverse_word(word)
            print(f"the result of combined word is {result}")
        except ValueError:
            print("please only insert word bruh")
            
            

# word = str(input("insert your word :"))

# reverse = word[::-1]
# print("the reversed word :",reverse)
