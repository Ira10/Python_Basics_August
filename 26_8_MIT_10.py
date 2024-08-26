# ############################
# ############################
# ## Control copying, alises
# old_list = [[1,2],[3,'foo']]
# new_list = old_list

# new_list[1][0] = 'okay'

# print("New list:", new_list)
# print("Old list:", old_list)

# # Control copying, shallow copy
# import copy
# old_list = [[1,2],[3,4],[5,6]]
# new_list = copy.copy(old_list)

# old_list.append([7,8])
# old_list[1][1] = 9
# print("New list:", new_list)
# print("Old list:", old_list)

# New list: [[1, 2], [3, 9], [5, 6]]
# Old list: [[1, 2], [3, 9], [5, 6], [7, 8]]


# # Control copying, deep copy
# import copy
# old_list = [[1,2],[3,4],[5,6]]
# new_list = copy.deepcopy(old_list)

# old_list.append([7,8])
# old_list[1][1] = 9
# print("New list:", new_list)
# print("Old list:", old_list)

# # New list: [[1, 2], [3, 4], [5, 6]]
# # Old list: [[1, 2], [3, 9], [5, 6], [7, 8]]



# # EXAMPLE: aliasing
# a = 1
# b = a
# print(a)
# print(b)

# warm = ['red', 'yellow', 'orange']
# hot = warm
# hot.append('pink')
# print(hot)
# print(warm)

# 1
# 1
# ['red', 'yellow', 'orange', 'pink']
# ['red', 'yellow', 'orange', 'pink']



# # EXAMPLE: cloning
# cool = ['blue', 'green', 'grey']
# chill = cool[:]
# chill.append('black')
# print(chill)  # ['blue', 'green', 'grey', 'black']
# print(cool)  # ['blue', 'green', 'grey']

# # EXAMPLE: sorting with/without mutation
# warm = ['red', 'yellow', 'orange']
# sortedwarm = warm.sort()
# print(warm)          # ['orange', 'red', 'yellow']
# print(sortedwarm)    # None

# cool = ['grey', 'green', 'blue']
# sortedcool = sorted(cool)
# print(cool)          # ['grey', 'green', 'blue']
# print(sortedcool)    # ['blue', 'green', 'grey']

# # EXAMPLE: lists of lists of lists...
# warm = ['yellow', 'orange']
# hot = ['red']
# brightcolors = [warm]
# print(brightcolors)       # [['yellow', 'orange']]
# brightcolors.append(hot)
# print(brightcolors)       # [['yellow', 'orange'], ['red']]
# hot.append('pink')
# print(hot)                # ['red', 'pink']
# print(brightcolors)       # [['yellow', 'orange'], ['red', 'pink']]


############ YOU TRY IT AT HOME ###################
# Step through the code below without running it
# Write down what values each variable has
# Draw the memory diagram to help you keep track of aliases and clones

cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool)       # ['blue', 'green']
print(warm)       # ['red', 'yellow', 'orange']

colors1 = [cool]
print(colors1)    # [['blue', 'green']]
colors1.append(warm)
print('colors1 = ', colors1)   # [['blue', 'green'], ['red', 'yellow', 'orange']]

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']]
print('colors2 =', colors2)    # [['blue', 'green'], ['red', 'yellow', 'orange']]

warm.remove('red') 
print('colors1 = ', colors1)   #  [['blue', 'green'], ['yellow', 'orange']]
print('colors2 =', colors2)    # [['blue', 'green'], ['red', 'yellow', 'orange']]

for e in colors1:
    print('e =', e) 
# ['blue', 'green']
#  ['yellow', 'orange']


for e in colors1:
    if type(e) == list:
        for e1 in e:
            print(e1)
    else:
        print(e)     
# blue
# green
# yellow
# orange

flat = cool + warm
print('flat =', flat)      # flat = ['blue', 'green', 'yellow', 'orange']

print(flat.sort())         # None
print('flat =', flat)      # flat = ['blue', 'green', 'orange', 'yellow']

new_flat = sorted(flat, reverse = True)
print('flat =', flat)           # flat = ['blue', 'green', 'orange', 'yellow']
print('new_flat =', new_flat)   # new_flat = ['yellow', 'orange', 'green', 'blue']

cool[1] = 'black'
print(cool)            # ['blue', 'black']
print(colors1)         # [['blue', 'black'], ['yellow', 'orange']]