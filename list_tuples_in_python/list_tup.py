#WAP to ask user to enter names if their 3 fav movies and store them in a list
movies = []
movies.append(input("Enter your first fav movie "))
movies.append(input("Enter your second fav movie "))
movies.append(input("Enter your third fav movie "))
print("Your top three movies are ", movies)
#END

#WAP to check if a list contains a palindrome of elements
palindrome = []
palindrome.append(input('Enter the first value'))
palindrome.append(input('Enter the second value'))
palindrome.append(input('Enter the third value'))
palindrome.append(input('Enter the fourth value'))
palindrome.append(input('Enter the fifth value'))
palindrome.append(input('Enter the sixth value'))
#print(palindrome[0:3])
#print(palindrome[3:])
#if(palindrome[0:2]== palindrome[3:]):
#    print("The entered values are a palindrome")
#else:
#    print("It is not a palindrome")
reverse = palindrome.reverse()
if(palindrome == reverse):
    print("The entered values are a palindrome")
else:
    print("It is not a palindrome")
#END

#WAP to count the number of students with A grane in the following tuple
tup = ["C", "D", "A", "A", "B", "B", "A"]
print(tup.count("A"), "Students have scored Grade A") 
tup.sort()
print(tup)