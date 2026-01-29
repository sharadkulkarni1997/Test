#WAP to input user's name and print it's length
name = input("Enter user name\n")
length = len(name)
print("The lenghth of the name is:",length)

#WAP to find the occurrence of '$" in a string
print("$ occured: ", name.count("$"), "times")

#WAP to capitalize the first letter of the name and find the index of substring "talw"
name = name.capitalize()
print(name)
print(name.find("talw"))

#WAP to check if the string starts with "A" or ends with "z"
if name.startswith("A"):
    print("The string starts with A")
else:
    print("The string does not start with A")
if name.endswith("z"):
    print("The string ends with z")
else:
    print("The string does not end with z") 

#END