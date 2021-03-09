'''
Write a program which can compute the factorial(阶乘) of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be: 40320
Hint: In case of input data being supplied to the question, 
        it should be assumed to be a console input.
'''

def factorial(num):
    p = 1
    for i in range(1,num+1):
        p*=i
    return p

Num = int(input("Input a number and we will find it factorial: "))
print(factorial(Num))

'''
Recursive:
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
Solution:
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(raw_input())
print fact(x)
'''