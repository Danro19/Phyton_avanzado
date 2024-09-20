import json
import pprint

with open("datos.json", "r") as fd:
    estructura = json.load(fd)

pprint.pprint(estructura)
print(type(estructura))