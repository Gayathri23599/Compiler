import ner
import pre
import pos
import csv
import re
import semantic_map
user = []
with open('input.csv',) as csvfile:
	csvreader = csv.DictReader(csvfile,delimiter='#')
	for row in csvreader:
		#print(row)
		word = row['Input']
		word = re.sub('[.,!"]','',word)	
		print (word)
		token = pre.pre_processing(word)
		print(token)
		part_of_speech = []
		part_of_speech = pos.pos_tagging(token)
		print(part_of_speech)
		ner_tag = ner.ner_tagging(part_of_speech)
		print(ner_tag)
		
