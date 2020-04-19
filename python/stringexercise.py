# tanya alamat email user
email = input("Enter your email address: ")

# cek apakah emailya valid
# valid: ada tanda @ 
if email.count("@") == 1:
    # john@gmail.com
    # ada domain misalnya .com atau .de dsb
    dot_position = email.find(".")
    domain = email[dot_position]
    print(dot_position)
    if dot_position is not -1:
        print("email is valid")
        # print domain .com, .id ...
    else:
        print("email not valid")
else:
    print("email not valid")


