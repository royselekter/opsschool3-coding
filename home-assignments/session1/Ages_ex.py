import os
import pprint
import yaml
import json

#from pprint import pprint


with open('my_list.json') as file:
    data = json.load(file)

pprint.pprint(data)


buckets = {"11-20": [],
			"20-25": [],
			"25-40": [],
			"40-130": []}

for name,age in data["ppl_ages"].items():
	if age>=11 and age<=20:
		a = "11-20"
		print ( a + " : " + name)
		#python_dict = ast.literal_eval("{'a': 'name'}")
		#print (python_dict)
	elif age>20 and age<=25:
		a = "20-25"
		print ( a + " : " + name)
		#print (name)
	elif age>25 and age<=40:
		a = "25-40"
		print ( a + " : " + name) 
	else:
		a = "40-130"
		print ( a + " : " + name) 
		#print (name)
	buckets[a].append(name)

pprint.pprint(buckets)


with open('data.yml', 'w') as outfile:
    yaml.dump(buckets, outfile, default_flow_style=False)