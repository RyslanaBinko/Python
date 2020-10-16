email = input("Enter your email: ")


def hide_email(email):
    new_email = email[:2] + "***" + "@" + "**" + email[len(email)-3:]
    print(new_email)


hide_email(email)