#Write a program to calculate the sum of whole numbers.

whole_num=int(input("Enter the numbers whose sum you want to find."))

var_sum=0
for r in range(1,whole_num+1):
    var_sum= var_sum+r
    print("the sum is" ,var_sum,)