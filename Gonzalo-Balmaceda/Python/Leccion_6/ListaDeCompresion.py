nombres = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in nombres if p[0] == "P"]
print(alongP)

bottleC = [{"Name": "Quilmes", "Country": "Arg"},
           {"Name": "Corona", "Country": "Mx"},
           {"Name": "Stella Artois", "Country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["Country"] == "Arg"]

print(Arg)
print(bottleC)