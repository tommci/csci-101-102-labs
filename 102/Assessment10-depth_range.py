#   Thomas McInnes
#  ​ CSCI 102 – Section B
#   Assessment 10
#   References: Zybooks csv files
#   Time: 2 hours

import csv
newlist = [['Depth', 'Start Depth', 'End Depth', 'Difference in Depth', 'Formation', 'Age of Formation']]
currentlist = []
starts = []
ordered = []
already_parsed = []

with open('formations.csv', 'r') as file:
    contents = csv.reader(file, delimiter=',')
    
    j = 0
    for i in contents:
        if j != 0:
            if i[1] not in already_parsed:      # Checks if a certain formation has already been checked
                range = i[0]
                already_parsed.append(i[1])
                currentlist.append(range)
                range_split = range.split('-')          # Splits depth range into a lower and higher value
                starts.append(range_split[0])           # Unsorted list of starting values
                ordered.append(range_split[0])          # Sorted list of starting values   
                diff = float(range_split[1]) - float(range_split[0])
                currentlist.append(float(range_split[0]))
                currentlist.append(float(range_split[1]))
                currentlist.append(f'{diff:.2f}')
                currentlist.append(i[1])
                if float(range_split[0]) < 700.0:
                    currentlist.append('Paleocene')
                else:
                    currentlist.append('Cretaceous')
                newlist.append(currentlist)
                currentlist = []
                j += 1
        else:
            j += 1
        
    ordered.sort(key=float)     # Sorts list of starting values

    with open('formations_parsed.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(newlist[0])
        newlist.remove(['Depth', 'Start Depth', 'End Depth', 'Difference in Depth', 'Formation', 'Age of Formation'])
        j = 0
        
#        for i in starts:    # Compares unsorted list (newlist) to sorted version using the starting values set up earlier
