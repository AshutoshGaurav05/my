Dictionary = { "dictionary" : "A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.Dictionaries are used to store data values in key:value pairs. "}

# chai_types = {
#     "Masala": "Spicy",
#     "Ginger": "Sweet",
#     "Green": "Herbal",
#     "Black": "Strong"
# }
# print(chai_types["Masala"])
# print(chai_types.get("Ginger"))

# chai_types["Earl Grey"] = "Citrus"
# print(chai_types)
# print("pop: ", chai_types.pop("Green"))
# print("popitem: ", chai_types.popitem())

# squared_num = {x: x**2 for x in range(6)}
# print(squared_num)


keys = ["Masala", "Ginger", "Green", "Black"]

default_value = "Spicy"
chai = dict.fromkeys(keys, default_value)
chai_2 = dict.fromkeys(keys, keys)
print(chai)
