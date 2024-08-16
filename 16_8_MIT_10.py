# tuple_ = (4,5,6,)

# print(tuple_)

# print(tuple_[2])

# tuple_[0] = 7

# print(tuple_)


# list_ = [4,5,6,]

# print(list_)

# print(list_[2])

# list_[0] = 7

# print(list_ )


# t = (1,2,3)
# print(id(t))

# t = (4,2,3)

# print(id(t))


# L = [1,2,3,4] 

# L.append(5,6,7) ##TypeError: list.append() takes exactly one argument (3 given)

# print(L)

################
## EXAMPLE: change value in a list and appending a value to a list
##############
# L = [2, 4, 3]
# print(L)
# L[1] = 5
# print(L)
# L = L.append(5) ## commenting this gets me [2, 5, 3] 
# print(L) ## None



############ YOU TRY IT #####################
##### What is the value of L1, L2, L3, and L after these commands?
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.append(L4)
L = L2.append(L3)
print(L3)  # ['do', ['re', 'mi']]
print(L)  # None
print(L4)  # ['re', 'mi']



