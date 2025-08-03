marks = [5, 3, 5, 33,2]
extra_marks = [88, 78, 65, 70]
print(marks)
marks.append(99) #this will change the original list
print(marks)
marks.pop()
print(marks)
marks.extend(extra_marks) #this will add the elements of extra_marks to marks
print(marks)
marks.insert(3,62) #this will insert 62 at index 3
print(marks)
marks.remove(5) #this will remove the first occurrence of 5 from the list
print(marks)
marks.sort() #this will sort the list in ascending order
print(marks)
marks.reverse() #this will reverse the list
print(marks)
marks.count(5) #this will count the number of occurrences of 5 in the list
print(marks)
marks.clear() #this will clear the list
print(marks) # this will print an empty list
