"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
# """

# salespeople = []
# melons_sold = []

# f = open("sales-report.txt")
# for line in f:
#     line = line.rstrip() #eliminate white space
#     entries = line.split("|") # returns list of strings separated at "|""
#     salesperson = entries[0] # name of salesperson is the first string
#     melons = int(entries[2]) # converts the third string (# melons sold) to an integer

#     if salesperson in salespeople: #if the salesperson is in the list:
#         position = salespeople.index(salesperson) #set position as index of salesperson list
#         melons_sold[position] += melons # adds amount of melons sold
#     else:
#         salespeople.append(salesperson) #if not in list, adds salesperson to list
#         melons_sold.append(melons)


# for i in range(len(salespeople)):
#     print "{} sold {} melons".format(salespeople[i], melons_sold[i])
#prints 

f = open("sales-report.txt")
salespeople = {}

for line in f:
    line = line.rstrip()
    data = line.split("|")
    salespeople = salespeople[data[0]] = salespeople[]