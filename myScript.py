import json
import csv
jsonFile = open('spec.json')
data = json.load(jsonFile)
jsonFile.close()
arrayList1 = data['ColumnNames']
arrayList2 = data['Offsets']
columns = tuple(map(tuple, zip(arrayList1, list(map(int, arrayList2)))))
with open('fixedWithFile.txt', 'w', encoding='cp1252') as fixed_width_file:
    fixed_width_file.write(''.join([(field_name).ljust(width) for field_name, width in columns]))
    
def delimit(xCor,len):
    location = 0
    for length in len:
        yield xCor[location:location + length]
        location += length

with open("fixedWithFile.txt") as fixed_width_file:
        for line in fixed_width_file:
            with open('mohitcsv.csv', 'w', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(list(delimit(line, list(map(int, arrayList2)))))