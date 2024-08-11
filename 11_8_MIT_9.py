# print(max(1,5))

# print('\n')

# print(max(1,5,4,2,4,21,3,442,2111))

# ###### checking out on my own
# def sum(*args):

#     sum_ = 0
#     for a in args:
#         sum_ += a 
#     return sum_

# print(sum())


# #### chatgpt, how to take user input seperated by spaces

# def sum(*args):
#     sum_ = 0
#     for a in args:
#         sum_ += a 
#     return sum_

# # Taking input from the user
# user_input = input("Enter numbers separated by spaces: ")

# # Splitting the input string into individual numbers, converting them to integers or floats, and passing them to the sum function
# numbers = map(int, user_input.split())

# # Unpacking the list of numbers into the sum function
# print(sum(*numbers))


#### chatgpt, how to take user input seperated by comma

# def sum(*args):
#     sum_ = 0
#     for a in args:
#         sum_ += a 
#     return sum_

# # Taking input from the user
# user_input = input("Enter numbers separated by comma: ")

# # Splitting the input string into individual numbers, converting them to integers or floats, and passing them to the sum function
# numbers = map(int, user_input.split(','))

# # Unpacking the list of numbers into the sum function
# print(sum(*numbers))
# print('\n')
# print(numbers)
# print('\n')



######## let's see

def sum(*args):
    # args = int(input())
    sum_ = 0
    for a in args:
        sum_ += a 
    return sum_

print(sum(1,2,3,4,5,5))
print(sum(1,2,3,4))
print(sum(4))

