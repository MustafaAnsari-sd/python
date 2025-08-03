#create a list containing the table of 5
'''
table =[]
for i in range(1, 11):
    table.append(5 * i)

print(table)
'''
#instead of writing the above code, we can use list compehension 

table = [5 * i for i in range(1, 11)]
print(table)