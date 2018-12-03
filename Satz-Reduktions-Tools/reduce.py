import csv 

with open('/Users/Nils/Projekte/Satz-Reduktion/pia_output.txt', 'r') as tsvin, open('new.csv', 'wb') as csvout:
  tsv4reader = csv.reader(tsvin, delimiter='\t')
  #csvout = csv.writer(csvout)


# Format ist ein Problem
  for row in tsvin:
    #row = row.split(" ")
    
    if "B-PER" in row:
        row = "irgendwer"

    if "B-ORG" in row:
        row = "irgendwo"


    print(row)
