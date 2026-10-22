#list
#orderd and mutable and duplicates are allowed

names = ["Amit","Ravi","Amit"]
names.append("neha")
print(names[0])




#tuple
#orderd and immutable


point = (10,20)
print(point[0])

#set
#store unique values

ids = {1,2,3,4,5}
print(ids)

#Dictionary
#Store kay-value pairs

emp = {
    "name": "Amit",
    "salary": 50000
}

print(emp["name"])


employees = [
    {"id": 1, "name": "Amit", "salary": 50000},
    {"id": 2, "name": "Neha", "salary": 60000},
    {"id": 3, "name": "Ravi", "salary": 45000}
]

for employee in employees:
    if employee["salary"] >= 50000:
        print(employee["name"], employee["salary"])