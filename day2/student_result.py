'''
Accept the average score of the student and print the result as follows:
0 to 59         Fail
60 to 84        Second class
85 to 95        First class
96 to 100       Excellent
Also check for invalid score
'''

average_score = int(input('enter the average score of the stduent : '))
if average_score<0 or average_score>100:
    print("the result is invalid")
elif average_score>=0 and average_score<=59:
    print("fail")
elif average_score>=60 and average_score<=84:
    print("Second class")
elif average_score>=85 and average_score<=95:
    print("first class")
else:
    print("excellent") 