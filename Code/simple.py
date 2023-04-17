# for x in range(5):
#     print(x)


# def square(n):
#     return n*n

# def sum_squares(x):
#     sum = 0
#     for n in range(x):
#         sum += square(n)
#     return sum

# print(sum_squares(10)) # Should be 285

def factorial(n):
    result = 1
    for i in (1,n+1):
      result=result*i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# def factorial(n):
#     result = 1
#     for x in range(1,n+1):
#         result = result * x
#     return result
# print(factorial(4)) # should return 24
# print(factorial(5)) # should return 120


# def to_celsius(x):
#   return (x-32) * 5/9
# for x in range (0, 101, 50):
#   print(x, to_celsius(x))

# for left in range(7):
#   for right in range(left,7):
#     print("["+ str(left)+"|"+str(right)+"]", end=" ")
#   print()


# teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#     for away_team in teams:
#       if home_team!=away_team:
#         print(home_team+'vs'+away_team)