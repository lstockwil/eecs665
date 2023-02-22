#Generates expected test cases from oracles for any .jeff files present

import json 
import glob
import os

folder_path = "" # Change to your absolute folder path to this folder. On Mac, my url path was "/Users/luca/Desktop/EECS 665 Project 3/p3/p3_tests/"

tests = glob.glob("*.jeff")
print("tests filenames: ")
print(tests)

# iterate through names and 
for file_name_jeff in tests:
	name = file_name_jeff.split(".jeff")[0] # removes the extension from the filename
	print(name)

	#make curl request and store output in file called {name}.json
	command = "curl -F input=@\"" + folder_path + "/" + file_name_jeff + "\" https://compilers.cool/oracles/o3/api.php >" + name + ".json"

	os.system(command)

	#open filename and load it into file
	with open(name + ".json") as json_file:
		data = json.load(json_file)

		#print (data["latestOut"])

		f = open(name + ".unparse.expected","w+")
		f.write(data["latestOut"])
		f.close()

		#err isn't used for this project
		#f = open(name + ".err.expected", "w+")
		#f.close()
