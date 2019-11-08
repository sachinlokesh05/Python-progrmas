import json
with open("JSON.json") as f:
    data=json.load(f)
print(data)
print(type(data))

# with open("data.txt","r") as f:
dump=json.dumps(data)
print(dump)
print(type(dump))