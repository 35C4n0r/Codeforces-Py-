number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
phone = input("phone: ")
for z in phone:
  output += number.get(z, "!") + " "
print(output)