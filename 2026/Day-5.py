name = "Jayasimha"
city = 'Hyderabad'
print(name)
print(city)

text = "Python"
print(text[0])
print(text[1])
print(text[-1])

text = "Developer"
print(text[0:4])
print(text[4:])
print(text[:5])
print(text[::-1])

text = "DevOps"
print(len(text))

text = "python"
print(text.upper())

text = "PYTHON"
print(text.lower())

text = "python"
print(text.capitalize())

text = "learn python"
print(text.title())

text = "I like Java"
print(text.replace("Java", "Python"))

text = "banana"
print(text.count("a"))

text = "DevOps"
print(text.find("Ops"))

text = "Python"sentence = "I love Python"
words = sentence.split()
print(words)
print("Py" in text)
print("Java" in text)

words = ["DevOps", "is", "Awesome"]
print(" ".join(words))

a = "apple"
b = "banana"
print(a == b)
print(a < b)

word = "Python"
for ch in word:
    print(ch)

text = "Python"
print(text[::-1])
text = "Python"
reverse = ""
for ch in text:
    reverse = ch + reverse
print(reverse)
