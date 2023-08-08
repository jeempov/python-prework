#Question 1
#Write a function to print "hello_USERNAME!"
def hello_name(user_name):
    '''This function prints hello_ added to the str passed in the function with an ! at the end'''
    print("hello_"+ str(user_name)+ "!")


#Question 2
#Write a function that prints the odd numbers from 1-100, returning nothing
def first_odds():
    '''This function prints the odd numbers from 1-100'''
    for num in range(1,100):
        if num % 2 != 0:
            print(num)


#Question 3
# Write a function to return the max number of a given list
def max_num_in_list(a_list):
    '''this function returns the max number from a given list'''
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

#Question 4
#A function to return if the given year is a leap year
def is_leap_year(a_year):
    '''This function returns True if the year passed is a leap year'''
    if a_year % 4 == 0:
        if a_year % 400 == 0:
            return True
        elif a_year % 100 != 0:
            return True
        else:
            return False        
    else:
        return False


#Question 5
#A function to see if all numbers in a list are consecutive numbers
def is_consecutive(a_list):
    '''returns True if the list contains all consecutive numbers, even if unordered'''
    if len(a_list) < 2:
        print("Your list isn't long enough")
        return False
    else:
        a_list = sorted(a_list)
        previous_value = a_list[0]
        for value in a_list[1:]:
            if value - previous_value == 1:
                previous_value = value
                continue
            else:
                return False
        return True