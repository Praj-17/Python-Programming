d1 = { }
#print(type(d1))
d2 = {"prajwal" : "chocolate", "aishu" : "dabeli", "saumya" : {"B": "maggie", "L": "roti", "D":"tp"}}
print(d2["saumya"] ["B"] )
d2["sanika"] = "Junk food"
d2[420]    = "kabab"
print(d2)
del d2[420]
print(d2) 
d3 = d2
del d3["prajwal"]
print(d2)
d4 = d2.copy()
del d4["aishu"]
print(d2)
d2.update({"leena" : "Toffee"})
print(d2)
print(d2.keys())

