import json


json_obj = dict()

with open("template.json", "r") as json_file:
    json_obj = json.load(json_file)
    print(json_obj["value-float"])
    print(json_obj["value-array"][3]["city"])
    print(json_obj["123"])
    print(json_obj)

json_obj["age"] = 18
json_obj[123] = "hello"


with open("template.json", "w+") as json_file:
    json.dump(json_obj, json_file)

print("-===================-")
str_json = json.dumps(json_obj)
print(json_obj)
print(str_json)
json_obj = json.loads(str_json)
print("-===================-")






