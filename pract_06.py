marks = 75

if marks >= 90:
    print("A")
elif marks >=30:
    print("B")
else:
  print("Fail")



  for number in range(1,6):
      print(number)
      number += 1


count = 1

while count <= 3:
    print("Attempt:",count)
    count +=1

for number in range(1, 6):
    if number == 3:
        continue  # Skip 3

    if number == 5:
        break     # Stop the loop

    print(number)