import csv
import json

tsvfile1 = open('De Novo Mutations.txt', 'r', encoding='utf16')
tsvfile2 = open('Gene Level Summary.txt', 'r')

jsonfile1 = open('data_table_1.txt', 'w', encoding='utf16')
jsonfile2 = open('data_table_2.txt', 'w')

final_list1 = []

Dict1 = {}

reader = csv.reader(tsvfile1, delimiter='\t')
next(reader)

for row in reader:
	final_list1.append(row)

Dict1["data"] = final_list1

json.dump(Dict1,jsonfile1)

final_list2 = []

Dict2 = {}

reader = csv.reader(tsvfile2, delimiter='\t')
next(reader)

for row in reader:
	final_list2.append(row)

Dict2["data"] = final_list2

json.dump(Dict2,jsonfile2)

tsvfile1.close()
tsvfile2.close()
jsonfile1.close()
jsonfile2.close()