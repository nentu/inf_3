import yaml
f = open('task_2.json', 'w', encoding='utf-8')
json = str(yaml.safe_load(open("original.yml", "r", encoding="utf-8").read()))
json = json.replace('\'', '"')
json = json.replace('",', '",\n')
json = json.replace('{', '{\n')
json = json.replace('}', '}\n')
f.write(json)
f.close()
#print(json)