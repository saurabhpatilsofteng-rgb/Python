def add(a,b):
    return a + b

result = add(10,20)
print(result)


def greet(name, message="Welcome"):
    return f"{message},{name}!"

print(greet("saurabh"))
print(greet("Amit",message="Hello"))


#Scopes

company = "ABC"  #Global variable

def show_company():
    department = "Engineering" #local variable
    print(company)
    print(department)

show_company()


#lambada

square = lambda num: num * num
print(square(12))

add = lambda a,b: a + b
print(add(10,20))