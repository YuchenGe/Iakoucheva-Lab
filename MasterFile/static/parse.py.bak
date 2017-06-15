import csv
import json

tsvfile = open('MasterFile.txt', 'r', encoding='utf16')
jsonfile = open('data.txt', 'w', encoding='utf16')

final_list = []

Dict = {}

reader = csv.reader(tsvfile, delimiter='\t')
next(reader)

for row in reader:
	final_list.append(row)

Dict["data"] = final_list

json.dump(Dict,jsonfile)

tsvfile.close()
jsonfile.close()