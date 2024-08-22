# L = [1,2,3]

# print("L is ", L , " and id of L is ", id(L))

# L_new = L[:] # syntax for making  a copy
# print("L is ", L_new , " and id of L is ", id(L_new))

# # the above 2 lines are making a new object at memory
# # L is  [1, 2, 3]  and id of L is  4314231552
# # L is  [1, 2, 3]  and id of L is  4312932288


# L_new = L
# print("L is ", L_new , " and id of L is ", id(L_new))

# #the above 2 lines are i am renaming a same object, so memory location is same
# # L is  [1, 2, 3]  and id of L is  4334597120
# # L is  [1, 2, 3]  and id of L is  4334597120



# def remove_all(L,e):   ### my solution
#     """
#     L is a list
#     Mutates L to remove all elements in L that are equal to e
#     Returns none
#     """
#     L_copy = L[:]  # make a copy
#     L.clear()   # L becomes []
#     # print(L)
#     for i in L_copy:
#     #     if i == e:
#     #         pass 
#     #     else: 
#     #         L.append(i)
#     # return L
#         if i!= e:
#             L.append(i)
#     # no need to return L, as the L is already mutated
        

# Lin = [1,2,2,2]
# remove_all(Lin, 2)
# print(Lin)    # prints [1]

# Lin = [1,2,2,2]
# remove_all(Lin, 1)
# print(Lin)    # prints [2, 2, 2]

# Lin = [1,2,2,2]
# remove_all(Lin, 0)
# print(Lin)    # prints [1, 2, 2, 2]



# # remove from a list
# L = [2,1,3,6,3,7,0]
# L.remove(2)
# print(L) # [1, 3, 6, 3, 7, 0]
# L.remove(3)
# print(L) # [1, 6, 3, 7, 0]
# del(L[1])
# print(L) # [1, 3, 7, 0]
# print(L.pop()) # 0
# print(L) # [1, 3, 7]


# ############
# # Removing elements
# ############

# L = [2,1,3,6,3,7,0] 
# L.pop(5) 
# print(L) # [2, 1, 3, 6, 3, 0]
# L.remove(3) 
# print(L)  # [2, 1, 6, 3, 0]
# a = L.pop()
# print(L)   # [2, 1, 6, 3]
# print(a)   # 0


# def remove_all(L,e):   ### my solution with above operation
#     """
#     L is a list
#     Mutates L to remove all elements in L that are equal to e
#     Returns none
#     """
#     L.remove(e)



# Lin = [1,2,2,2]
# remove_all(Lin, 2)
# print(Lin)    # prints [1, 2, 2] # for this let us write one more time

# Lin = [1,2,2,2]
# remove_all(Lin, 1)
# print(Lin)    # prints [2, 2, 2]

# Lin = [1,2,2,2]
# remove_all(Lin, 0)
# print(Lin)    # prints ValueError: list.remove(x): x not in list

def remove_all(L,e):   ### my solution with above operation WRONG
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns none
    """
    for i in L:
        if i == e:
            L.remove(e)

Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin)    # prints [1, 2] WRONG becuase The loop starts checking each item in the list:
# The first item is 1 (not equal to 2), so nothing happens.
# The second item is 2, which matches e, so the code removes this 2. Now the list looks like this: [1, 2, 2].
# After removing the 2, the next item the loop checks is the second 2 in the new list.
# The loop skips over the second 2 because the list has shifted, and the loop doesn’t know that the list has changed. It checks the last 2 instead, removes it, and now the list is [1, 2].
# So, the loop skips over some elements, and that’s why the list still has a 2 left.


def remove_all(L,e):   ### MIT solution CORRECT
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns none
    """
    while e in L:
        L.remove(e)

Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin)    # prints [1, 2] WRONG