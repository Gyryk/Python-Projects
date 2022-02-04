# Learning Python and dat

text = input("Go crazy: ")

print(f"My mans said {text.lower()}")

texts = [text, "lol", "peepee", "poopoo"]

cells = [
    ("Quarter", "Sales"),
    ("Q1", 2792)
]

texts.append("stinky")

joinedTexts = ", " .join(texts)

oldTexts = joinedTexts.split(",")
joinedTexts = joinedTexts.strip()

for i in range(len(texts)):
    print(texts[i] + "\n")

print(joinedTexts)
print(oldTexts)

original_string = "wowowow"
sliced_string = original_string[3:-1]

print(sliced_string)