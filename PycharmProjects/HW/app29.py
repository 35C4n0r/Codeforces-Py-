fun = input(">")
words = fun.split(" ")
output = " "
emojis = {
    ":)": "😁😃",
    ":(": "😪😪"
}
for word in words:
    output += emojis.get(word, word) + " "
print(output)
