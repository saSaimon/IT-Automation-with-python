# def greet_friends(friends):
#     for friend in friends:
#      print("Hi "+friend)
# greet_friends(['Saimon', 'Mahi', 'Mohan', 'Kaniz'])
# greet_friends('Saimon')
# greet_friends(['Saimon'])

# def multiple(n):
#     result=7
#     for x in range(n, n+1):
#         mul=result*x
#         return mul

# for n in range(0, 101):
#     print("7"+" *", n, "=", multiple(n))
# print(multiple(12))

# def multiples(x):
#     for n in range(100):
#         n = (n*x)
#         if n <= 100:
#             print(n)
# print(multiples(7))

# Recursive

# def factorial(n):
#     result = 1
#     for x in range(1,n+1):
#         result = result * x
#     return result

def factorial(n):
    print("Factorial Called with "+ str(n))
    if n<2:
        print("Returning 1")
        return 1
    result=n* factorial(n-1)
    print("Returning"+ str(result)+ " for factorial of "+ str(n)) 
    return result
factorial(4)

