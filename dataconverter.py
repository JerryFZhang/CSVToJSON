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
            print row
            itemCounter = 0
            temp = "{"
            for item in row:
                a = item
                print "---------------"
                print a
                #print the item name.
                # temp += a 
                # temp += ', '
                nameCounter = 0
                for item in fieldnames:
                    if itemCounter == nameCounter:
                        # print "---------------"
                        print item
                        # print the fieldname that matches the location counter.
                        # print itemCounter
                        # print nameCounter
                        temp+= ' "'
                        temp+= item
                        temp+= '"'
                        temp += ': "'
                        temp += a 
                        temp += '",'
                
                    nameCounter += 1
            
                itemCounter += 1
                # print "---------------"
            temp = temp[:-1]
        
            temp += "}"
            print temp
            out += temp
            out += ", "
        counter += 1
        
        # print "******SET******"
        # print fieldnames
        
                

# 




# out = json.dumps( [ row for row in reader ] )
# print out
# out = out.replace("[","{")
# print out

# out = out.replace("]","}")
# print out

    jsonfile.write(out)
