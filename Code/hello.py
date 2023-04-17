# for i in range(100):print('kola')

# color ='red'
# thing ='rose'
# print(color+' '+ 'is the color of ' +   thing)

# print(20//3)
# print(type("a"))
# print(type(2.5))
# print(type(True))

# length=10;
# width=20;
# area= length*width;
# print(area)
# print("The area of the rectangle is "+ str(area) )
# def greeting(Name):
#     print("Hello my boy "+ Name)
# greeting("Saimon")
# greeting("Mahi")

# def greeting(name, depertment):
#     print("Hello "+ name)
#     print("You are part of "+ depertment)

# greeting("saimon", "QA")

# def football(name, position, foot, age):
#     print(name)
#     print("He plays as a "+ position)
#     print("His strong foot is "+ foot)
#     print("He is "+ age)

# football("Ronaldo", "Striker", "right", "36")
# print(" ")
# football("Messi", "Forward", "left","33")

# def print_seconds(hours, minutes, seconds):
#     print(hours*3600)
#     print(minutes*60)
#     print(seconds*1)
#     print(hours*3600+minutes*60+seconds)


# print_seconds(1,2,3)

# def area_triangle(height, width):
#     return (height*width)/2
# Triangle1= area_triangle(2,3)
# Triangle2= area_triangle(4,5)
# sum=Triangle1+Triangle2
# print("The sum of the triangls is "+ str(sum))

# def convert_seconds(seconds):
#     hours = seconds//3600
#     minutes = (seconds - hours*3600)//60
#     remaining_seconds = seconds - hours*3600 - minutes*60
#     return hours, minutes, remaining_seconds
# hours, minutes, seconds= convert_seconds(5000)
# print(hours,minutes, seconds)

# def greeting(name):
#     print("You are welcome Mr. "+ name)
# result= greeting("saimon")
# print(result)

# name="saimon"
# number=len(name)*5
# print("Hello "+name+ ". Your lucky number is "+str(number))
# name="mahi"
# number=len(name)*5
# print("Hello "+name+ ". Your lucky number is "+str(number))

# def lucky_num(name):
#     number=len(name)*5
#     return("Hello "+name+ ". Your lucky number is "+str(number))
# a=lucky_num("saimon")
# b=lucky_num("mahi")
# print(a," ", b)

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")

# def month_days(month, days):
#     print(month+ " has "+str(days) +" days.")

# month_days("June", "30")
# month_days("July", "31")

# def month_days(month,days):
#     print(month + " has " + str(days) + " days.")
# month_days("June","30")
# month_days("July","31")

# def order_number(number1, number2):
#     if number1>number2:
#         return number1, number2
#     else:
#         return number2, number1
# smaller, bigger= order_number(60, 50)
# print(smaller, bigger)

# print("cat" == "Cat")

# def hint_username(username):
#     if len(username)<3:
#         print("The name should be more than three word")
# hint_username('sa')

# conditional block

# def is_positive(number):
#   if number>0:
#     return True
#   else:
#         None

# def weather(temperature):
#     if temperature>30:
#         print("It is hot")
#     else:
#         print("It is cold")
# weather(50)

# def is_positive(number):
#   if number > 0:
#     return True
#   else:
#     return False
# print(is_positive(2))
# print(is_positive(-2))

# def is_even(number):
#     if number%2==0:
#         return True
#     return False
# print("Is it an even number? Ans: "+ str(is_even(11)))

# #for_print
# def hint_username(name):
#     if len(name)<3:
#         print("The name should be more than 3 words")
#     elif len(name)>15:
#         print("The name is too big.")
#     else:
#         print("Valid Username")
# hint_username("Sadiqul Alam Saimon")
# hint_username("Saimon")
# hint_username("SA")
# #for_return
# def hint_username(name):
#     if len(name)<3:
#         return("The name should be more than 3 words")
#     elif len(name)>15:
#         return("The name is too big.")
#     else:
#         return("Valid Username")
# print(hint_username("Sadiqul Alam Saimon"))

# def greeting(name):
#   if name == "Taylor":
#     return "Welcome back Taylor!"
#   else:
#     return "Hello there, " + name

# print(greeting("Taylor"))
# print(greeting("John"))

