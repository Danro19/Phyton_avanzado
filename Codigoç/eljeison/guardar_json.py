import json 

#lista = ["Daniel", "Maria", "Maria", "Ada", "Julian", "Gabriel", ["Julian", "Ricardo"]]
campers = {
    1:{
        "nombre":"Daniel",
        "Edad": 21,
        "sexo":"m",
        "telefonos":[123,456]
    },
    2:{
        "nombre":"Maria",
        "Edad": 20,
        "sexo":"f",
        "telefonos":[789]
    }     


}
with open("datos.json", "w") as fd:
    json.dump(campers,fd )

if not fd.closed:
    fd.close          

