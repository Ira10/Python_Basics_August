#############
## TRICKY EXAMPLE 4: removing element as you are mutating a list
#############
## this is an incorrect way to do it
def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
remove_dups(L1, L2)
print(L1)



## this is an incorrect way to do it
def remove_dups(L1, L2):
    L1_copy = L1 # not actually a copy, just an alias!!
    for e in L1:
        if e in L2:
            L1.remove(e)

# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# remove_dups(L1, L2)
# print(L1)
            

## this is the CORRECT way to do it
def remove_dups(L1, L2):
    L1_copy = L1[:] # actually a copy aka clone
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
print(L1)