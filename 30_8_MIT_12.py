# ######################################
# # EXAMPLE: Exceptions with summing digits in a string
# ######################################

# # Not using exceptions
# def sum_digits(s):
#     """ s is a non-empty string containing digits
#     Returns sum of all characters that are digits """
#     total = 0
#     for char in s:
#          if char in '0123456789':
#         # if char in '0123456789': # ValueError: invalid literal for int() with base 10: 'a'
#             val = int(char)
#             total += val
#     return total

# print(sum_digits("123"))  ## 6
# print(sum_digits("123abc"))  ## 6  if not if statement then ValueError: invalid literal for int() with base 10: 'a'


# # Using exceptions around potentially problematic code
# # Print that an error happened and let the program keep going
# def sum_digits_except(s):
#     """ s is a non-empty string containing digits
#     Returns sum of all characters that are digits """
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             print("couldn't convert character", char)
#     return total

# print(sum_digits_except("123"))
# print(sum_digits_except("123abc"))

# # 6
# # couldn't convert character a
# # couldn't convert character b
# # couldn't convert character c
# # 6



# ######################################
# # EXAMPLE: Exceptions with user input
# ######################################

# def divide_nums1():
#     a = int(input("Tell me one number: "))
#     b = int(input("Tell me another number: "))
#     print(a/b)

# # print(divide_nums1()) ## ZeroDivisionError: division by zero


# def divide_nums2():
#     try:
#         a = int(input("Tell me one number: "))
#         b = int(input("Tell me another number: "))
#         print(a/b)
#     except:
#         print("Bug in user input")

# # print(divide_nums2())
# # Bug in user input
# # None


# def divide_nums3():
#     try:
#         a = int(input("Tell me one number: "))
#         b = int(input("Tell me another number: "))
#         print("a/b = ", a/b)
#         print("a+b = ", a+b)
#     except ValueError:
#         print("Could not convert to a number.")
#     except ZeroDivisionError:
#         print("Can't divide by zero")
#         print("a/b = infinity")
#         print("a+b =", a+b)
#     except:
#         print("Something went very wrong.")

# print(divide_nums3())

# # Can't divide by zero
# # a/b = infinity
# # a+b = 6
# # None




# # Raising our own more informative error
# # This is typically what you'd be asked to do in this class
# def sum_digits_raise(s):
#     """ s is a non-empty string containing digits
#     Returns sum of all characters that are digits """
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             raise ValueError("string contained a character")  # this will halt the execution
#     return total
            
# print(sum_digits_raise("123"))
# print(sum_digits_raise("123abc"))  # ValueError: string contained a character



#########################################
########### YOU TRY IT ##################
##########################################
def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of 
        equal lengths containing numbers

    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 

    Raise a ValueError if Ldenom contains 0. """
    # your code here
    # challenge: write this with list comprehension! Fine <P

    Lnew = []

    # Lnew = [Lnum[i]/Ldenom[i] for i in range(len(Lnum))] #### this i is the index man!!!!

    # for e in Lnum: ## this will grab the character

    for e in range(len(Lnum)):
        try:
            Lnew.append(Lnum[e]/Ldenom[e])
        
        except:
            raise ValueError("nice message")

    return Lnew
    

    



    
# For example:
L1 = [4,5,6]
L2 = [1,2,3]    
print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]

L1 = [4,5,6]
L2 = [1,0,3]    
print(pairwise_div(L1, L2))  # raises a ValueError

## to run after introducing assertions
L1 = [4,5,6,7,8]
L2 = [1,8,3]    
# print(pairwise_div(L1, L2))  # raises an AssertionError

L1 = []
L2 = []    
# print(pairwise_div(L1, L2))  # raises an AssertionError