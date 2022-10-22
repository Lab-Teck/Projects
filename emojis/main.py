def emojis():
    emoji1 = {

        ":)": "😊",
        "):": "😢",
        "(::)": "❤"

    }
    return emoji1


message = input("> ")
constant = message.split()
output = ""
for r in constant:
    output += emojis().get(r, r) + " "
print(output)