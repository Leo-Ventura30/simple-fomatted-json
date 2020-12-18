import json

dic = {
    "nome": "Jhow",
    "linguagem": "Python",
    "similar": ["C", "lisp"],
    "users": 10000
}

dic_dumps = json.dumps(dic)

with open('./dados.json', 'w') as file:
    file.write(json.dumps(dic))

with open("./dados.json", "r") as file:
    text = file.read()
    datas = json.loads(text)

print(datas)
print(datas["nome"])
