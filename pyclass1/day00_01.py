import csv
 
f = open('ddareng.csv', 'r')
rdr = csv.reader(f)
wedo = []
keungdo = []
for line in rdr:
    wedo = line[9]
    keungdo = line[10]
    print(wedo, keungdo)
f.close()