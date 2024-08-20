# ############### YOU TRY IT #######################
# # Write a function that meets the specification:
# def make_ordered_list(n):
#     """ n is a positive int
#     Returns a list containing all ints in order 
#     from 0 to n (inclusive)
#     """
#     # your code here
#     L = []
#     for i in range(n+1):  # range(0, n+1): 0 is default
#         L.append(i)
#         # return L
#     return L


# print(make_ordered_list(6))  # prints [0, 1, 2, 3, 4, 5, 6]




# ############ YOU TRY IT ###############   MY    Solution 
# def remove_elem(L, e):
#     """ 
#     L is a list
#     Returns a new list with elements in the same order as L
#     but without any elements equal to e. 
#     """
#     # your code here
#     new_list = []
#     for i in L:
#         if i == e:
#             pass 
#         else:
#             new_list.append(i)
#     return new_list
  
# L = [1,2,2,2]
# print(remove_elem(L, 2))    # prints [1]
# L = [1,2,2,2]
# print(remove_elem(L, 1))    # prints [2,2,2]
# L = [1,2,2,2]
# print(remove_elem(L, 0))    # prints [1,2,2,2]




# ###### YOU TRY IT ###############   MIT    Solution 
# def remove_elem(L, e):
#     """ 
#     L is a list
#     Returns a new list with elements in the same order as L
#     but without any elements equal to e. 
#     """
#     # your code here
#     new_list = []
#     for i in L:
#         if i != e:
#         # if i not in e: ### wrong line as e is an integer, and i not in e will raise an error 
# # because the in operator expects a sequence (like a list, string, or tuple) on the right-hand side.
#             new_list.append(i)
#     return new_list
  
# L = [1,2,2,2]
# print(remove_elem(L, 2))    # prints [1]
# L = [1,2,2,2]
# print(remove_elem(L, 1))    # prints [2,2,2]
# L = [1,2,2,2]
# print(remove_elem(L, 0))    # prints [1,2,2,2]



# s = '1274hcv'

# print(list(s)) # ['1', '2', '7', '4', 'h', 'c', 'v']

# print(s.split('4'))  # ['127', 'hcv']

# print(s.split('c')) # ['1274h', 'v']

# print(s.split())  # ['1274hcv']



# L = ["abc"]
# L_ = ['a','b','c']

# A = ''.join(L)
# B =''.join(L_)
# C = '_'.join(L_)

# print(A)
# print(B)
# print(C)


# ####### YOU TRY IT ###################     my solution
# # Write a function that meets this specification
# def count_words(sen):
#     """ sen is a string representing a sentence 
#     Returns how many words are in sen (i.e. a word is a 
#     a sequence of characters between spaces. """
#     # your code here
#     count = 0
#     split_ = s.split()
#     for i in split_:
#         count += 1
#     return count

# s = "Hello it's me"
# print(count_words(s))   # prints 3

# s = "I just took a DNA test turns out I'm 100% splitting strings"
# print(count_words(s))   # prints 12


# ####### YOU TRY IT ###################     MIT solution
# # Write a function that meets this specification
# def count_words(sen):
#     """ sen is a string representing a sentence 
#     Returns how many words are in sen (i.e. a word is a 
#     a sequence of characters between spaces. """
#     # your code here
#     count = 0
#     split_ = s.split()
#     return len(split_)

# s = "Hello it's me"
# print(count_words(s))   # prints 3

# s = "I just took a DNA test turns out I'm 100% splitting strings"
# print(count_words(s))   # prints 12

L = [4,2,7,0,1,6,9,8,3,5,2]  # [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9] if 2 is added one more

print(L.sort())  # None
print(L)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


print(L.reverse())  # None
print(L)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(sorted(L))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L)  #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


print([1,(4,5)].sort()) # TypeError: '<' not supported between instances of 'tuple' and 'int'


