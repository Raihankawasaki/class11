#Write a program to reverse the string entered by the user.

string=input("Write a word or sentence you want to reverse. \n")

rev_string=""
for q in string:
    rev_string=q+rev_string
print("Original string is ",string," and the reversed string is ",rev_string,)
