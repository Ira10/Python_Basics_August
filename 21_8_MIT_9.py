#############
# Loops over lists
###############
def square_list(L):
    for i in range(len(L)): 
        L[i] = L[i]**2

print(square_list([2,3,4]))  # prints None

Lin = [2,3,4]
print("before fcn call:",Lin) #[2,3,4]
square_list(Lin)
print("after fcn call:",Lin)   # mutated L    # [4,9,16]

print(square_list(Lin)) # prints None just like 8th line


A = square_list(Lin)
print(A)  # prints None just like 8th and 15th line


my_list = [4,5,6,7,8]
for i in range(len(my_list)):
    my_list[i] = my_list[i]**2 # Understanding Assignment in Python
# In Python, the = sign is used to assign a value to a variable (or in this case, an element in a list). 
# This doesn't mean that the left side (the variable or list element) is equal to the right side in a mathematical 
# sense; instead, it means "take the value on the right side and store it in the variable on the left side."

print(my_list)


L = [1,2,3]

for i,e in enumerate(L):
    print(i,e) 
# 0 1
# 1 2
# 2 3

##############  Tricky example 1  ############

# TRICKY EXAMPLE 1: append to L white iterating over range(L)

L = [1,2,3,4]
for i in range(len(L)):
    L.append(i) 
    print(L)



############
# TRICKY EXAMPLE 2: append to L while iterating over L
# this leads to an infinite loop
############
L = [1,2,3,4]
i = 0
for e in L:
    # print(e)
    L.append(i)
    # print(i)
    # print(L)
    i += 1
    print(L)
    if i == 10:
        break


# extend a list
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2
L1.extend([0,6])
L2.extend([[0,2],[7,9]])

print(L1)   # [2, 1, 3, 0, 6]

print(L2)    # [4, 5, 6, [0, 2], [7, 9]]

print(L3)     # [2, 1, 3, 4, 5, 6]


#############
# TRICKY EXAMPLE 3: combining
#############
L = [1,2,3,4]
for e in L:
    L = L + L
    print(L)
    print(len(L), " is i am printing")
    print("Done")

# Ans 

# [1, 2, 3, 4, 1, 2, 3, 4]
# 8  is i am printing
# Done
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# 16  is i am printing
# Done
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# 32  is i am printing
# Done
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# 64  is i am printing
# Done


#############
# Clear a list and check that it's the same object
###############
L = [4,5,6]
print(L)
print(id(L))
L.clear()
print(L)
print(id(L)) # same as 3 lines up, same object

## vs.

L = [4,5,6]
print(L)
print(id(L))
L = []
print(L)
print(id(L))  # different than 3 lines up, different object!