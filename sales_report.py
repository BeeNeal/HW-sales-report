"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []
melons_sold = []

f = open("sales-report.txt")
for line in f:
    line = line.rstrip() #eliminate white space
    entries = line.split("|") # returns list of strings separated at "|""
    salesperson = entries[0] # name of salesperson is the first string
    melons = int(entries[2]) # converts the third string to an integer

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])