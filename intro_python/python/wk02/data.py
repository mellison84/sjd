import json
with open('animal-questions.json', "r") as read_file:
    data = json.load(read_file)

for key in data:
    print(data[key])
    record = data[key]
    if record['ans'] == 'Y':
      print(record['Q']) 

