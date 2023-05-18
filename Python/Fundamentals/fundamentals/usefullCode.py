fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)
#============================================
drawers = ["documents", "envelopes", "pens"]
    
# access the drawer with index of 0 and print value
print(drawers[0])  #prints documents
# access the drawer with index of 1 and print value
print(drawers[1]) #prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2]) #prints pens
    
# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]
    
# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

#===================================
# play around with the drawers!
drawers = ['documents', 'envelopes', 'pens']

# Print the second value from the list (envelopes)
print(drawers[1])
# Change "pens" to "useless manuals"
drawers[2]="useless manuals"
# Change the first value to whatever is the second value
drawers[0]=drawers[1]
# What should the list look like now?
print(drawers)
# Print the list! Does it match your prediction?

#=======================================
nums = [1,2,3,4,5]
nums.append(99)
print(nums)
#the output would be [1,2,3,4,5,99]

#======================================
words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']
    
# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']

#====================================
some_nums = [44,56,2,3,12,19,6]
print("Get started by writing your own code!")

# Some optional challenges to assess and refine your understanding:

# Print the length of the list.
print(len(some_nums))
# Print the highest value in a sequence
print(max(some_nums))
#Print the lowest value in a sequence.
print(min(some_nums))
#print a sorted sequence
print(sorted(some_nums))

# Use another python built-in function and print the result.

# Remove an item from the list. Remember to verify that it was removed.
some_nums.pop()
print(some_nums)
# Utilize a method from the documentation and print the result.


# list.pop(index) remove a value at given position. if no parameter is passed, it will remove the last value in the list.
some_nums.pop(4)# 4=array[4] in js
print(some_nums)
# list.index(value) returns the index (position) of the given value if it exists in the list and raises an error if it does not exist.
some_nums.index(44)#==== need explenation
# list.reverse() reverses the order of the elements, in place.*
some_nums.reverse()
print(some_nums)
# list.sort() sorts the items in order of least to greatest, or alphabetically for strings, in place.*
some_nums.sort()
print(some_nums)
# list.append(value) appends a value to the end of the list.
some_nums.append("thia")
print(some_nums)
#see more
#? https://docs.python.org/3/tutorial/datastructures.html 
#? https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
#? https://docs.python.org/2/library/functions.html#range
#? https://docs.python.org/3/tutorial/datastructures.html

for x in range(0,10):
    if x%5== 0:
        continue #skip condition (wont print x multiple of 5 )
    print(x)

for y in range (0,2):
    for x in range(1,10):
        if x%5== 0:
            break #leave parent loop on condition
        print('x =',x)
    print(y)

# concatenate = lasa9