# Simple Python program that converts CSV to JSON for my MongoDB project.
# - It converts all the csv files under the directory at once.
import csv
import json
import glob

for files in glob.glob("*.csv"):
    csvfile = open(files, 'r')
    jsonfile = open(files[:-4] + '.json', 'w')
    reader = csv.reader(open(files, 'rU'))
    fieldnames = ()
    out = 0
    for row in reader:
        temp = []
        # print row
        fieldnames = row
        break
        
    counter = 0
    out = ""
    
    for row in reader:
        if counter == 0:
            # skip
            print "0"
        else:
            # print row
            itemCounter = 0
            temp = "{"
        
            for item in row:
                a = item
                # print a
                nameCounter = 0
                
                for item in fieldnames:
                    if itemCounter == nameCounter:
                        # print item
                        temp += ' "'
                        temp += item
                        temp += '"'
                        temp += ': "'
                        temp += a 
                        temp += '",'
                
                    nameCounter += 1
                
                itemCounter += 1
            
            temp = temp[:-1]
            temp += "}"
            # print temp
            out += temp
            out += ", "
        
        counter += 1
        
    out = out[:-1]
    jsonfile.write(out)
print "End of Execution"
    
