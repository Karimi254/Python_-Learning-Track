message = "The month is february, i have dedicated my time to learn and master python programming. I am not quitting until i can program excellently."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
