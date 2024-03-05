def extract_domain(email):
    return email.split('@')[1]

while True:
    user_email = input("insert your email (or insert 'e' to end teh program ): ")
    if user_email.lower() == 'e':
        print("Thank you!, but be aware where you insert your email :)\n")
        break
    extracted_domain = extract_domain(user_email)
    print(f"Domain yang diekstraksi: {extracted_domain}\n")
