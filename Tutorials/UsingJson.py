import json

data = '{"var1":"Prajwal", "var2": 56}'
#parsing the json
parsed = json.loads(data)
print(parsed['var1'])
print(data)