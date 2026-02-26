thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 }
print(thisdict)
thisdict["colors"] = ["red", "white", "blue"]
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict["model"])
print(thisdict.get("model"))
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
del thisdict["year"]
print(thisdict)