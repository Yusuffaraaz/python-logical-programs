"""name = input("Enter your name : ")
print(len(name))
print(name.find(" "))
print(name.rfind("a"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("a"))
print(name.replace(" " , "-"))"""

username = input("Enter Your username : ")

if len(username)>12:
    print("Useername should not be more than 12 characters")

elif not username.find(" ") == -1:
    print("Your username should not contain spaces")

elif not username.isalpha():
    print("Your username should not contain digits")

else:
    print("welcome" , username)
