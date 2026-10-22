
import json

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python\n")
    file.write("Next: FastAPI")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)


#handle exception

try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ValueError:
    print("Please enter a valid integer")
except ZeroDivisionError:
    print("Number cannot be zero")
finally:
    print("Operation completed.")


    employee = {
        "id": 101,
        "name":"Amit",
        "skills":["Python","SQL"]
    }

    json_text = json.dumps(employee,indent=2)
    print(json_text)

    restored_employee = json.loads(json_text)
    print(restored_employee)


