import json

with open('data.json') as read_file:
    data = json.load(read_file)


print(data)

data['nume']['varsta'] = '30'

with open('data.json', mode='w') as write_file:
    json.dump(data, write_file)


# Real life scenarios
import requests
import json

# Get data from JSON
#data = requests.get('https://jsonplaceholder.typicode.com/todos')
#assert data.status_code == 200

#json_data = json.loads(data.text)
#print(json_data)
#print(type(json_data))


# Post data with JSON
payload = {
    "title": "a title",
    "body": "some body",
    "userid": 666
}
headers = {"Content-type": "application/json; charset=UTF-8"}

result = requests.post("https://jsonplaceholder.typicode.com/posts", data=json.dumps(payload), headers=headers)
print(result.status_code)
print(result.text)

# Doing get of the posted doc
data = requests.get('https://jsonplaceholder.typicode.com/todos/101')
print(data.text)