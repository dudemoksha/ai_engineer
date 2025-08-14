a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in a:
    b = []
    if isinstance(i, list):
        b.extend(i)
        print(max(b)+min(b))
# Dictionary basics
d = {"name": "Moksha", "level": "AI Engineer"}
d["city"] = "Hyderabad"  # Add new key
print(d["name"])  # Access value
print(d.get("country", "Not Found"))  # Safe access
print(d.keys(), d.values(), d.items())  # All keys/values/items

# Remove element
d.pop("level")
# or
# del d["city"]

# Set basics
s = set([1, 2, 3])
s.add(4)
s.add(3)  # no duplicates
print(s)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))         # All unique
print(a.intersection(b))  # Common
print(a.difference(b))    # In a not in b'''