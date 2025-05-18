marks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]

print(marks) # List without appending 63 to the list
marks.append(63) # This will change the original list to add a new element at the end: [5, 2, 21, 5, 7, 63]
print(marks) # List after appending 63 to the list

marks.pop() # This will remove the last element from the list by default: [5, 2, 21, 5, 7] after adding 63
print(marks) # List after removing the last element from the list

marks.extend(extra_marks)
print(marks)
