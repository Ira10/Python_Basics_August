# def apply(criteria,n):
#     """ criteria is a function that takes in a number and returns a Boolean
#         n is an int
#     Returns how many ints from 0 to n (inclusive) match the criteria 
#     (i.e. return True when criteria is applied to them)
#     """ 
#     count = 0
#     for i in range(0, n+1):
#         if criteria(i):
#             count += 1
#     return count

# def is_even(x):
#     return x%2==0

# def is_5(x):
#     return x%2==1

# # print('apply with is_5:',apply(is_5,10))
# print('apply with anon fcn:', apply(lambda x: x==5, 7))
# print('\n')
# print(is_even(8))
# print('\n')
# print((lambda x:x%2==0)(0))
# print('\n')

#########################################################################################################


# def do_twice(n,fn):
#     return fn(fn(n))

# print(do_twice(3, lambda x:x**2))


#########################################################################################################


# b = 'dive9129'

# print(b[1:4])
# print(b[0:4])
# print(b[:7])
# print(b[-1])
# print(b[7])


#########################################################################################################

# te = ()
# ts = (2,)


# print('\n')

# print(ts)

# print('\n')


# ###############################################################


# t = (2,"mit",3)

# print('\n')
# print(t[0],t[1],t[2])
# print('\n')

# print(t[1:2])

# print('\n')

# print(t[1:3])

# print('\n')

# print(t[1:1])

# print('\n')

# tuple_ = (5)

# tuple_actually = (5 , )

# print(type(tuple_))


# print('\n')


# print(type(tuple_actually))

# print('\n')

# print(tuple_)

# print('\n')


# print(tuple_actually)

# print('\n')

# print(tuple_actually[0])

# print('\n')

# print(id((tuple_actually)))

# tuple_actually = (9,00)

# print(tuple_actually)




# seq = (2,'dr',78, [9,5,9],(3,5))

# print('\n')

# print(len(seq))

# print('\n')

# print(seq[3])

# print('\n')

# print(seq[3][0])

# print('\n')

# print(seq[4][1])

# print('\n')

# for e in seq:
#     print(e)

# print('\n')



##########################################################

# x = 1 

# y = 2 

# temp = x
# x = y 
# y = temp

# print(x,y)

# (x,y) = (y,x)

# print(x,y)


###################
### example with returning a tuple with many values
###################
# def quotient_and_remainder(x, y):
#       q = x // y
#       r = x % y
#       return (q, r)

# result = quotient_and_remainder(10,6)
# print(result)

# print('\n')

# (quot, rem) = quotient_and_remainder(5,2)
# print('quotient is:', quot)
# print('remainder is:', rem)

# print('\n')


############### YOU TRY IT #####################
# Write a function that meets these specifications:
def char_counts(s):
    """ s is a string of lowercase chars 
    Returns a tuple where the first value is the 
    number of vowels in s and the second value 
    is the number of consonants in s 
    """
    # your code here


print(char_counts("abcd"))  # prints (1,3)
print(char_counts("zcght"))  # prints (0,5)