# def check_num(number):
#     if number > 11:
#        print(0)
#     elif number != 10:
#       print(1)
#     elif number >= 20 or number < 12:
#       print(2)
#     else:
#       print(3)
# check_num(10)

# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?
# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = (filesize+block_size-1)//block_size
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = full_blocks%2
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder > 0:
#         return 4096
#     return 8192

# print(calculate_storage(1))    # Should be 4096
# print(calculate_storage(4096)) # Should be 4096
# print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(6000)) # Should be 8192

# print("big">"small")

# def format_name(first_name, last_name):
# 	# code goes here
# 	if first_name== '' and last_name=='':
# 		string=""
		
# 	elif last_name == "":
# 		string = "Name: "+first_name
# 	elif first_name=="":
# 		string = "Name: "+last_name
# 	else:
# 		string = "Name: "+last_name+", "+first_name
	
# 	return string 

# print(format_name("Ernest", "Hemingway"))
# # Should return the string "Name: Hemingway, Ernest"

# print(format_name("", "Madonna"))
# # Should return the string "Name: Madonna"

# print(format_name("Voltaire", ""))
# # Should return the string "Name: Voltaire"

# print(format_name("", ""))
# # Should return an empty string

# def longest_word(word1, word2, word3):
# 	if len(word1) >= len(word2) and len(word1) >= len(word3):
# 		word = word1
# 	elif len(word2) >= len(word3):
# 		word = word2
# 	else:
# 		word = word3
# 	return(word)

# print(longest_word("chair", "couch", "table"))
# print(longest_word("bed", "bath", "beyond"))
# print(longest_word("laptop", "notebook", "desktop"))

# def sum(x, y):
#     return x+y
# print(sum(sum(1,2), sum(3,4)))

# print(((10 >= 5*2) and (12 <= 5*2)))

# def longest_word(word1, word2, word3):
# 	if len(word1) >= len(word2) and len(word1) >= len(word3):
# 		word = word1
# 	elif len(word2)>= len(word1) and len(word2)>=len(word3):
# 		word = word2
# 	else:
# 		word = word3
# 	return(word)

# print(longest_word("chair", "couch", "table"))
# print(longest_word("bed", "bath", "beyond"))
# print(longest_word("laptop", "notebook", "desktop"))



# def fractional_part(numerator, denominator):
# 	# Operate with numerator and denominator to 
# # keep just the fractional part of the quotient
#     quotient=numerator/denominator
# 	fractional= numerator-(quotient*denominator)
# 	return fractional
# print(fractional_part(5, 5)) # Should be 0
# print(fractional_part(5, 4)) # Should be 0.25
# print(fractional_part(5, 3)) # Should be 0.66...
# print(fractional_part(5, 2)) # Should be 0.5
# print(fractional_part(5, 0)) # Should be 0
# print(fractional_part(0, 5)) # Should be 0

# def sum(num1, num2, num3):
# 	a=num1+num2+num3
# 	if a>30 and a<40:
# 		return 40
# 	else:
# 		return a
# print(sum(10,20,5))
# print(sum(1, 2, 3))

# x=0
# while x<5:
#     print("Not yet x= "+ str(x))
#     x=x+1
# print("x= "+ str(x))

# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x += 1
#     print("Done")
# attempts(10)

# username= get_username()
# while not valid username(username):
#     print("Invalid Username")
#     username:get_username()

# def count_down(start_number):
#   current=start_number
#   while (current > 0):
#     print(current)
#     current -= 1
#   print("Zero!")
# count_down(3)


# if x!=0 and x % 2==0:
#     x=x/2
# print(x)

# def print_range(start, end):
# 	# Loop through the numbers from start to end
# 	n = start
# 	while n <= end:
# 		print(n)
#         n += 1



# print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor += 1
#   return "Done"

# print_prime_factors(100)
# # Should print 2,2,5,5
# # DO NOT DELETE THIS COMMENT

# def is_power_of_two(n):
#   while n!=0 and n==0:
#     n=n/2
#   if n==1:
#     return True
#     n +=1
#   else:
#     return False
# print(is_power_of_two(0)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False
def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114





def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier
		# What is the additional condition to exit out of the loop?
		if result>=25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24