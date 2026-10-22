text = " python Developer "


print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("Develoer","Engineer"))
print(text.strip().split())


#List compresion
#A compresion creates a collection using a concise expression

numbers = [1,2,3,4,5,6,7]

squares = [number ** 2 for number in numbers]

evens = [number for number in numbers if number % 2 == 0]

print(squares)
print(evens)

#Dictionary compresion

numbers = [1,2,3,4]

square_map = {
    number: number ** 2
    for number in numbers
}

print(square_map)