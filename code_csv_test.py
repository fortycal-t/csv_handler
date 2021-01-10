import csv, json, pandas as pd
data = {}
jsonFilePath = "csv_json.json"

#file handling

with open('sandbox-installs.csv','r', encoding='utf-8')as f:
    reader = csv.DictReader(f)
    pandas_data = pd.read_csv(f)
    for row in reader:
        user_id = row["user_pseudo_id"]
        data[user_id] = row

with open(jsonFilePath,"w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
    print("JSON file created!")

#data summary (using Pandas library)

india =len(pandas_data[pandas_data['geo_country'] == "India"])
sony_version = (pandas_data[(pandas_data['device_brand_name'] == 'Sony') &
                                  (pandas_data['app_version'] == "1.20.1")])
sony = len(sony_version)
languages = pd.value_counts(pandas_data['device_language'])
languages_length = len(languages)

print("Number of users in India: " + str(india) +".")
print("There are "+ str(sony) +" users using a Sony device, with version 1.20.1.")
print(str(languages_length) + " languages are being used.")


#SQL

with open('sandbox-installs.csv','r', encoding='utf-8')as f:
    csv_file = csv.reader(f)
    header = next(csv_file)
    headers = map((lambda x: '`'+x+'`'), header)
    insert = 'INSERT INTO Table (' + ", ".join(headers) + ") VALUES " #this is the SQL insert string
    
    for row in csv_file:
        values = map((lambda x: '"'+x+'"'), row)
        #print (insert +"("+ ", ".join(values) +");" )
        #uncomment above line to view insert statement
   


