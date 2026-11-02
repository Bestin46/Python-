keys = input("Enter keys: ").split()
values = list(map(int, input("Enter values: ").split()))
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print("\nDictionary:", d)
values_list = list(d.values())
values_list.sort()
sorted_d = {}
for v in values_list:
    for k in d:
        if d[k] == v and k not in sorted_d:
            sorted_d[k] = v
print("Sorted Dictionary:", sorted_d)
keys2 = input("\nEnter keys for second dictionary: ").split()
